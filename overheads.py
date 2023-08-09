#Import Path Function from pathlib
from pathlib import Path
#Import CSV module
import csv

# create function
def overheads_function():
    """
    -This function processes data from 'overheads.csv' file to find highestthe overhead
    -No parameters is required
    """

    #setup filepath for reading the "Profit_and_Loss.csv" file 
    overheads_fp_read= Path.cwd()/"csv_folder"/"overheads.csv"
    #setup filepath for writing results to a text file, "Summary_report.txt)
    fp_write= Path.cwd()/"Summary_report.txt"
    
    #Creates the output text file at the specified path and filename if it doesn't already exist
    fp_write.touch()

    # create empty list to store overheads data
    overheads_list=[]

    # open the "overheads.csv" file to read data 
    with overheads_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # create csv reader object to read file content as rows
        reader=csv.reader(file)
        #skip the header roe of the CSV file
        next(reader)

        # use for loop to iterate through each row in the csv fie
        for row in reader:
            #Extraxt the category from the CSV file
            category= row[0]
            #Extract the Overheads percentage from the CSV file and convert them to float
            overhead=float(row[1])
            # add category and overhead to the overheads_list
            overheads_list.append([category,overhead])

    # create empty list to store values for highest overhead
    highest_overhead_category=[]
    # set initial value of the percentage of overhead to be 0
    highest_overhead_percentage=0.00 

    # Iterate through the list of overheads to identify the category with the highest overhead percentage
    for category, overhead in overheads_list:
        # compare overhead value to current overhead percentage value and determine if the overhead value is higher than the current
        if overhead>highest_overhead_percentage:
            # update highest value if the current overhead is greater
            highest_overhead_percentage= overhead
            # store the category with the new highest overhead value
            highest_overhead_category= category 

    # create result string showing the category with the highest overhead percentage
    highest_overhead_result=f"[HIGHEST OVERHEAD] Category:{highest_overhead_category}"
    # print the function
    print(highest_overhead_result)

    # write the highest overhead result to 'Summary_report.txt' file and open in append mode
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        # write the result string and add a new line 
        file.write(highest_overhead_result + "\n")




