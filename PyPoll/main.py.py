import csv

# Filepath for the CSV file
file_path = 'PyPoll/Resources/election_data.csv'
file_to_output = 'PyPoll/analysis/Election_Results.txt'

# Initialize variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the dataset
    for row in csv_reader:
        total_votes += 1
        candidate = row["Candidate"]
        
        # Track the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate results
candidates = list(candidate_votes.keys())
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
winner = max(candidate_votes, key=candidate_votes.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Prepare the output as a string
output = "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += "-------------------------\n"

for candidate in candidates:
    output += f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"

output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

# Write results to a text file
with open(file_to_output, 'w') as txt_file:  # 'w' mode for writing
    txt_file.write(output)

print(f"Results have been written to {file_to_output}")
