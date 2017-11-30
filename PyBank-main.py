import os
import csv
import pandas as pd

csv_path1 = os.path.join("budget_data_1.csv")
csv_path2 = os.path.join("budget_data_2.csv")
count = 0
total_revenue_change = 0
months = []
list_of_revenues = []
change_revenue = []
previous_month_value = 0

with open(csv_path1, "r", newline = "") as csv_data1:
    datafile1 = csv.reader(csv_data1, delimiter = ",")
    lines = csv_data1.readline()[1:]

    for row in datafile1:
        list_of_revenues.append(int(row[1]))
        months.append(row[0])

    for i in range(len(list_of_revenues)):
        change = list_of_revenues[i] - previous_month_value
        #print(change)
        change_revenue.append(change)
        previous_month_value = list_of_revenues[i]

    highest_revenue = int(max(list_of_revenues))
    lowest_revenue = int(min(list_of_revenues))

max_value = max(change_revenue)
index = change_revenue.index(max_value)
high_month = months[index]

min_value = min(change_revenue)
index2 = change_revenue.index(min_value)
low_month = months[index2]


print("Financial Analysis")
print("_____________________________")
print("Total Months: " + str(len(months)))
print("Total Revenue: " + str(sum(list_of_revenues)))
print("The average change in revenue " + str(round(sum(change_revenue)/41)))
print("The greatest increase in revenue was on " + str(high_month) + " "+ str(max_value))
print("The greatest decrease in revenue was on " + str(low_month) + " "+ str(min_value))


count = 0
total_revenue_change = 0
months2 = []
list_of_revenues2 = []
change_revenue2 = []
previous_month_value2 = 0

with open(csv_path2, "r", newline = "") as csv_data2:
    datafile2 = csv.reader(csv_data2, delimiter = ",")
    lines = csv_data2.readline()[1:]

    for row in datafile2:
        list_of_revenues2.append(int(row[1]))
        months2.append(row[0])

    for j in range(len(list_of_revenues2)):
        change2 = list_of_revenues2[j] - previous_month_value2
        #print(change)
        change_revenue2.append(change2)
        previous_month_value2 = list_of_revenues2[j]

   
max_value2 = max(change_revenue2)
index2 = change_revenue2.index(max_value2)
high_month2 = months2[index2]

min_value2 = min(change_revenue2)
index3 = change_revenue2.index(min_value2)
low_month2 = months2[index3]


print("Financial Analysis")
print("_____________________________")
print("Total Months: " + str(len(months2)))
print("Total Revenue: " + str(sum(list_of_revenues2)))
print("The average change in revenue " + str(round(sum(change_revenue2)/41)))
print("The greatest increase in revenue was on " + str(high_month2) + " "+ str(max_value2))
print("The greatest decrease in revenue was on " + str(low_month2) + " "+ str(min_value2))

