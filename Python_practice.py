counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("Else Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties.")

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in range(3):
    print(num)

for i in range(len(counties)-1):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}




for county, voters in counties_dict.items():
    print(county, "county has", voters, "registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")    

#candidate_votes = int(input("How many votes did the candidate get? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
       # f"You received {candidate_votes:,} number of votes."
      #  f"The total number of votes in the elections was {total_votes:,}. "
      #  f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]

print(voting_data[0]["county"])

for x in range(3):
    print(f"{voting_data[x]['county']} county has {voting_data[x]['registered_voters']} registered voters.")

for y in range(2, 30, 3):
    print(y)

#for i in range(len(voting_data)):
  #  print(voting_data[i])

#for county_dict in voting_data:
  #  for value in county_dict.values():
   #     print(value)

#for county_dict in voting_data:
  #  print(county_dict["registered_voters"])

#for county_dict in voting_data:
 #   print(county_dict["county"])

