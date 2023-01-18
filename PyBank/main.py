# Import the OS Module
import os

# Module for reading CSV Files
import csv

csvpath = os.path.join('PyBank/Resources/budget_data.csv') 

# Open the CSV
with open(csvpath) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    print(csvreader)

    # Read the header row first (skip this if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print()

    # Set lists for CSV data
    months = []
    netPL = []
    monthlychange = []

    print("Financial Analysis")
    print()
    print("-----------------------------")
    print()

    # Loop through CSV file and add to lists
    for row in csvreader:
       
       # Total list of months
       months.append(row[0])
    
       # Total lsit of Profit/Losses
       netPL.append(int(row[1]))
    
    # Find the number of months
    total_months = len(months) 

    # Find the net amount of Profit/Losses
    net_amount =sum(netPL)
    
    print("Total Months: "+ str(total_months))
    print()
    print("Total: $"+ str(net_amount))
    print()

    for x in range(1, total_months):
        monthlychange.append(netPL[x]-netPL[x-1])
    
    # Find the average change in Profit/Losses
    def avg(monthlychange):
        length = len(monthlychange)
        total = 0.0
        for number in monthlychange:
            total += number
        return total / length
      
    average_change = avg(monthlychange)
    print("Average Change: $"+ str(average_change))
    print()

   # Find the Max Profit
    maxMonthlyChange = max(monthlychange)
   # print("Greatest Increase in Profits: " + str(maxMonthlyChange))

   # Find the Min Profit
    minMonthlyChange = min(monthlychange)
   # print("Greatest Decrese in Profits: " + str(minMonthlyChange))

   # Find the Max Month
    maxMonth = monthlychange.index(max(monthlychange)) + 1
   # print(months[maxMonth])

   # Find the min Month
    minMonth = monthlychange.index(min(monthlychange)) + 1
   # print(months[minMonth])

   # Print Max/Min months and Max/Min month amount combined
    print("Greatest Increase in Profits: " + str(months[maxMonth]) + " ($" + str(maxMonthlyChange) + ")")
    print()
    print("Greatest Decrease in Profits: " + str(months[minMonth]) + " ($" + str(minMonthlyChange) + ")")
    print()

   # Output
    output_path = os.path.join('PyBank/Analysis/PyBankText.txt') 

   # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as text_file:
        print('Financial Analysis', file=text_file)
        print(file=text_file)
        print('-----------------------------', file=text_file)
        print(file=text_file)
        print('Total Months: ' + str(total_months), file=text_file)
        print(file=text_file)
        print('Total: $'+ str(net_amount), file=text_file)
        print(file=text_file)
        print('Average Change: $'+ str(average_change), file=text_file)
        print(file=text_file)
        print('Greatest Increase in Profits: ' + str(months[maxMonth]) + ' ($' + str(maxMonthlyChange) + ')', file=text_file)
        print(file=text_file)
        print('Greatest Decrease in Profits: ' + str(months[minMonth]) + ' ($' + str(minMonthlyChange) + ')', file=text_file)
        print(file=text_file)





