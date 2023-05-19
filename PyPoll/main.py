#PYPOLL create a Python script that analyzes the votes and calculates each of the following values:

import os 
import csv

PyPoll_csv = os.path.join ("Resources", "election_data.csv")

with open(PyPoll_csv, newline = "") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=",")
	csv_header = next(csv_reader)
        
  votespercandidate = []
  candidatenames = []
  Stockham = []
  DeGette = []
  Doane = []
  Stockhamvotes = 0
  DeGettevotes = 0
  Doanevotes = 0
		
#The total number of votes cast
  for row in csv_reader:
		votespercandidate.append(int(row[0]))
		candidatenames.append(row[2])
	
  totalvotes = (len(votespercandidate))

  for candidate in candidatenames : 
        if candidate == "Charles Casper Stockham":
            Stockham.append(candidatenames)
            Stockhamvotes = len(Stockham)
    
        elif candidate == "Diana DeGette":
            DeGette.append(candidatenames)
            DeGettevotes = len(DeGette)

        else:
            Doane.append(candidatenames)
            Doanevotes = len(Doane)

#The percentage of votes each candidate won
percent_Stockham = (Stockhamvotes/totalvotes)*100
percent_DeGette = (DeGette/totalvotes)*100
percent_Doane = (Doane/totalvotes)*100

#The winner of the election based on popular vote

if percent_Stockham > max(percent_DeGette, percent_Doane):
        Winner = ("Charles Casper Stockham")

elif percent_DeGette > max(percent_Stockham, percent_Doane):
        Winner = ("Diana DeGette")

else: 
        Winner = ("Raymon Anthony Doane")

#Print PYBANK Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("-------------------------")
print(f"Charles Casper Stockham: {str(percent_Stockham)}% {str(Stockhamvotes)}")
print(f"Diana DeGette: {str(percent_DeGette)}% {str(DeGettevotes)}")
print(f"Raymon Anthony Doane: {str(percent_Doane)}% {str(Doanevotes)}")	
print("-------------------------")
print(f"Winner: {str(Winner)}")
print("-------------------------")

#Export PYPOLL Text File
file = open("output.txt", "w")
one = "Election Results"
two = "----------------------------"
three = str(f"Total Votes: {str(totalvotes)}")
four = "----------------------------"	
five = str(f"Charles Casper Stockham: {str(percent_Stockham)} {str(Stockhamvotes)}")
six = str(f"Diana DeGette: {str(percent_DeGette)} {str(DeGettevotes)}")
seven = str(f"Raymon Anthony Doane: {str(percent_Doane)} {str(Doanevotes)}")
eight = "----------------------------"
nine = str (f"Winner: (${str(Winner)})")
ten = "-------------------------"

file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(one,two,three,four,five,six,seven,eight,nine,ten))
