class Parking_garage ():
    
    def __init__(self):
        self.tickets = ['001', '002', '003', '004', '005', '006', '007','008','009']
        self.parkingSpaces = ['101', '102', '103', '104', '105','106','107','108','109'] 
        self.takenTickets = []
        self.takenSpaces = []
        self.currentTicket = {}

    def takeTicket (self):
        if len(self.tickets) > 0 and len(self.parkingSpaces) > 0:
            ticket_num1 = self.tickets.pop(0)
            parking_space_num1 = self.parkingSpaces.pop(0)
            self.takenTickets.append(ticket_num1)
            self.takenSpaces.append(parking_space_num1)
            self.currentTicket = {
                'Ticket Number' : ticket_num1,
                'Parking Space' : parking_space_num1
             }
            print(f'Your ticket number is {ticket_num1}. Please park in space {parking_space_num1}.')
        else:
            print('Sorry, the parking garage is full.')

    def payForParking (self):
        if not self.currentTicket:
            print('The Parking Garage is currently empty.')
        else:     
            amount1 = input('Please pay for your ticket: ')   
            if not amount1:                                     
                print('Payment not recieved, please make a payment.')
            else:
                self.currentTicket["paid"] = True                        
                print('Payment approved. You have 15 minutes to leave.')

    def leaveGarage (self):
        if not self.currentTicket:
            print("The Parking Garage is currently empty.")
        elif 'paid' in self.currentTicket:
            print("Thank you, have a nice day!")                                             
            del self.currentTicket['paid']
            ticket_num2 = self.takenTickets.pop(0)
            parking_space_num2 = self.takenSpaces.pop(0)
            self.tickets.insert(0, ticket_num2)
            self.parkingSpaces.insert(0, parking_space_num2)
        else:
            amount2 = input('No payment recieved, you must make a payment before leaving: ')
            if not amount2:
                print('Payment is required. Please try again.')
            else:
                print('Thank you, have a nice day!')                                             
                ticket_num2 = self.takenTickets.pop()
                parking_space_num2 = self.takenSpaces.pop()
                self.tickets.insert(0, ticket_num2)
                self.parkingSpaces.insert(0, parking_space_num2)

lot = Parking_garage()

def run_parking_garage():
    print('\nWELCOME TO PARKING GARAGE')
    while True:
        response = input('\nWhat would you like to do? (Park/Pay/Leave/Quit): ')
        if response.lower() == 'park':
            lot.takeTicket()
            continue
        elif response.lower() == 'pay':
            lot.payForParking()
            continue
        elif response.lower() == 'leave':
            lot.leaveGarage()
            continue
        elif response.lower() == 'quit':
            break
        else:
            print('That is not a valid response.')
            continue

run_parking_garage()