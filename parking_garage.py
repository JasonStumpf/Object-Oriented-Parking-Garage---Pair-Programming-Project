class Parking_garage ():
    tickets = []            
    parkingSpaces = []      # These are constant attributes
    currentTicket = {}

    def __init__(self):
        pass
        # Put necessary variables here

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
