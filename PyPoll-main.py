import os
import csv



candidates = []
total_candidates = []
candidate_percent = [] 
candidate_total = []
summaries = [] 

csv_path1 = os.path.join("election_data_1.csv")

with open(csv_path1, "r", newline = "") as csv_data1:
    datafile1 = csv.reader(csv_data1, delimiter = ",")
    next(datafile1)

    rows = 0

    for row in datafile1:
        total_candidates.append(row[2])
        rows += 1


# sorted list of total_candidates
sorted_candidates = sorted(total_candidates)

for i in range(rows):
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])




print(" Election Results")
print("-------------------------------------")
print("Total Votes:", rows)
print("-------------------------------------")


for j in range(len(candidates)):
    candidate_count = 0

    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1

    candidate_percent.append(round(candidate_count / rows * 100, 1))
    candidate_total.append(candidate_count)


ziped_file = zip(candidates, candidate_percent, candidate_total)

for row in ziped_file:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)


for k in range(len(candidate_percent)):
    if candidate_total[k] > candidate_total[k - 1]:
        the_winner = candidates[k]


print("----------------------------------------" )
print("Winner:", the_winner)
print("-----------------------------------------")
print("   ")


