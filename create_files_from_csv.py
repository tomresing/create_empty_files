import os

# Load the CSV file
csv_file_path = 'Enhanced_Business_Documents_Filenames.csv'  # Replace with the actual path to your CSV file

# Directory to store the new files
output_directory = './files'  # Replace with your desired directory path
os.makedirs(output_directory, exist_ok=True)
#Create a list to store the filenames
filenames = []
# Read the CSV file and extract filenames
with open(csv_file_path, 'r') as file:
    # Read each line in the file
    for line in file:
        # Split the line into columns (assuming comma-separated values)
        columns = line.strip().split(',')

        # Extract the first column (filename) and add it to the list
        filenames.append(columns[0])

# Function to create an empty file
def create_empty_file(filename):
    with open(os.path.join(output_directory, filename), 'w') as file:
        pass

# Create a new file for each filename in the CSV
for filename in filenames:
    create_empty_file(filename)

print(f"Files created in {output_directory}")
