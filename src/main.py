"""
U know u not analysing when
the pandas are missing
"""
import pandas as pd
import os
import time
import matplotlib.pyplot as plt

from itertools import islice

csvFilePath=os.path.join("pub", "v2.csv")

def doubleNumToTime(doubleNumToTime):
  hours=int(doubleNumToTime * 24)
  minutes=int((doubleNumToTime * 24 * 60) % 60)
  seconds=int((doubleNumToTime * 24 * 60 * 60) % 60)
  return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
  print("pwd: ", os.getcwd())
  df=pd.read_csv(csvFilePath);

  ###
  # Important to know that this will by 
  # default truncate the info
  # feel free to check the csv urself
  # just in case the file is shared
  # in my drive: https://drive.google.com/file/d/17DHLRpllDXFWuOBJw89n7uoNWNyE5viO/view?usp=sharing
  ###
  print(df.head())

  # First approach (understanding time features) (not an AI comment btw)
  """
  we build a basic function
  that resolves the rule of three
  """

  # Animating in python LMFAO
  time.sleep(1)

  print(
    f"So we know that 0.5 is half a day, "
      f"so let's try our function:\n"
      f"0.5 = {doubleNumToTime(0.5)}"
  )

  # Second approach
  """
  Now using the simplicity of python
  we can make some magic by interpreting the information
  in a very litteral way, you'll see how
  """

  reportsPath="reports"
  interpretationSamplesPath=os.path.join(reportsPath, "litInterpretationSamples.txt")

  # Just in case
  os.makedirs("reports", exist_ok=True)


  # We lit gonna iterate and interpret the data as following
  """
  so aparently there is something called 
  islice to manage iterations with
  respect it's limits, I hate python
  """

  with open(interpretationSamplesPath, "w") as file:
    for index,row in islice(df.iterrows(), 30):
      date=row['Fecha']
      segment=row['Segmento']
      timeArrival=doubleNumToTime(row['hora_llegada'])
      timeCalled=doubleNumToTime(row['hora_llamado'])
      timeExit=doubleNumToTime(row['hora_salida'])
      cashRegister=row['caja']
      store=row['tienda']
      status=row['status']
      state=row['estado']

      interpretation = (
        f"Row {index + 1}: On {date}, a customer arrived at approximately {timeArrival} for a {segment} service "
          f"at {store} in {state}. They were called at around {timeCalled} and left at approximately {timeExit}. "
          f"The service was handled at counter {cashRegister}, and the status was {status}.\n"
      )

      file.write(interpretation)

  # Notifying what happen
  print(
    f"\nHey, some interpretations are being generated"
      f"\nCheck them out at {interpretationSamplesPath}\n"
  )

  time.sleep(1)

  # Final approach
  """
  lets plot something no?
  """
  # Count the occurrences of each segment
  segmentCounts = df['Segmento'].value_counts()

  # Create a bar plot
  plt.figure(figsize=(10, 6))
  segmentCounts.plot(kind='bar', color='skyblue', edgecolor='black')
  plt.title('Counts of Services by Segment', fontsize=16)
  plt.xlabel('Segment', fontsize=12)
  plt.ylabel('Count', fontsize=12)
  plt.xticks(rotation=45, ha='right', fontsize=10)
  plt.tight_layout()

  plotPath = os.path.join(reportsPath, "segmentCountsPlot.png")
  plt.savefig(plotPath)

  # Show the plot (optional, if running interactively)
  plt.show()

  print(f"A bar plot summarizing the counts of services by segment has been generated.")
  print(f"Check it out at {plotPath}")
