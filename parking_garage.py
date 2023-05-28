class Parking_garage ():
    
    def __init__(self, number_of_tickets, number_of_parking_space):
        self.tickets = []            
        self.parkingSpaces = []      
        self.currentTicket = {}

    def takeTicket (self):
        pass
        # This should decrease the amount of tickets available by 1
        # This should decrease the amount of parkingSpaces available by 1

    def payForParking (self):
        pass
        # Display an input that waits for an amount from the user and store it in a variable
        # If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
        # This should update the "currentTicket" dictionary key "paid" to True

    def leaveGarage (self):
        pass
        # If the ticket has been paid, display a message of "Thank You, have a nice day"
        # If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        # Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        # Update tickets list to increase by 1 (meaning add to the tickets list)

lot = Parking_garage(number_of_tickets = 10, number_of_parking_space = 10) #This calls the code from the class, for simplicity sake, the lot size is set to 10 spaces. Can increase number later.

# This will run the program by using the lot to call the class functions
def run_parking_garage():
    print("\nWELCOME TO PARKING GARAGE")
    while True:
        response = input("\nWhat would you like to do? (Park/Pay/Leave/Quit): ")
        if response.lower() == 'park':
            pass
        elif response.lower() == 'pay':
            pass
        elif response.lower() == 'leave':
            pass
        elif response.lower() == 'quit':
            break
        else:
            print("That is not a valid response.")
            pass

run_parking_garage()