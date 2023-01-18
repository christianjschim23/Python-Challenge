# Import the OS Module
import os

# Module for reading CSV Files
import csv

csvpath = os.path.join('PyPoll/Resources/election_data.csv') 

# Open the CSV
with open(csvpath) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Set lists for CSV data
    ballotID = []
    county = []
    candidate = []
    stockham = []
    degette = []
    doane = []

    print("Election Results")
    print("-----------------------------")

    # Loop through CSV file and add to lists
    for row in csvreader:
       
       # Toal number of Votes 
       ballotID.append(row[0])
    
       # Total number of Counties 
       county.append(str(row[1]))

       # Total number of Candidates
       candidate.append(str(row[2]))
    
    # Find the Total amount of votes
    total_votes = len(ballotID) 

    # Total number of Candidates 
    total_candidates = len(candidate)

    # List of candidates 
    candidates = {"Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"}

    print("Total Votes: " + str(total_votes))
    print("-----------------------------")
    # print("Total Number of candidates " + str(total_candidates))
    
    x = 0
    for candidates in (1, total_candidates):
        if candidates == "Charles Casper Stockham":
            stockham.append(x)
        elif candidates == "Diana DeGette":
            degette.append(x)
        elif candidates == "Raymon Anthony Doane":
            doane.append(x)
        x += 1

    stockhamVotes = sum(stockham)
    degetteVotes = sum(degette)
    doaneVotes = sum(doane)
    print("Charles Casper Stockham " + str(stockhamVotes))
    print("Diana DeGette " + str(degetteVotes))
    print("Raymon Anthony Doane " + str(doaneVotes))

 