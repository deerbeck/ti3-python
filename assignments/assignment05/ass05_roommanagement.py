# Projekt Raumverwaltungssystem

from abc import ABC, abstractmethod
import ass05_rooms as rooms
import ass05_customer as customer


class Roommanagement():
    """Raumverwaltungsobjekt um Räume einzusehen, hinzuzufügen sowie zu entfernen."""

    def __init__(self) -> None:
        #initialize with empty rooms list to later add new rooms to
        self.__rooms = []

    # create new closet
    def new_closet(self, room_number: str, capacity: int, area: int) -> rooms.Abstellraum:
        for room in self.__rooms:
            if room.room_number == room_number:
                #case when room_number is already taken
                print(f"Raum konnte nicht hinzugefügt werden --> Raumnummer {room_number} bereits vergeben.")
                return -1
        #append room to roomslist of roommanagement
        self.__rooms.append(closet := rooms.Abstellraum(
            room_number, capacity, area))
        #return room object
        return closet

    # create new classroom
    def new_classroom(self, room_number: str, capacity: int, presentation_medium: int) -> rooms.Vorlesungsraum:
        for room in self.__rooms:
            if room.room_number == room_number:
                #case when room_number is already taken
                print(f"Raum konnte nicht hinzugefügt werden --> Raumnummer {room_number} bereits vergeben.")
                return -1
        #append room to roomslist of roommanagement
        self.__rooms.append(classroom := rooms.Vorlesungsraum(
            room_number, capacity, presentation_medium))
        #return room object
        return classroom

    # create new meetingroom
    def new_meetingroom(self, room_number: str, capacity: int) -> rooms.Meetingraum:
        for room in self.__rooms:
            if room.room_number == room_number:
                #case when room_number is already taken
                print(f"Raum konnte nicht hinzugefügt werden --> Raumnummer {room_number} bereits vergeben.")
                return -1
        #append room to roomslist of roommanagement
        self.__rooms.append(
            meetingroom := rooms.Meetingraum(room_number, capacity))
        #return room object
        return meetingroom

    # add external created room-object to Roommanagement
    def add_room(self, room):
        self.__rooms.append(room)

    # remove room from Roommanagement
    def remove_room(self, room_number):
        # can either enter "room_number" or room object that should be removed
        # "room_number" can be object of a room as well
        if type(room_number) != str:
            for room in self.__rooms:
                if room == room_number:
                    ##remove room from list and print out to terminal for better track keeping
                    print(f"Raum {room.room_number} wurde entfernt.")
                    self.__rooms.remove(room)
                    return 1
        else:
            for room in self.__rooms:
                if room.room_number == room_number:
                    ##remove room from list and print out to terminal for better track keeping
                    print(f"Raum {room.room_number} wurde entfernt.")
                    self.__rooms.remove(room)
                    return 1
        #return -1 if room does not exist
        print("Raum nicht vorhanden.")
        return -1

    # book room in Roommanagement
    def book_room(self, room_number, customer):
        # can either enter "room_number" or room object that should be booked
        # "room_number" can be object of a room as well
        if type(room_number) != str:
            # check if room is already booked
            if room_number.availability == "gebucht":
                print(f"Raum {room_number.room_number} bereits belegt.")
                return -1
            
            # book room otherwise
            room_number.availability = "gebucht"
            #set room property customer to provided customer
            room_number.customer = customer
            print(f"Raum {room_number.room_number} erfolgreich von {customer.name} gebucht.")
            return 1

        else:
            for room in self.__rooms:
                if room.room_number == room_number:
                    # check if room is already booked
                    if room.availability == "gebucht":
                        print(f"Raum {room.room_number} bereits belegt.")
                        return -1
                    
                    # book room otherwise
                    room.availability = "gebucht"
                    #set room property customer to provided customer
                    room.customer = customer
                    print(f"Raum {room.room_number} erfolgreich von {customer.name} gebucht.")
                    return 1
        #return -1 if room is not available
        print("Raum nicht vorhanden.")
        return -1

    # unbook room in Roommanagement
    def unbook_room(self, room_number):
        # can either enter "room_number" or room object that should be booked
        # "room_number" can be object of a room as well
        if type(room_number) != str:
            #change room availability
            room_number.availability = "verfügbar"
            #resset booked room by customer to None
            room_number.customer = None
            #terminal printout for easier track keeping
            print(f"Raum {room_number.room_number} ist jetzt frei.")
            return 1
        else:
            for room in self.__rooms:
                if room.room_number == room_number:
                    #change room availability
                    room.availability = "verfügbar"
                    #resset booked room by customer to None
                    room.customer = None
                    #terminal printout for easier track keeping
                    print(f"Raum {room.room_number} ist jetzt frei.")
                    return 1
        #return -1 if room is not available
        print("Raum nicht vorhanden.")
        return -1

    # return all managed rooms and the respective properties

    def __str__(self) -> str:
        ##preparing printout of contained rooms
        closets = "Abstellräume: \n-------------\n"
        classrooms = "Vorlesungsräume: \n-------------\n"
        meetings = "Meetingräume: \n-------------\n"
        
        #use string manipulation to only print out existing rooms (printflag)
        closets_available = 0
        classroomes_available = 0
        meetings_available = 0

        #loop through each room type and add it to bufferstring
        for rooms in self.__rooms:
            if type(rooms).__name__ == "Abstellraum":
                closets += str(rooms) + "\n"
                #printflag
                closets_available = 1

            elif type(rooms).__name__ == "Vorlesungsraum":
                classrooms += str(rooms) + "\n"                
                #printflag
                classroomes_available = 1

            elif type(rooms).__name__ == "Meetingraum":
                meetings += str(rooms) + "\n"
                #printflag
                meetings_available = 1
        #concatenate all strings and print them out
        return classrooms * classroomes_available + meetings * meetings_available + closets * closets_available


if __name__ == "__main__":
    # RM = Roommanagement()
    # meeting_1 = RM.new_meetingroom("R0.001", 20)
    # closet_1 = RM.new_closet("R0.002", 10, 20)
    # classroom_1 = RM.new_classroom("R0.003", 10, "Tafel")
    # classroom_2 = RM.new_classroom("R0.004", 20, "Projektor")

    # customer_1 = customer.Kunde("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    # customer_2 = customer.Kunde("Franz Huber", "Franz.Huber@hm.edu")

    # RM.book_room("R0.001", customer_1)
    # RM.book_room("R0.001", customer_1)
    # RM.book_room("R0.002", customer_2)
    # RM.book_room("R0.003", customer_1)

    # print(RM)
    pass
