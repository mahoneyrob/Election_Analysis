#Add our dependencies
import csv
import os

#Load the file
file_to_load = os.path.join("Resources", "election_results.csv")

#create file name to save variable and open
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
#Track who won
winning_candidate = ""
winning_count = 0
winning_percentage = 0


with open(file_to_load) as election_data:
    with open(file_to_save, "w") as txt_file:

    #Read the file object with reader function
        file_reader = csv.reader(election_data)
    #print the header row
        headers = next(file_reader)
   
    #Print each row in the CSV file
        for row in file_reader:
            candidate_name = row[2]
        #Check to see if candidate already in list
            if candidate_name not in candidate_options:
            #Add candidate
                candidate_options.append(candidate_name)
            #insert candidate in dictionary and start counting vote
                candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] += 1
            total_votes += 1
        election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
        txt_file.write(election_results)
        print(election_results, end="")



    #loop through candidate list in candidate votes dictionary
        for candidate_name in candidate_votes:
            votes = 0
                #retrieve votes for each candidate
            votes = candidate_votes[candidate_name]
            vote_percent = float(votes) / float(total_votes) * 100 
            candidate_results = (f"{candidate_name}: received {votes:,} votes, or {vote_percent:.1f}% of the vote.\n\n")
            txt_file.write(candidate_results) 
            #calculate percent of votes
        
            #print results
            print(f"{candidate_name}: received {votes:,} votes, or {vote_percent:.1f}% of the vote.\n")
            if (votes > winning_count) and (vote_percent > winning_percentage):
                winning_candidate = candidate_name
                winning_count = votes
                winning_percentage = vote_percent
        winning_candidate_summary = (
            f"-----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n")
        txt_file.write(winning_candidate_summary)
        print(winning_candidate_summary)

    # save to text file
    
        
        
        
            


    

#Who won?

#print(f"{winning_candidate} won the election by getting {winning_count:,} votes, and {winning_percentage:.1f}% of the vote.\n\n")



#print(winning_candidate_summary)

#print(f"{total_percent:.2f}")    
#print(candidate_options)
#print(candidate_votes)
#print(f'{total_votes:,}')











# The data we need to retrieve
# The toal number of votes cast
# A complete list of candidates who recieved votes
# The precentage of botes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

