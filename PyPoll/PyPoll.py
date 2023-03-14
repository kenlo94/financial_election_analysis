# import dependencies
import os
import csv

# file paths to load and output
file_to_load = os.path.join("Resources/election_data.csv")
file_to_output = os.path.join("Analysis/election_analysis.txt")

# total votes
total_votes = 0

# candidate options and votes
candidate_options = []
candidate_votes = {}

# winning candidate and votes
winning_candidate = ""
winning_count = 0

# read in the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    # for each row...
    for row in reader:

        # update the total votes count
        total_votes += 1

        # grab the candidates' names
        candidate_name = row[2]

        # if the candidate name is not already in the list of options...
        if candidate_name not in candidate_options:

            # add it to the list
            candidate_options.append(candidate_name)

            # begin tracking votes for each candidate
            candidate_votes[candidate_name] = 0

        # update the votes for each candidate
        candidate_votes[candidate_name] += 1

# print the results to the terminal and export them to our text file
with open(file_to_output, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------------\n"
    )
    print(election_results)
    txt_file.write(election_results)

    # determine the winner by looping through the data
    for candidate in candidate_votes:

        # retrieve the votes and percentages
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes)*100

        # print the results for each candidate to the terminal
        voter_outcome = (f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n")
        print(voter_outcome)
        txt_file.write(voter_outcome)

        # compare votes to determine winner
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
    
    # print winner to the terminal
    winner = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------------\n")
    print(winner)
    txt_file.write(winner)