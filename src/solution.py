import pandas as pd
import numpy as np
import heapq
from datetime import datetime
from main import csvFilePath, doubleNumToTime

df = pd.read_csv(csvFilePath)
print(df.head())

# Space for learning some pandas basic
print("\n--- PANDAS BASIC ANALYSIS ---\n")

# 1. Basic dataset information
print("Dataset shape:", df.shape)
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())

# 2. Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 3. Calculate wait times
df['waitTime'] = df['hora_llamado'] - df['hora_llegada']
df['serviceTime'] = df['hora_salida'] - df['hora_llamado']
df['totalTime'] = df['hora_salida'] - df['hora_llegada']

# Convert to human-readable format for display
print("\nSample wait times (in HH:MM:SS):")
for i in range(5):
    print(f"Customer {i+1}: Wait time = {doubleNumToTime(df['waitTime'].iloc[i])}, "
          f"Service time = {doubleNumToTime(df['serviceTime'].iloc[i])}")

# 4. Segment analysis
print("\nSegment distribution:")
segmentCounts = df['Segmento'].value_counts()
print(segmentCounts)

print("\nAverage wait time by segment:")
avgWaitBySegment = df.groupby('Segmento')['waitTime'].mean().apply(doubleNumToTime)
print(avgWaitBySegment)

# 5. Status analysis
print("\nStatus distribution:")
print(df['status'].value_counts())

# 6. Store performance
print("\nTop 5 stores by number of customers:")
print(df['tienda'].value_counts().head())

print("\nStores with longest average wait times:")
avgWaitByStore = df.groupby('tienda')['waitTime'].mean().sort_values(ascending=False).head()
print(avgWaitByStore.apply(doubleNumToTime))


# Implementation of the priority queue
"""
So our idea is to implement the theory of queues
in the following way (a priority queue): 

Add the a bool feature called isElderly where we
take into consideration the elderly poblation that
goes to coppel have same priority as the people with
more time but this two groups mentioned have more 
priority than everyone else.
"""

class Customer:
    def __init__(self, customerId, arrivalTime, segment, isElderly=False):
        self.customerId = customerId
        self.arrivalTime = arrivalTime  # Store as float (days since epoch)
        self.segment = segment
        self.isElderly = isElderly
        self.waitTime = 0  
    
    def updateWaitTime(self, currentTime):
        self.waitTime = currentTime - self.arrivalTime
    
    def __str__(self):
        return f"Customer {self.customerId} ({self.segment}), Waiting: {doubleNumToTime(self.waitTime)}, Elderly: {self.isElderly}"


class PriorityQueue:
    def __init__(self, longWaitThreshold=0.01):  # 0.01 days = ~14.4 minutes
        self.queue = []
        self.currentId = 0
        self.longWaitThreshold = longWaitThreshold
    
    def addCustomer(self, segment, isElderly=False, arrivalTime=None):
        if arrivalTime is None:
            # Use current time if not specified
            now = datetime.now()
            # Convert to days since epoch (to match the dataset format)
            arrivalTime = (now - datetime(1900, 1, 1)).total_seconds() / (24 * 3600)
        
        self.currentId += 1
        newCustomer = Customer(self.currentId, arrivalTime, segment, isElderly)
        
        # Add to priority queue
        # Priority is determined by:
        # 1. Elderly OR long wait time (lowest value = highest priority)
        # 2. Arrival time (tie-breaker)
        priority = (0 if isElderly else 1, arrivalTime)
        heapq.heappush(self.queue, (priority, newCustomer))
        
        return newCustomer
    
    def updatePriorities(self, currentTime):
        """Update wait times and adjust priorities based on wait time threshold"""
        updatedQueue = []
        
        while self.queue:
            priority, customer = heapq.heappop(self.queue)
            customer.updateWaitTime(currentTime)
            
            # If customer has been waiting longer than threshold, give high priority
            if customer.waitTime >= self.longWaitThreshold:
                priority = (0, customer.arrivalTime)  # Same priority as elderly
            else:
                priority = (0 if customer.isElderly else 1, customer.arrivalTime)
            
            updatedQueue.append((priority, customer))
        
        # Rebuild the queue
        self.queue = []
        for item in updatedQueue:
            heapq.heappush(self.queue, item)
    
    def getNextCustomer(self):
        if not self.queue:
            return None
        
        _, customer = heapq.heappop(self.queue)
        return customer
    
    def peekNextCustomer(self):
        if not self.queue:
            return None
        
        _, customer = self.queue[0]
        return customer
    
    def getQueueLength(self):
        return len(self.queue)
    
    def displayQueue(self):
        print(f"\nCurrent queue (length: {self.getQueueLength()}):")
        
        # Create a copy of the queue for display
        tempQueue = self.queue.copy()
        position = 1
        
        while tempQueue:
            priority, customer = heapq.heappop(tempQueue)
            priorityType = "High" if priority[0] == 0 else "Normal"
            print(f"{position}. {customer} - Priority: {priorityType}")
            position += 1


# Example usage of the priority queue
if __name__ == "__main__":
    print("\n--- PRIORITY QUEUE DEMONSTRATION ---\n")
    
    # Create a queue
    serviceQueue = PriorityQueue(longWaitThreshold=0.007)  # ~10 minutes
    
    # Add some customers
    currentTime = 0.5  # Noon
    serviceQueue.addCustomer("retail", False, currentTime - 0.001)  # Just arrived
    serviceQueue.addCustomer("banco", True, currentTime - 0.002)    # Elderly customer
    serviceQueue.addCustomer("afiliacion", False, currentTime - 0.008)  # Waiting >10 min
    serviceQueue.addCustomer("retail", False, currentTime - 0.003)  # Regular customer
    
    # Update priorities based on current time
    serviceQueue.updatePriorities(currentTime)
    
    # Display the queue
    serviceQueue.displayQueue()
    
    # Process next customer
    print("\nServing next customer:")
    nextCustomer = serviceQueue.getNextCustomer()
    print(nextCustomer)
    
    # Display updated queue
    serviceQueue.displayQueue()
    
    # Add more customers and update time
    print("\nAdding more customers and advancing time...")
    currentTime += 0.01  # Add ~14 minutes
    serviceQueue.addCustomer("banco", False, currentTime - 0.002)
    serviceQueue.updatePriorities(currentTime)
    
    # Display updated queue
    serviceQueue.displayQueue()
