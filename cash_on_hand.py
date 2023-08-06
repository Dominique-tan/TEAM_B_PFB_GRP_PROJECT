#This function reads data from the "Cash_on_Hand.csv" file, 
#computes the difference in Cash-on-Hand between consecutive days, 
#and identifies any cash deficits (negative differences) indicating a reduction in available cash from one day to the next.

from pathlib import Path
import csv

def cash_on_hand_function():
 # Set file paths for the input and output files
    cash_on_hand_fp_read = Path.cwd() / "csv_folder" / "Cash_on_Hand.csv"
    fp_write = Path.cwd() / "Summary_report.txt"

    # Create empty file to store the summary report
    fp_write.touch()

    # Create empty list to store data from the csv file
    cash_on_hand_list = []

    # Open the csv file to read data
    with cash_on_hand_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # Create a csv reader object to read file content as rows
        reader = csv.reader(file)
        # Skip the header in the reader
        next(reader)

        # Iterate through each row in the file
        for row in reader:
            # Extract values from the first and second columns of the row
            day = row[0]
            cash_on_hand = float(row[1])  # Convert the cash on hand value to a float
            # Add day and cash on hand as a list to the main list
            cash_on_hand_list.append([day, cash_on_hand])

    # Create an empty list to store values for cash deficits
    cash_on_hand_difference = []

    # Using a for loop, iterate through each item in the list
    for i in range(1, len(cash_on_hand_list)):
        current_day_cash = cash_on_hand_list[i][1]
        previous_day_cash = cash_on_hand_list[i - 1][1]

        # Compute the difference in cash on hand between consecutive days
        difference = current_day_cash - previous_day_cash

        if difference < 0:
            # Append the details of cash deficits to the cash_on_hand_difference list
            cash_on_hand_difference.append(f"[Cash deficit] Day: {cash_on_hand_list[i][0]}, Amount: USD {abs(difference)}")

    # Write the cash deficits to the "Summary_report.txt" file and open in append mode
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        for cash_deficit in cash_on_hand_difference:
            # Print the cash deficits to the console
            print(cash_deficit)
            # Write the cash deficits to the file and add a new line
            file.write(cash_deficit + "\n")
            