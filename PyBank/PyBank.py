# import dependencies
import os
import csv

# file paths to load and output
file_to_load = os.path.join("Resources/budget_data.csv")
file_to_output = os.path.join("Analysis/budget_analysis.txt")

# track parameters
total_months = 0
total_profit = 0
months = []
net_changes_list = []
prev_net = 0

# read in the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)

    # for each row...
    for row in reader:

        # update the total months and profit
        total_months += 1
        total_profit += int(row[1])

        # update the months and net changes list
        months.append(row[0])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_changes_list.append(net_change)

# calculate the average change
avg_change = sum(net_changes_list[1:])/len(net_changes_list[1:])

# calculate the greatest increase in profits and month
gi = max(net_changes_list)
gi_month = months[net_changes_list.index(gi)]

# calculate the greatest decrease in profits and month
gd = min(net_changes_list)
gd_month = months[net_changes_list.index(gd)]

# print our results to the terminal
output = (
    f"Financial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit:,}\n"
    f"Average Change: ${avg_change:,.2f}\n"
    f"Greatest Increase in Profits: {gi_month} (${gi:,})\n"
    f"Greatest Decrease in Profits: {gd_month} (${gd:,})\n"
)

print(output)

# export our results to our text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)