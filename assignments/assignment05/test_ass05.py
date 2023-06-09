import pytest

import glob
from radon.raw import analyze
import sys, os
import subprocess

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
    assert ncomments / nloc >= 0.25


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
    assert RM.remove_room(closet_1)


if __name__ == "__main__":
    test_codequality()
    test_commit_messages()

    test_customer()
    test_rooms()
    test_roommanagement_adding_removing()