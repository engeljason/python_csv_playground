import csv
from genericpath import exists
import os

election_data_csv = os.path.join("Resources","election_data.csv")
target_path = os.path.join("Analysis","election_results.txt")
# dictionary = {"Candidate": {voter1, voter2, ...}, 
#               "Candidate2": {voterx, ...}}

# for row: 
#   if candidate in dictionary:
#        dictionary[candidate].add(voterid)
#   else:
#        dictionary.update({candidate : {voterid}})


if (not os.path.exists(target_path)):
    try:
        os.mkdir("Analysis")
        newfile = open(target_path, "x")
        newfile.close()
    except:
        print("oops I don't know how these work yet")
if (not os.path.exists(election_data_csv)):
    print("\nFile not found")
    print(f"Expected to find /Resources/election_data.csv \nin current working directory ({os.getcwd()})")
else:
    with open(election_data_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        # for element in header:
        #     print(element)
        # Voter ID | County | Candidate

        
        # dictionary for holding votes for candidates sorted by county
        # {county : {candidate : {voterid, voterid}, 
        #            candidate : {voterid, voterid}},
        #  county : {candidate : {voterid, voterid}, 
        #            candidate : {voterid, voterid}}, ...}
        votes_by_county = dict()

        # dictionary for holding all votes across all counties per candidate
        # {candidate : {voterid, voterid, ...}, ...}
        votes_by_candidate = dict()

        # store each voterid to ensure no double votes
        allvoterids = set()

        for row in csvreader:
            voterid = row[0]
            county = row[1]
            candidate = row[2]

            # check for voter fraud
            if voterid in allvoterids:
                print(f"{voterid} has voted more than once!")
                # TODO: resolve the fraud somehow
                # temporary solution skips the duplicated vote (but arbitrarily leaves in the earlier vote)
            else:
                if county in votes_by_county:
                    if candidate in votes_by_county[county]:
                        votes_by_county[county][candidate].add(voterid)
                    else:
                        votes_by_county[county][candidate] = {voterid}
                else:
                    votes_by_county[county] = {candidate : {voterid}}
                
                if candidate in votes_by_candidate:
                    votes_by_candidate[candidate].add(voterid)
                else:
                    votes_by_candidate[candidate] = {voterid}

                allvoterids.add(voterid)

        output = "\nThe election results are in!\n\n"
        total = len(allvoterids)
        winner = ("", 0)

        for county, votes in votes_by_county.items():
            county_total = 0
            for voterids in votes.values():
                county_total+= len(voterids)
            output += f"In {county} County:\n"
            for candidate, voterids in votes.items():
                candidate_votes = len(voterids)
                candidate_percent = candidate_votes/county_total
                output += f"Candidate {candidate} received {candidate_votes:,} votes ({candidate_percent:.3%})\n"
            output+= f"County Total: {county_total:,}\n\n"
        output+= f"Total votes for all counties: {total:,}\n"
        for candidate, voterids in votes_by_candidate.items():
            candidate_votes= len(voterids)
            candidate_percent = candidate_votes/total
            if (candidate_votes > winner[1]):
                winner = (candidate, candidate_votes)
            output+= f"The total votes for {candidate} is {candidate_votes:,} ({candidate_percent:.3%})\n"
        output += f"\nThe winner is {winner[0]}!\n"
        
        print(output)
        with open(target_path, "w") as output_file:
            output_file.write(output)


