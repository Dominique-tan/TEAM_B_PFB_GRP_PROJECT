from pathlib import Path
import csv

def overheads_function():
    """
    - processes data from overheads.csv file to find highest overhead where results are written in Summary_report file
    - no parameters required
    -
    """

    # using the path module, set the file paths for the input and output files
    overheads_fp_read= Path.cwd()/"csv_folder"/"overheads.csv"
    fp_write= Path.cwd()/"Summary_report.txt"
    
     # create empty file to store summary report
    fp_write.touch()

    # create empty list to store data from csv file
    overheads_list=[]

    # open csv file to read data 
    with overheads_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        # create csv reader object to read file content as rows
        reader=csv.reader(file)
        #skip the header in reader
        next(reader)

        # use for loop to run each row of the file
        for row in reader:
            #extract values from first column of the row
            category= row[0]
            # convert values from second column of file to float
            overhead=float(row[1])
            # add category and overhead as a list to the main list
            overheads_list.append([category,overhead])

    # create empty list to store values for highest overhead
    highest_overhead_category=[]
    # set initial value of the percentage of overhead to be 0
    highest_overhead_percentage=0.00 

    # using for loop, run each item in the list
    for category, overhead in overheads_list:
        # compare overhead value to current overhead percentage value and determine if overhead value is higher than the current
        if overhead>highest_overhead_percentage:
            # update highest value is overhead is higher
            highest_overhead_percentage= overhead
            # store category with the new highest overhead value
            highest_overhead_category= category 

    # create result string showing the category with the highest overhead percentage
    highest_overhead_result=f"[HIGHEST OVERHEAD] Category:{highest_overhead_category}"
    # print the function
    print(highest_overhead_result)

    # write the highest overhead result to 'Summary_report.txt' file and open in append mode
    with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
        # write the result string and add a new line 
        file.write(highest_overhead_result + "\n")




