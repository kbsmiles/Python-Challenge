#Import modules / dependencies
import os   #os to join elements of file path for PC or Mac
import csv  #read csv file using .reader method

budget_data = os.path.join("Resources", "budget_data.csv")
#print(budget_data.csv)

outputpath = os.path.join("Analysis", "bank_data_analysis.txt")


#Initialize variables
total_months = 0
total = 0
average_change = 0
row = 0
current_month = 0
next_month = 0
previous_month = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
list_of_differences = []

#Open and read csv_file called budget_data.csv
with open(budget_data) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row 
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Read through each row of data in the csv file from row 2 to end
    # for row in csv_reader:
    #     # print(row)
    #     current_month = int(row[1]) #this line calls the profit/loss value and converts it to an integer        # print(f"{next_month} - {prior_month}")
    #     # print(current_month)
        
    #     # Increased total_months by 1
    #     total_months = total_months + 1        

    #     # Sum up Total Profit/Losses (second column of csv file)
    #     total = total += float(row[1])
        
    for row in csv_reader:
        # Need to start on second month
        current_month = int(row[1]) #this line calls the profit/loss value and converts it to an integer        # print(f"{next_month} - {prior_month}")
        # print(current_month)
        if total_months >0: 
        #     Go to next row
            print(current_month - previous_month) 
            total_months = total_months + 1 
        else: 
            total_months = total_months + 1
        previous_month = current_month
            
        # Calculate the month-to-month change (increase or decrease)
        #print(f"")
        
        # Use conditional for month-to-month change to see if current change is greater than greatest_increase
            # If greater than, replace current values in greatest_increase
        
        # Use conditional to see if current change is greater than greater_decrease
            # If large negative number, replace values in greatest_decrease


        # --------------------------------------------------------------
        # setup variables for next iteration (next row)
        # set prior_value = current_row
         
# Calculate total of months in the dataset
print(total_months)

# Calculate total_change of profit/losses over the entire period

# Calculate average_change = total_change / (total_months - 1)        


# Create summary table
summary_table_output = (
    f"Financial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n"
)
print(summary_table_output)

# Save results to text file
with open(outputpath, "w") as output_text_file:
    output_text_file.write(summary_table_output)