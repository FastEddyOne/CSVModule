# Open the CSV file
# Simplify the data by filtering rows and/or columns to create a subset of the data
# Write the new data back to a different CSV file.
# Print the subset of data to the screen using f-string formatting.
# Data from https://catalog.data.gov/dataset/fdic-failed-bank-list

import csv

# Step 1: Open the CSV file (banklist.csv)
input_file = 'CSVModule/banklist.csv'
with open(input_file, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Step 2: Simplify the data by filtering rows (banks in Utah)
utah_banks = [row for row in data if row['State'] == 'UT']

# Step 3: Write the new data to a different CSV file (output.csv)
output_file = 'CSVModule/output.csv'
with open(output_file, mode='w', newline='') as file:
    fieldnames = utah_banks[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(utah_banks)

# Step 4: Print the subset of data to the screen using f-string formatting
print("Failed Banks in Utah:")
for row in utah_banks:
    print(f"Bank Name: {row['Bank Name']}, State: {row['State']}")
