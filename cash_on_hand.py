from pathlib import Path
import csv

def cash_on_hand_function():
    cash_on_hand_fp_read= Path.cwd()/"csv_folder"/"Cash_on_Hand.csv"
    fp_write= Path.cwd()/"Summary_report.txt"
    fp_write.touch

    cash_on_hand_list=[]

    with cash_on_hand_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader=csv.reader(file)
        next(reader)
         
        for row in reader:
            cash_on_hand_list.append(row)
    # print(cash_on_hand_list)
    
    cash_on_hand_difference=[]

    for cash in range(1,len(cash_on_hand_list)):
        current_day=int(cash_on_hand_list[cash][1])
        previous_day=int(cash_on_hand_list[cash-1][1])

        difference= current_day-previous_day

        if difference<0:
            cash_on_hand_difference.append(f"[Cash deficit] Day: {cash_on_hand_list[cash][0]}, Amount:USD{abs(difference)}")

    with fp_write.open(mode="w",encoding="UTF-8",newline="") as file:
        for cash_deficit in cash_on_hand_difference:
            print(cash_deficit)
            file.write(cash_deficit+"\n")


cash_on_hand_function()
