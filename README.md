# Coppel Hackaton
## Nombre de equipo: Unwanted

### Integrantes:
- Erick Gonzalez Parada
- Migue Garcia Diaz de Rivera
- Emiliano Ruiz Plancarte

## Description

This project was developed as part of the **Coppel Hackathon**. The goal of the project is to analyze customer service data from a CSV file, interpret key metrics, and generate meaningful insights through textual summaries and visualizations. The project includes tools for converting fractional time values into human-readable formats, interpreting service events, and generating plots to summarize trends in the data.

## Table of contents
- [Installation](#installation)
- [Usage](#usage)
  - [Running main.py](#running-mainpy)
  - [Running solution.py](#running-solutionpy)
- [License](#license)
- [Contact](#contact)

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/HugeErick/CoppelHackaton.git
   cd CoppelHackaton
```

2. **Set Up the Virtual Environment**
A pre-configured virtual environment (`venv`) is included in the repository. To activate it:

1. On **Windows**:

```shellscript
venv\Scripts\activate
```


2. On **macOS/Linux**:

```shellscript
source venv/bin/activate
```

3. **Install Dependencies**
Once the virtual environment is activated, install the required dependencies using `pip`:

```shellscript
pip install -r requirements.txt
```

4. **Verify Installation**
Run the script to ensure everything is set up correctly:

```shellscript
python src/main.py
```

---

## Usage

After completing the installation steps, you can use the project as follows:

### Running main.py

The main script provides basic data exploration and visualization:

```shellscript
python src/main.py
```

**Expected Output:**

1. Display of the first 5 rows of the dataset
2. Demonstration of time conversion (e.g., 0.5 days = 12:00:00)
3. Generation of textual interpretations for the first 30 rows in:

```plaintext
reports/litInterpretationSamples.txt
```

4. Creation of a bar plot showing the distribution of service segments in:

```plaintext
reports/segmentCountsPlot.png
```

### Running solution.py

The solution script provides more advanced analysis and a priority queue implementation:

```shellscript
python src/solution.py
```

**Expected Output:**

1. Display of the first 5 rows of the dataset
2. Comprehensive pandas analysis including:

1. Dataset shape and data types
2. Basic statistics
3. Missing value analysis
4. Wait time calculations and conversions
5. Segment distribution and average wait times
6. Status distribution
7. Store performance metrics

3. Demonstration of a priority queue implementation that:

1. Prioritizes elderly customers
2. Gives high priority to customers waiting longer than a threshold
3. Shows queue management with various customer types
4. Displays how priorities change as wait times increase

>[!IMPORTANT]
>Both scripts can be run independently and provide different insights into the dataset.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Erick Gonzalez Parada - [erick.parada101@gmail.com](mailto:erick.parada101@gmail.com)

Project Link: [https://github.com/HugeErick/CoppelHackaton](https://github.com/HugeErick/CoppelHackaton)

