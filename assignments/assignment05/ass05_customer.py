import ass05_rooms as rooms
import ass05_roommanagement as roommanagement

class Kunde():

    def __init__(self, name :str, mail_address :str) -> None:
        #initialize name and mail address
        self.name = name
        self.mail_address = mail_address

    #getter for customer name
    @property
    def name(self):
        return self.__name
    #setter for customer name
    @name.setter
    def name(self, name):
        self.__name = name
    

    #getter for customer mail_address
    @property
    def mail_address(self):
        return self.__mail_address
    #setter for customer mail_address
    @mail_address.setter
    def mail_address(self, mail_address):
        self.__mail_address = mail_address

    #return properties of customer
    def __str__(self) -> str:
        #use string buffer to print out later
        print_buffer = f"Kundenname: {self.__name}\n"
        print_buffer += f"Kundenkontakt: {self.__mail_address}\n"
        return print_buffer

if __name__ == "__main__":
    # customer_1 = Kunde("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    # customer_2 = Kunde("Franz Huber", "Franz.Huber@hm.edu")

    # print(customer_1)
    # print(customer_2)

    pass