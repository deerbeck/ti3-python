# Projekt Raumverwaltungssystem

from abc import ABC, abstractmethod


class Raum(ABC):
    """Abstrakte Klasse mit verpflichtenden Attributen & Methoden."""
    # initialize abstract room object with needed information
    @abstractmethod
    def __init__(self, room_number: str, capacity: int) -> None:

        self.room_number = room_number
        self.capacity = capacity
        self.availability = "verfügbar"
        self.customer = None

    # setter/gettter room_number
    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number: str):
        self.__room_number = room_number

    # setter/gettter capacity
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    # setter/gettter availability
    @property
    def availability(self):
        return self.__availability

    @availability.setter
    def availability(self, availability: str):
        self.__availability = availability

    # setter/getter customer
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer


    # return room properties
    def __str__(self):
        room_properties = f"Raumnummer: {self.__room_number}\n"
        room_properties += f"Raumtyp: {type(self).__name__}\n"
        room_properties += f"Kapazität: {self.__capacity}\n"
        room_properties += f"Verfügbarkeit: {self.__availability}\n"
        if self.__availability == "gebucht":
            room_properties += f"   --> Gebucht von: {self.__customer.name}\n"

        return room_properties


class Abstellraum(Raum):
    """Abstellraum mit dem zusätzlichen Attribut der Fläche."""
    #subclass to "Raum"
    def __init__(self, room_number: str, capacity: int, area: int) -> None:
        super().__init__(room_number, capacity)
        self.area = area

    # setter/getter area
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: int):
        self.__area = area

    #return room properties
    def __str__(self):
        room_properties = f"Fläche: {self.__area}\n"
        return super().__str__() + room_properties

class Vorlesungsraum(Raum):
    """Vorlesungsraum mit dem zusätzlichen Attribut des Präsentationsmediums"""
    #subclass to "Raum"
    def __init__(self, room_number: str, capacity: int, presentation_medium: str) -> None:
        super().__init__(room_number, capacity)
        self.presentation_medium = presentation_medium

    # setter/getter presentation_medium
    @property
    def presentation_medium(self):
        return self.__presentation_medium

    @presentation_medium.setter
    def presentation_medium(self, presentation_medium: str):
        self.__presentation_medium = presentation_medium

    #return room properties
    def __str__(self):
        room_properties = f"Präsentationsmedium: {self.__presentation_medium}\n"
        return super().__str__() + room_properties


class Meetingraum(Raum):
    """Meetingraum nur mit den default-Attributen."""
    #subclass to "Raum"
    def __init__(self, room_number: str, capacity: int) -> None:
        super().__init__(room_number, capacity)


if __name__ == "__main__":
    meeting_1 = Meetingraum("R0.001", 20)
    closet_1 = Abstellraum("R0.002",10, 20)
    classroom_1 = Vorlesungsraum("R0.003", 10, "Tafel")
    print(meeting_1)
    print(closet_1)
    print(classroom_1)
    test = 0