import pytest

import glob
from radon.raw import analyze
import sys, os
import subprocess
import filecmp
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def get_commit_count_exclude_user(folder_path, username):

    cmd = ["git", "log", "--format='%H %an'", "--", folder_path]
    
    output = subprocess.check_output(cmd).decode('utf-8')
    commits = output.split('\n')
    flohr_commits = [username in el for el in commits]
    return len(commits) - sum(flohr_commits) -1

def test_codequality():
    ncomments = 0
    nloc = 0
    files_grabbed = glob.glob("./*.py")
    for filename in files_grabbed:
        with open(filename) as fobj:
            source = fobj.read()
            report =  analyze(source)
            ncomments+=report.comments
            nloc+=report.loc
            nloc -= report.multi
            nloc -= report.blank

    assert nloc != 0
    print("#comments:",ncomments,"#loc:",nloc, "#comments/#loc:", ncomments / nloc)
    assert ncomments / nloc >= 0.1


def test_commit_messages():
    count = get_commit_count_exclude_user("./", "Fabian Flohr")
    assert int(count)>=5

def test_rooms():
    import ass05_rooms
    print("Test zu den Raumklassen")
    meeting_1 = ass05_rooms.Meetingraum("R0.001", 20)
    closet_1 = ass05_rooms.Abstellraum("R0.002",10, 20)
    classroom_1 = ass05_rooms.Vorlesungsraum("R0.003", 10, "Tafel")

    assert str(meeting_1.room_number) == "R0.001"
    assert str(closet_1.room_number) == "R0.002"
    assert str(classroom_1.room_number) == "R0.003"

    assert str(meeting_1) == "Raumnummer: R0.001\nRaumtyp: Meetingraum\nKapazität: 20\nVerfügbarkeit: verfügbar\n"
    assert str(closet_1) == "Raumnummer: R0.002\nRaumtyp: Abstellraum\nKapazität: 10\nVerfügbarkeit: verfügbar\nFläche: 20\n"
    assert str(classroom_1) == "Raumnummer: R0.003\nRaumtyp: Vorlesungsraum\nKapazität: 10\nVerfügbarkeit: verfügbar\nPräsentationsmedium: Tafel\n"


