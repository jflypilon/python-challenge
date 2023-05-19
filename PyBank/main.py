import os 
import csv 

#PYBANK create a Python script that analyzes the records to calculate each of the following values:

PyBank_csv = os.path.join ("..", "Resources", "budget_data.csv")

totalmonths = 0
total_profit_losses = 0
change = 0
dates = []
profits = []
value = 0

with open(PyBank_csv, newline = "") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csv_reader)
	
	first_row = next(csv_reader)
	totalmonths += 1
	total_profit_losses += int(first_row[1])
	value = int(first_row[1])
	
	for row in csv_reader:
		dates.append(row[0])
		
		#calculating the change and adding to profit array
		change = int(row[1])-value
		profits.append(change)
		value = int(row[1])
		
		#The total number of months included in the dataset
		totalmonths +=1
		
		#The net total amount of "Profit/Losses" over the entire period
		total_profit_losses = total_profit_losses + int(row[1])

	#The changes in "Profit/Losses" over the entire period, and then the average of those changes
	total_change = sum(profits)/len(profits)

	#The greatest increase in profits (date and amount) over the entire period
	greatest_increase = max(profits)
	date_greatest_increase = profits.index(greatest_increase)
	new_date = dates[date_greatest_increase]

	#The greatest decrease in profits (date and amount) over the entire period
	greatest_decrease = min(profits)
	date_greatest_decrease = profits.index(greatest_decrease)
	worst_date = dates[date_greatest_decrease]

#Print PYBANK Analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_profit_losses)}")	
print(f"Average Change: ${str(round(total_change, 2))}")
print(f"Greatest Increase in Profits: {new_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Export PYBANK Text File
file = open("output.txt", "w")
one = "Financial Analysis"
two = "----------------------------"
three = str(f"Total Months: {str(total_months)}")
four = str(f"Total: ${str(total_profit_losses)}")	
five = str(f"Average Change: ${str(round(total_change, 2))}")
six = str(f"Greatest Increase in Profits: {new_date} (${str(greatest_increase)})")
seven = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(one,two,three,four,five,six,seven))
