# Dependencies
import csv
import os   # os allows for path manipulation across operating systems
 
# Files to load and output
file_to_load = "C:\\Users\\flysc\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv"
# Path where the analysis output will be saved
file_to_output = "C:\\Users\\flysc\\OneDrive\\Desktop\\python-challenge\\PyPoll\\analysis\\analysis.txt"
 
# Create the analysis directory if it doesn't exist
analysis_dir = "C:\\Users\\flysc\\OneDrive\\Desktop\\python-challenge\\PyPoll\\analysis"
os.makedirs(analysis_dir, exist_ok=True)  # exist_ok=True prevents error if directory already exists
 
# Define variables to track election data
total_votes = 0
candidates = {}  # Dictionary to store candidate votes
winner = ""
winning_votes = 0
 
# Open and read the csv
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)
 
    # Read the header row
    header = next(csvreader)
 
    # Process each row of data
    for row in csvreader:
        # Count total votes
        total_votes += 1
 
        # Get candidate name from each row
        candidate = row[2]
 
        # Add candidate to dictionary if not there
        if candidate not in candidates:
            candidates[candidate] = 0
 
        # Add a vote to that candidate's count
        candidates[candidate] += 1
 
# Determine the winner
for candidate in candidates:
    votes = candidates[candidate]
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate
 
# Generate the output summary
output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
)
 
# Add each candidate's results to output
for candidate in candidates:
    votes = candidates[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n"
 
# Complete the output with winner
output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
 
# Print the output
print(output)
 
# Write the results to a text file
with open(file_to_output, "w") as txt_file:    # "w" means write mode
    txt_file.write(output)           # this is writing the output of the variables