def test_customer():
    import ass05_customer
    print("Test zur Kundenklasse")

    customer_1 = ass05_customer.Kunde("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    customer_2 = ass05_customer.Kunde("Franz Huber", "Franz.Huber@hm.edu")

    assert str(customer_1) == 'Kundenname: Johannes Hirschbeck\nKundenkontakt: Johannes.Hirschbeck@hm.edu\n'
    assert str(customer_2) == 'Kundenname: Franz Huber\nKundenkontakt: Franz.Huber@hm.edu\n'


def test_roommanagement_adding_removing():
    import ass05_roommanagement
    import ass05_rooms
    import ass05_customer
    print("Teste hinzufügen/entfernen von Räumen im Raummanagement")
    RM = ass05_roommanagement.Roommanagement()
    meeting_1 = RM.new_meetingroom("R0.001", 20)
    closet_1 = RM.new_closet("R0.002", 10, 20)
    classroom_1 = RM.new_classroom("R0.003", 10, "Tafel")
    classroom_2 = RM.new_classroom("R0.004", 20, "Projektor")
    
    assert isinstance(classroom_1, ass05_rooms.Vorlesungsraum)
    assert isinstance(classroom_2, ass05_rooms.Vorlesungsraum)
    assert isinstance(closet_1, ass05_rooms.Abstellraum)
    assert isinstance(meeting_1, ass05_rooms.Meetingraum)

    classroom_3 = RM.new_classroom("R0.003", 15, "Projektor")
    closet_2 = RM.new_closet("R0.002", 10, 20)    
    meeting_2 = RM.new_meetingroom("R0.001", 20)

    assert classroom_3 == -1
    assert closet_2 == -1
    assert meeting_2 == -1

    assert RM.remove_room("R0.001") == 1
    assert RM.remove_room(meeting_1) == -1
    assert RM.remove_room(closet_1) == 1

def test_roommanagement_booking():
    import ass05_roommanagement
    import ass05_rooms
    import ass05_customer
    print("Teste buchen/freigeben von Räumen im Raummanagement")
    RM = ass05_roommanagement.Roommanagement()
    meeting_1 = RM.new_meetingroom("R0.001", 20)
    closet_1 = RM.new_closet("R0.002", 10, 20)
    classroom_1 = RM.new_classroom("R0.003", 10, "Tafel")
    classroom_2 = RM.new_classroom("R0.004", 20, "Projektor")

    customer_1 = ass05_customer.Kunde("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    customer_2 = ass05_customer.Kunde("Franz Huber", "Franz.Huber@hm.edu")

    assert RM.book_room("R0.001", customer_1) == 1
    assert RM.book_room("R0.001", customer_1) == -1
    assert RM.book_room("R0.002", customer_2) == 1
    assert RM.book_room(classroom_1, customer_1) == 1

    assert str(RM) == 'Vorlesungsräume: \n-------------\nRaumnummer: R0.003\nRaumtyp: Vorlesungsraum\nKapazität: 10\nVerfügbarkeit: gebucht\n   --> Gebucht von: Johannes Hirschbeck\nPräsentationsmedium: Tafel\n\nRaumnummer: R0.004\nRaumtyp: Vorlesungsraum\nKapazität: 20\nVerfügbarkeit: verfügbar\nPräsentationsmedium: Projektor\n\nMeetingräume: \n-------------\nRaumnummer: R0.001\nRaumtyp: Meetingraum\nKapazität: 20\nVerfügbarkeit: gebucht\n   --> Gebucht von: Johannes Hirschbeck\n\nAbstellräume: \n-------------\nRaumnummer: R0.002\nRaumtyp: Abstellraum\nKapazität: 10\nVerfügbarkeit: gebucht\n   --> Gebucht von: Franz Huber\nFläche: 20\n\n'

    assert RM.unbook_room("R0.001") == 1
    assert RM.unbook_room("R1.000") == -1
    assert RM.unbook_room("R0.002") == 1
    assert RM.unbook_room("R0.003") == 1
    
def test_roommanagement_customers():
    import ass05_roommanagement
    import ass05_rooms
    import ass05_customer

    RM = ass05_roommanagement.Roommanagement()

    RM.new_customer("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    RM.new_customer("Franz Huber", "Franz.Huber@hm.edu")
    RM.new_customer("Sebastian Ringlstetter", "Sebastian.Ringlstetter@hm.edu")

    assert str(RM.get_customers()) == 'Kundenname: Johannes Hirschbeck\nKundenkontakt: Johannes.Hirschbeck@hm.edu\n\nKundenname: Franz Huber\nKundenkontakt: Franz.Huber@hm.edu\n\nKundenname: Sebastian Ringlstetter\nKundenkontakt: Sebastian.Ringlstetter@hm.edu\n\n'
    pass


def test_json_safe():
    import ass05_roommanagement
    import ass05_rooms
    import ass05_customer
    import ass05_json_handling

    RM1 = ass05_roommanagement.Roommanagement()
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
    
    data_file = "test_json_handling_data.json"
    handle_file = "test_json_handling_handle.json"
    ass05_json_handling.safe_as_json(RM1, handle_file)

    assert filecmp.cmp(data_file, handle_file)

def test_json_load():
    import ass05_roommanagement
    import ass05_rooms
    import ass05_customer
    import ass05_json_handling


    RM1 = ass05_roommanagement.Roommanagement()
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

    RM = ass05_roommanagement.Roommanagement()
    
    data_file = "test_json_handling_data.json"

    ass05_json_handling.load_from_json(RM, data_file)

    jsondata = json.dumps(RM1, default=lambda x: x.__dict__, indent = 4)
    jsonhandle = json.dumps(RM, default=lambda x: x.__dict__, indent = 4)

    assert jsondata == jsonhandle




if __name__ == "__main__":
    test_codequality()
    test_commit_messages()

    test_customer()
    test_rooms()
    test_roommanagement_adding_removing()
    test_roommanagement_booking()
    test_roommanagement_customers()
    test_json_load()
    test_json_safe()