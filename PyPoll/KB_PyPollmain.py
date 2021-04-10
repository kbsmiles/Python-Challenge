#TODO pseudo code before I begin

# Import modules / dependencies
import os   #os to join elements of file path for PC or Mac
import csv  #read csv file using .reader method

election_data = os.path.join("Resources", "election_data.csv")
# print(election_data.csv)

outputpath = os.path.join("Analysis", "poll_data_analysis.txt")

# Initialize variables
total_votes = 0
correy_votes = 0
correy_percent = 0
khan_votes = 0
khan_percent = 0
li_votes = 0
li_percent = 0
otooley_votes = 0
otooley_percent = 0

# Open and read csv_file called budget_data.csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row 
    csv_header = next(csv_reader)

    for row in csv_reader:
    
        # Total votes cast
        total_votes = total_votes + 1

        # Candidates who received votes (if-else)
        if row[2] == "Correy":
            correy_votes = correy_votes + 1
                
        elif row[2] == "Khan":
            khan_votes = khan_votes + 1
        
        elif row[2] == "Li":
            li_votes = li_votes + 1
        
        else: otooley_votes = otooley_votes + 1

# Percent of votes for each candidate
correy_percent = round((correy_votes / total_votes)*100,1)

khan_percent = round((khan_votes / total_votes)*100,1)

li_percent = round((li_votes / total_votes)*100,1)

otooley_votes = round((otooley_votes / total_votes)*100,1)

# Winner of election based on popular vote
popvote_dict = {
    "Election Winner: Correy": correy_votes,
    "Election Winner: Khan": khan_votes,
    "Election Winner: Li": li_votes,
    "Election Winner: O'Tooley": otooley_votes,
}
for x in popvote_dict.values():
  print(x)

popvote_key = max(popvote_dict, key=popvote_dict.get)
# print(popvote_key)

# Create summary table
summary_table_output = (
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"------------------------\n"
    f"Correy: {correy_percent}%    {correy_votes} votes\n"
    f"Khan: {khan_percent}%    {khan_votes} votes\n"
    f"Li: {li_percent}%    {li_votes} votes\n"
    f"O'Tooley: {otooley_percent}%    {otooley_votes} votes\n" 
    f"------------------------\n"
    f"{popvote_key}\n"
)

print(summary_table_output)

# Save results to text file
with open(outputpath, "w") as output_text_file:
    output_text_file.write(summary_table_output)

