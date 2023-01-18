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
    print()

    # Set lists for CSV data
    ballotID = []
    county = []
    candidate = []
    stockham = []
    degette = []
    doane = []

    print("Election Results")
    print()
    print("-----------------------------")
    print()

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
    print()
    print("-----------------------------")
    print()
    # print("Total Number of candidates " + str(total_candidates))
    
    # Set Votes variable to 0
    stockhamVotes = 0
    degetteVotes = 0
    doaneVotes = 0

    # Find the number of votes for each candidate
    for c_name in candidate:
        if c_name == "Charles Casper Stockham":
            stockhamVotes += 1
            stockham.append(stockhamVotes)
        elif c_name == "Diana DeGette":
            degetteVotes += 1
            degette.append(degetteVotes)
        elif c_name == "Raymon Anthony Doane":
            doaneVotes += 1
            doane.append(doaneVotes)
    
    # Find the percentage of total votes each candidate recieved 
    StockhamPercent = round(stockhamVotes / total_votes * 100, 3)
    DeGettePercent = round(degetteVotes / total_votes * 100, 3)
    DoanePercent = round(doaneVotes / total_votes * 100, 3)

    # Print the number of votes each candidate recieved and the percentage the nummber was out of all total votes
    print("Charles Casper Stockham: " + str(StockhamPercent) + "%" + " (" + str(stockhamVotes) + ")")
    print()
    print("Diana DeGette: " + str(DeGettePercent) + "%" + " (" + str(degetteVotes) + ")")
    print()
    print("Raymon Anthony Doane: " + str(DoanePercent) + "%" + " (" + str(doaneVotes) + ")")
    print()
    print("--------------------------------")
    print()

    # Find out who recieved the most votes using an if statement 
    if stockhamVotes > degetteVotes and stockhamVotes > doaneVotes:
        print("Winner: Charles Casper Stockham")
    elif degetteVotes > stockhamVotes and degetteVotes > doaneVotes:
        print("Winner: Diana DeGette")
    else:
        print("Winner: Raymon Anthony Doane")
    
    winner = ("Diana DeGette")
    print()
    print("--------------------------------")

    # Output
    output_path = os.path.join('PyPoll/Analysis/PyPollText.txt') 

   # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as text_file:
        print('Election Results', file=text_file)
        print(file=text_file)
        print('-----------------------------', file=text_file)
        print(file=text_file)
        print('Total Votes: ' + str(total_votes), file=text_file)
        print(file=text_file)
        print('-----------------------------', file=text_file)
        print(file=text_file)
        print('Charles Casper Stockham: ' + str(StockhamPercent) + '%' + ' (' + str(stockhamVotes) + ')', file=text_file)
        print(file=text_file)
        print('Diana DeGette: ' + str(DeGettePercent) + '%' + ' (' + str(degetteVotes) + ')', file=text_file)
        print(file=text_file)
        print('Raymon Anthony Doane: ' + str(DoanePercent) + '%' + ' (' + str(doaneVotes) + ')', file=text_file)
        print(file=text_file)
        print('-----------------------------', file=text_file)
        print(file=text_file)
        print('Winner: ' + str(winner) , file=text_file)
        print(file=text_file)
        print('-----------------------------', file=text_file)

  