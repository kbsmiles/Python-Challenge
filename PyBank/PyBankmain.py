#TODO pseudo code before I begin
#Import modules / dependencies
import os   #os to join elements of file path for PC or Mac
import csv  #read csv file using .reader method

csv_file_path = os.path.join(".", "Resources", "budget_data.csv")
print(csv_file_path)

#Open and read csv_file called budget_data.csv
with open(csv_file_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data in the csv file from row 2 to end
    for row in csv_reader:


        print(row[0], row[1])