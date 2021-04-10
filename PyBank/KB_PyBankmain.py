# Import modules / dependencies
import os   #os to join elements of file path for PC or Mac
import csv  #read csv file using .reader method

budget_data = os.path.join("Resources", "budget_data.csv")
# print(budget_data.csv)

outputpath = os.path.join("Analysis", "bank_data_analysis.txt")


# Initialize variables
total_months = 0
total = 0
net_change = 0
net_change_list = []
average_change = 0
row = 0
current_month = 0
next_month = 0
previous_month_net = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
list_of_differences = []

# Open and read csv_file called budget_data.csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row 
    csv_header = next(csv_reader)
    
    # Set up previous_month_net
    first_row = next(csv_reader)
    previous_month_net = int(first_row[1])
    total_months += 1
    total = int(first_row[1]) 


    for row in csv_reader:
      
      # Get total_months and total
      total_months += 1
      total += int(row[1])


      # Get net_change
      current_net = int(row[1])
      net_change = current_net - previous_month_net
      net_change_list.append(net_change)
      
      # swap previous_month_net = 
      previous_month_net = current_net


      # Determine greatest_increase
      if net_change > greatest_increase[1]:
          greatest_increase[0] = row[0]
          greatest_increase[1] = net_change
          

      # Determine greatest_decrease
      if net_change < greatest_decrease[1]:
          greatest_decrease[0] = row[0]
          greatest_decrease[1] = net_change


# Calculate net_change
# Formula is average_change = sum(net_change) / (months - 1)
average_change = round(sum(net_change_list) / (total_months -1),2)




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