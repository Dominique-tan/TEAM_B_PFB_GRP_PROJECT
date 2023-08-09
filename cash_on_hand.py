#Import Path function from pathlib
from pathlib import Path
#Import csv module
import csv

def cash_on_hand_function():
    """
    This function processes the Cash on Hand data from the CSV file 'Cash_on_Hand.csv' and identifies cash deficits.
    By comparing the cash on hand of the current day with the previous day,
    it calculates the cash deficits for each day
    No Parameters are required
    """
    # Set the file paths for reading of the "Cash_On_Hand.csv" file
    cash_on_hand_fp_read = Path.cwd() / "csv_folder" / "Cash_on_Hand.csv"
    #setup filepath for writing results to the text file, "Summary_report.txt"
    fp_write = Path.cwd() / "Summary_report.txt"

    #Creates the output text file at the specified path and filename if it doesn't already exist
    fp_write.touch()

    # Create an empty list to store data from the Cash on hand data
    cash_on_hand_list = []

    # Opens the "Cash_on_hand.csv" file for reading 
    with cash_on_hand_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        #Create a CSV reader object to read the contents of the file
        reader = csv.reader(file)
        #Skip the header row of the CSV file
        next(reader)  # Skip the header

        #Using or loop to iterate through each row in the CSV file
        for row in reader:
            #add cash on hand to the cash_on_hand_list
            cash_on_hand_list.append(row)

    # Create an empty list to store profit deficit data
    cash_on_hand_difference = []

    # Iterating through the range of days, starting from index 1 up to the length
    #of the cash_on_hand list
    for cash in range(1, len(cash_on_hand_list)):
        
        #Extract the cash on hand for the current day an previous day
        current_day = int(cash_on_hand_list[cash][1])
        previous_day = int(cash_on_hand_list[cash - 1][1])

        #Calculate the difference in cash on hand between current and previous day
        difference = current_day - previous_day

        #Use If condition to only execute the code and add the results into 
        #cash_on_hand_difference list when there is a deficit in cash on hand
        if difference < 0:
            cash_on_hand_difference.append(f"[Cash deficit] Day: {cash_on_hand_list[cash][0]}, Amount: USD {abs(difference)}")


    # Open the output text file in append mode to write cash on hand deicit
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        #Iterate through the list of cash_deficit and write each deficit to the file
        for cash_deficit in cash_on_hand_difference:
            print(cash_deficit)
            file.write(cash_deficit + "\n")
