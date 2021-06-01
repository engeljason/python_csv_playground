import os
import csv

budget_data_file = os.path.join("Resources", "budget_data.csv")
target_path = os.path.join("Analysis", "budget_report.txt")

if (not os.path.exists(target_path)):
    try:
        os.mkdir("Analysis")
        newfile = open(target_path, "x")
        newfile.close()
    except:
        print("oops I don't know how these work yet")

if not os.path.exists(budget_data_file):
    print("\nFile not found")
    print(f"Expected to find /Resources/budget_data.csv \nin current working directory ({os.getcwd()})")
else: 
    with open(budget_data_file, 'r') as csvfile:
        count = 0
        total = 0
        delta = 0
        last = 0
        maxdelta = ("", 0, 0)
        mindelta = ("", 0, 0)
        total_delta = 0
        
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            #  Count row
            count += 1

            month: str = row[0]
            profit: int = int(row[1])
            #  Total profit/losses
            total += profit
            #  Calculate this month Delta
            delta = profit - last
            #     Store this months value for next delta
            last = profit
            #     Store max delta
            if (delta > maxdelta[2]): maxdelta = (month, profit, delta)
            #     Store min delta
            if (delta < mindelta[2]): mindelta = (month, profit, delta)
            #  Calculate average delta
            total_delta += delta

    average: float = float(total_delta/count)

    output = ""
    output += "Financial Analysis\n"
    output += "-------------------\n"
    output += f"Total Months: {count}\n"
    output += f"Total: ${total:,}\n"
    output += f"Average Change: ${average:,.2f}\n"
    output += f"Greatest Increase in Profits: {maxdelta[0]}: ${int(maxdelta[2]):,}\n"
    output += f"Greatest Decrease in Profits: {mindelta[0]}: ${int(mindelta[2]):,}"

    print(output)

    with open(target_path, "w") as output_file:
        output_file.write(output)

