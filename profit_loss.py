#Import Path function from pathlib
from pathlib import Path
#Import csv module
import csv

def net_profit():
    """
    This function processes the Profit and Loss data 
    from the CSV file 'Profit_and_Loss.csv' and identifies profit deficits.
    By comparing the net profit of the current day with the previous day,
    it calculates the profit deficits for each day.
    No Parameters required
    """
    #setup filepath for reading the "Profit_and_Loss.csv" file 
    net_profit_fp_read= Path.cwd()/"csv_folder"/"Profit_and_Loss.csv"
    #setup filepath for writing results to a text file, "Summary_report.txt)
    fp_write = Path.cwd()/"Summary_report.txt"

    #Creates the output text file at the specified path and filename if it doesn't already exist
    fp_write.touch()

    #Create an empty list to store net_profit data
    net_profit_list=[]

    #opens the "Profit_and_loss.csv file" for reading
    with net_profit_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        #create a CSV reader object to read the contents of the file
        reader=csv.reader(file)
        #Skip the header row of the CSV file
        next(reader)

        #using for loop to loop through each row in the CSV file
        for row in reader:
            #Extract the day and net proft data from the CSV file and covert 
            #them to integers
            day= int(row[0])
            net_profit= int(row[4])

            #Add day and net_proit to the net_profit_list
            net_profit_list.append([day, net_profit])

    #create an empty list to store profit deficit data
    profit_deficit_list =[]

    # Initialize the variable 'previous_day_profit' 
    #to keep track of the net profit of the previous day
    previous_day_profit = 0

    # Use for loop to Iterate through the list of net profit data for each day and net profit amount
    for day, net_profit_amount in net_profit_list:
        #using the if condition to only execute the code when the net profit of the current day
        #is less than the previous day to calculate the profit deficit
        if net_profit_amount < previous_day_profit:
            profit_deficit = previous_day_profit - net_profit_amount
            #Add the results into the profit_deficit_list
            profit_deficit_list.append(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD {profit_deficit}")

        #update the 'previous_day_profit' with the current day's net profit for the 
        #the next iteration
        previous_day_profit = net_profit_amount

    #Use for loop to iterate through the profit_deficit_list and print the profit deficit
    for deficit in profit_deficit_list:
        print(deficit)

    # Open the output text file in append mode to write profit deficits
    with fp_write.open(mode="a", encoding="UTF*",newline="") as file:
        # Iterate through the list of profit deficits and write each deficit to the file
        for deficit in profit_deficit_list:
            file.write(deficit+"\n")





