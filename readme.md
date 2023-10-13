# CSV Data Simplifier

## Description

This Python application manages data from a CSV file containing information about failed banks. It filters the data to isolate banks in Utah, writes this subset to a new CSV file, and displays it in the terminal using f-string formatting. The original data source is the FDIC failed bank list available at [Data Gov Catalog](https://catalog.data.gov/dataset/fdic-failed-bank-list).

## Features

- **Data Filtering**: Isolates data about banks in Utah.
- **Data Writing**: Outputs the filtered data to a new CSV file.
- **Data Display**: Neatly prints the filtered data using f-string formatting.

## How to Use

### Prerequisites

- Python 3.x
- Data file in CSV format

### Steps

1. **Setup**: Ensure Python is installed and available in your system path.
   
2. **Clone Repository**: Clone this repository and navigate to the directory.

   ```sh
   git clone [[Your-Repo-Link]](https://github.com/FastEddyOne/CSVModule.git)
   cd path-to-directory
Data Preparation: Ensure your data file (banklist.csv) is in the project directory (CSVModule/banklist.csv).

Execute the Script: Run the script using Python.

sh
Copy code
python3 [script-name].py
Review Output: After execution, check the new CSV file (CSVModule/output.csv) and view the terminal output.

### Code Overview
The application follows these steps:

- Step 1: Reads initial data from banklist.csv.
- Step 2: Filters for rows where the 'State' is 'UT' (Utah).
- Step 3: Writes filtered data to output.csv.
- Step 4: Prints bank names to the terminal.

### License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

Dataset may have its own license that you can find here: https://catalog.data.gov/dataset/fdic-failed-bank-list
