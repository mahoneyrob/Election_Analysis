#Add our dependencies
import csv
import os

#Load the file
file_to_load = os.path.join("Resources", "election_results.csv")

#create file name to save variable and open
file_to_save = os.path.join("analysis", "election_analysis.txt")



with open(file_to_load) as election_data:

    #Read the file object with reader function
    file_reader = csv.reader(election_data)
    #print the header row
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file
    #for row in file_reader:
     #   print(row)
    








#with open(file_to_save, "w") as txt_file:


# The data we need to retrieve
# The toal number of votes cast
# A complete list of candidates who recieved votes
# The precentage of botes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

