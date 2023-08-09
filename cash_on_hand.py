#This function reads data from the "Cash_on_Hand.csv" file, 
#computes the difference in Cash-on-Hand between consecutive days, 
#and identifies any cash deficits (negative differences) indicating a reduction in available cash from one day to the next.

from pathlib import Path
import csv

def cash_on_hand_function():
    # Set the file paths for input and output files
    cash_on_hand_fp_read = Path.cwd() / "csv_folder" / "Cash_on_Hand.csv"
    fp_write = Path.cwd() / "Summary_report.txt"

    # Create or update the Summary_report.txt file to store the results
    fp_write.touch()

    # Create an empty list to store data from the csv file
    cash_on_hand_list = []

    # Read data from the Cash_on_Hand.csv file
    with cash_on_hand_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header

        # Populate cash_on_hand_list with data from the CSV file
        for row in reader:
            cash_on_hand_list.append(row)

    # Create a list to store details of cash deficits
    cash_on_hand_difference = []

    # Calculate differences and identify cash deficits
    for cash in range(1, len(cash_on_hand_list)):
        current_day = int(cash_on_hand_list[cash][1])
        previous_day = int(cash_on_hand_list[cash - 1][1])

        difference = current_day - previous_day

        if difference < 0:
            cash_on_hand_difference.append(f"[Cash deficit] Day: {cash_on_hand_list[cash][0]}, Amount: USD {abs(difference)}")

    # Write cash deficit details to the Summary_report.txt file
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        for cash_deficit in cash_on_hand_difference:
            # Print cash deficit details to console
            print(cash_deficit)
            # Write cash deficit details to file and add a new line
            file.write(cash_deficit + "\n")
