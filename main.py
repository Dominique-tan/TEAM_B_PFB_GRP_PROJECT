# Import the required modules from the Python standard library and your custom modules
from pathlib import Path

# Import cash_on_hand function 
# Import overheads function 
# Import profit_loss function 
import cash_on_hand,overheads,profit_loss


# Define the main function that will be executed
def main():
    # Call the function from the 'overheads' module to calculate and calculate highest overhead cost
    overheads.overheads_function()

    # Call the function from the 'cash_on_hand' module to calculate and calculate cash on hand deficit
    cash_on_hand.cash_on_hand_function()

    # Call the function from the 'profit_loss' module to calculate the profit deficit 
    profit_loss.net_profit()

# Call the main function to start the program
main()
