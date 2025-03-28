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
   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   Once the virtual environment is activated, install the required dependencies using `pip`:
   ```bash
   pip install -r <requirements>
   ```

4. **Verify Installation**
   Run the script to ensure everything is set up correctly:
   ```bash
   python src/main.py
   ```

---

## Usage

After completing the installation steps, you can use the project as follows:

1. **Run the Script**
   Execute the main script to generate textual interpretations and visualizations:
   ```bash
   python src/main.py
   ```

2. **Check Generated Outputs**
   - Textual interpretations for the first 30 rows of the dataset will be saved in:
     ```
     reports/litInterpretationSamples.txt
     ```
   - A bar plot summarizing the counts of services by segment will be saved in:
     ```
     reports/segmentCountsPlot.png
     ```

3. **Explore the Data**
   Modify the script or extend its functionality to analyze additional aspects of the dataset.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Erick Gonzalez Parada - erick.parada101@gmail.com

Project Link: [https://github.com/HugeErick/CoppelHackaton](https://github.com/HugeErick/CoppelHackaton)
