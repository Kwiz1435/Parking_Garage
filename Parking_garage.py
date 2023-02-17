class ParkingGarage:
    def __init__(self, tickets=10, parking_spaces=10):
        self.tickets = [i for i in range(1, tickets+1)]
        self.parking_spaces = [i for i in range(1, parking_spaces+1)]
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parking_spaces.pop(0)
            self.current_ticket[ticket] = {"space": space, "paid": False}
            print(f"Your ticket number is {ticket}. Please park in space {space}.")
        else:
            print("Sorry, the garage is full. Please come back later.")

    def pay_for_parking(self):
        ticket = int(input("Please enter your ticket number: "))
        if ticket in self.current_ticket and not self.current_ticket[ticket]["paid"]:
            payment = input("Please enter your payment amount: ")
            if payment:
                self.current_ticket[ticket]["paid"] = True
                print("Payment received. You have 15 minutes to leave.")
            else:
                print("No payment received.")
        else:
            print("Invalid ticket number or ticket already paid.")

    def leave_garage(self):
        ticket = int(input("Please enter your ticket number: "))
        if ticket in self.current_ticket:
            if self.current_ticket[ticket]["paid"]:
                space = self.current_ticket[ticket]["space"]
                self.parking_spaces.append(space)
                self.tickets.append(ticket)
                del self.current_ticket[ticket]
                print("Thank you, have a nice day!")
            else:
                payment = input("Please pay for your ticket before leaving. Enter payment amount: ")
                if payment:
                    self.current_ticket[ticket]["paid"] = True
                    space = self.current_ticket[ticket]["space"]
                    self.parking_spaces.append(space)
                    self.tickets.append(ticket)
                    del self.current_ticket[ticket]
                    print("Payment received. Thank you, have a nice day!")
                else:
                    print("No payment received.")
        else:
            print("Invalid ticket number.")

# Instantiate a new parking garage
garage = ParkingGarage()

# Simulate cars entering, paying for, and leaving the garage
garage.take_ticket()
garage.pay_for_parking()
garage.leave_garage()
