# Projekt Raumverwaltungssystem

from abc import ABC, abstractmethod


class Raum(ABC):
    # initialize abstract room object with needed information
    def __init__(self, room_number: str, capacity: int) -> None:

        self.room_number = room_number
        self.capacity = capacity
        self.availability = "available"

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

    # return room properties

    def __str__(self):
        room_properties = f"Raumnummer: {self.__room_number}\n"
        room_properties += f"Kapazität: {self.__capacity}\n"
        room_properties += f"Verfügbarkeit: {self.__availability}\n"
        return room_properties


class Abstellraum(Raum):
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

class Vorlesungsraum(Raum):
    def __init__(self, room_number: str, capacity: int, presentation_medium) -> None:
        super().__init__(room_number, capacity)
        self.presentation_medium = presentation_medium

    # setter/getter presentation_medium
    @property
    def presentation_medium(self):
        return self.__presentation_medium

    @presentation_medium.setter
    def area(self, presentation_medium: int):
        self.__presentation_medium = presentation_medium


class Meetingraum(Raum):
    def __init__(self, room_number: str, capacity: int) -> None:
        super().__init__(room_number, capacity)


if __name__ == "__main__":
    meeting_1 = Meetingraum("R0.001", 20)
    room1 = Raum("R0.002", 40)
    test = 0
    