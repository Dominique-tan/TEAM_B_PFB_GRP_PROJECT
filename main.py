

# Import cash_on_hand function, Import overheads function, Import profit_loss function 
import cash_on_hand,overheads,profit_loss

def main():
    """
    This function calls functions from the 'cash_on_hand.py', 'overheads.py' and 'profit_loss.py' modules,
    to calculate cash deficits, highest overheads and profit deficits
    No parameters is required
    """
       
    # Call the function from the 'overheads' module to calculate and identify the highest overhead cost
    overheads.overheads_function()

    # Call the function from the 'cash_on_hand' module to calculate and identify cash deficits
    cash_on_hand.cash_on_hand_function()

    # Call the function from the 'profit_loss' module to calculate and identify the net profit deficit 
    profit_loss.net_profit()

# Call the main function to start the program
main()
