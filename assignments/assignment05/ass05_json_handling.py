from ass05_rooms import *
from ass05_roommanagement import *
from ass05_customer import *

import json

def safe_as_json(RM: Roommanagement, filename: str):
    #json conversion of data
    try:
        data = json.dumps(RM, default=lambda x: x.__dict__, indent = 4)
        with open(filename, 'w', encoding="utf-8") as json_file:
            json_file.write(data)
            return 1
    except:
        return -1
    
def load_from_json(RM: Roommanagement, filename:str):
    try:
        with open(filename, "r", encoding = "utf-8") as json_file:
            raw_RM = json.loads(json_file.read())

            for raw_customer in raw_RM["_Roommanagement__customers"]:
            
                    customer_name = raw_customer["_Kunde__name"]
                    customer_mail = raw_customer["_Kunde__mail_address"]
                
                    RM.new_customer(customer_name, customer_mail)

            for raw_room in raw_RM["_Roommanagement__rooms"]:
                room_number = raw_room["_Raum__room_number"]
                capacity = raw_room["_Raum__capacity"]
                
                if raw_room['_Raum__room_type'] == "Vorlesungsraum":
                    presentation_medium = raw_room["_Vorlesungsraum__presentation_medium"]
                    new_room = RM.new_classroom(room_number, capacity, presentation_medium)
                
                elif raw_room['_Raum__room_type'] == "Abstellraum":
                    area = raw_room["_Abstellraum__area"]
                    new_room = RM.new_closet(room_number, capacity, area)
                
                elif raw_room['_Raum__room_type'] == "Meetingraum":
                    new_room = RM.new_meetingroom(room_number, capacity)

                if raw_room["_Raum__availability"] == "gebucht":
                    name = raw_room["_Raum__customer"]["_Kunde__name"]
                    RM.book_room(new_room, name)
            return RM
    except:
        return -1
    
if __name__ == "__main__":
    #manual json testing
    RM1 = Roommanagement()
    meeting_1 = RM1.new_meetingroom("R0.001", 20)
    closet_1 = RM1.new_closet("R0.002", 10, 20)
    classroom_1 = RM1.new_classroom("R0.003", 10, "Tafel")
    classroom_2 = RM1.new_classroom("R0.004", 20, "Projektor")


        
    RM1.new_customer("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    RM1.new_customer("Franz Huber", "Franz.Huber@hm.edu")

    RM1.book_room("R0.001", "Johannes Hirschbeck") 
    RM1.book_room("R0.004", "Johannes Hirschbeck") 
    RM1.book_room("R0.002", "Franz Huber") 

    RM1.book_room("R0.003", "Johannes Hirschbec")
    RM1.book_room("R0.004", "Johannes Hirschbec")

    data = json.dumps(RM1, default=lambda x: x.__dict__, indent = 4)
    with open('roommanagement.json', 'w', encoding="utf-8") as json_file:
        json_file.write(data)

    with open('roommanagement.json', "r", encoding = "utf-8") as json_file:
            raw_RM = json.loads(json_file.read())
            RM = Roommanagement()
            for raw_customer in raw_RM["_Roommanagement__customers"]:
            
                    customer_name = raw_customer["_Kunde__name"]
                    customer_mail = raw_customer["_Kunde__mail_address"]
                
                    RM.new_customer(customer_name, customer_mail)

            for raw_room in raw_RM["_Roommanagement__rooms"]:
                room_number = raw_room["_Raum__room_number"]
                capacity = raw_room["_Raum__capacity"]
                
                if raw_room['_Raum__room_type'] == "Vorlesungsraum":
                    presentation_medium = raw_room["_Vorlesungsraum__presentation_medium"]
                    new_room = RM.new_classroom(room_number, capacity, presentation_medium)
                
                elif raw_room['_Raum__room_type'] == "Abstellraum":
                    area = raw_room["_Abstellraum__area"]
                    new_room = RM.new_closet(room_number, capacity, area)
                
                elif raw_room['_Raum__room_type'] == "Meetingraum":
                    new_room = RM.new_meetingroom(room_number, capacity)

                if raw_room["_Raum__availability"] == "gebucht":
                    name = raw_room["_Raum__customer"]["_Kunde__name"]
                    mail_address =raw_room["_Raum__customer"]["_Kunde__mail_address"]

                    RM.book_room(new_room, name)




    #converting json back to objects in python
    
    print(RM1)
    print("\n\n\nNEUER RAUM\n\n\n")
    print(RM)
    pass