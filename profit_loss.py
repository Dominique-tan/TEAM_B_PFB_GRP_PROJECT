from pathlib import Path
import csv

def net_profit():
    net_profit_fp_read= Path.cwd()/r"C:\TEAM_B_PFB_GRP_PROJECT\csv_folder\Profit_and_Loss.csv"
    net_profit_list=[]

    with net_profit_fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            day= int(row[0])
            net_profit= int(row[4])
            net_profit_list.append([day, net_profit])

    profit_deficit_list =[]

    previous_day_profit = 0

    for day, net_profit_amount in net_profit_list:
        if net_profit_amount < previous_day_profit:
            profit_deficit = previous_day_profit - net_profit_amount
            profit_deficit_list.append(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD {profit_deficit}")
        previous_day_profit = net_profit_amount

    for deficit in profit_deficit_list:
        print(deficit)

net_profit()



