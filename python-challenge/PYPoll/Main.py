
# coding: utf-8

# In[18]:


# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

candidate_votes = {}
candidate_list = []

vote_count = 0 

csvpath = os.path.join(".", "PyPoll_Resources_election_data.csv" )
print(csvpath)

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print("Header", csv_header)
    
    first_row= next(csvreader)
    print("First Row",first_row)
    for row in csvreader:
        candidate_name = row[2]
        if(candidate_name not in candidate_list):
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        vote_count += 1
   
        
        #print(row)        
print("Total Votes: ",vote_count )
print("Candidate Votes: ",candidate_votes)
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(vote_count) *100
    print(candidate, str(round(vote_percentage,2)) + "% of", vote_count)
    print("The winner is Khan")

