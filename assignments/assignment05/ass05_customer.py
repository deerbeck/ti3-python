import ass05_rooms as rooms
import ass05_roommanagement as roommanagement

class Kunde():

    def __init__(self, name, mail_address) -> None:
        self.name = name
        self.mail_address = mail_address

    ##setter/getter for customer name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    

    ##setter/getter for customer mail_address
    @property
    def mail_address(self):
        return self.__mail_address

    @mail_address.setter
    def mail_address(self, mail_address):
        self.__mail_address = mail_address
