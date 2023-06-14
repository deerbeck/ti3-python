from matplotlib import pyplot as plt
import ass05_rooms as rooms
import ass05_customer as customer
import ass05_roommanagement as roommanagement

def plot_rooms(RM: roommanagement.Roommanagement):
    all_rooms = RM.rooms()

    #get number of closets in roomamangement
    closets = len(list(filter(lambda x: type(x) == rooms.Abstellraum, all_rooms)))

    #get number of meeting rooms in roommanagement
    meetings = len(list(filter(lambda x: type(x) == rooms.Meetingraum, all_rooms)))
    
    #get number of classrooms in roomamangement
    classrooms = len(list(filter(lambda x: type(x) == rooms.Vorlesungsraum, all_rooms)))

    #safe aquired numbers in list for better changeability
    num_rooms = [closets, meetings, classrooms]
    room_names = ["Abstellräume", "Meetingsräume", "Vorlesungsräume"]

    #plot all rooms using pyplot
    plt.figure("Vorhandene Räume")
    plt.bar(room_names, num_rooms)
    plt.ylabel("Anzahl")
    plt.show(block=False)

def plot_availability(RM: roommanagement.Roommanagement):
    all_rooms = RM.rooms()

    #get number of available and booked rooms
    available = len(list(filter(lambda x: x.availability == "verfügbar", all_rooms)))
    booked = len(list(filter(lambda x: x.availability == "gebucht", all_rooms)))

    #safe acquired numbers for bester changeability
    status = [available, booked]
    labels = ["Verfügbar", "Gebucht"]
    
    #plot availability in a pie chart
    plt.figure("Verfügbarkeit")
    plt.pie(status, labels=labels, autopct='%1.1f%%')
    plt.show()

if __name__ == "__main__":
    RM = roommanagement.Roommanagement()

    RM.new_customer("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    RM.new_customer("Franz Huber", "Franz.Huber@hm.edu")
    RM.new_customer("Sebastian Ringlstetter", "Sebastian.Ringlstetter@hm.edu")
    
    print(RM.get_customers())
    RM = roommanagement.Roommanagement()
    meeting_1 = RM.new_meetingroom("R0.001", 20)
    closet_1 = RM.new_closet("R0.002", 10, 20)
    classroom_1 = RM.new_classroom("R0.003", 10, "Tafel")
    classroom_2 = RM.new_classroom("R0.004", 20, "Projektor")

    customer_1 = customer.Kunde("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    customer_2 = customer.Kunde("Franz Huber", "Franz.Huber@hm.edu")

    RM.book_room("R0.001", customer_1)
    RM.book_room("R0.001", customer_1)
    RM.book_room("R0.002", customer_2)
    RM.book_room("R0.003", customer_1)

    #plot_rooms(RM)
    plot_availability(RM)
    # print(RM)
    pass