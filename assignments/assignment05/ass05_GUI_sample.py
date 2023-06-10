from ass05_rooms import *
from ass05_roommanagement import *
from ass05_customer import *

import json

##GUI For Room Management
import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkfont

RM = Roommanagement()

def add_room():
    room_number = room_number_entry.get()
    room_type = room_type_combobox.get()
    capacity = capacity_entry.get()
    
    if room_number and room_type and capacity:
        if room_type == "Vorlesungsraum":
            presentation_medium = presentation_medium_entry.get()
            
            if presentation_medium:
                if RM.new_classroom(room_number,capacity, presentation_medium) == -1:
                    messagebox.showwarning("Warnung", f"Raumnummer {room_number} bereits vergeben.")
                else:
                    messagebox.showinfo("Erfolgreich", "Raum erfolgreich angelegt.")

                    room_list.insert(tkinter.END, f"{room_number}   |   {room_type} |   {capacity}")

                presentation_medium_entry.delete(0, tkinter.END)
                room_number_entry.delete(0, tkinter.END)
                room_type_combobox.delete(0, tkinter.END)
                capacity_entry.delete(0, tkinter.END)
                
                

            else:
                messagebox.showwarning("Warnung", "Bitte alle Eigenschaften eingeben.")

        elif room_type == "Abstellraum":
            area = area_entry.get()
            if area:
                if RM.new_closet(room_number, capacity, area) == -1:
                    messagebox.showwarning("Warnung", f"Raumnummer {room_number} bereits vergeben.")
                else:
                    messagebox.showinfo("Erfolgreich", "Raum erfolgreich angelegt.")

                    room_list.insert(tkinter.END, f"{room_number}   |   {room_type} |   {capacity}")

                area_entry.delete(0, tkinter.END)
                room_number_entry.delete(0, tkinter.END)
                room_type_combobox.delete(0, tkinter.END)
                capacity_entry.delete(0, tkinter.END)
                
            else:
                messagebox.showwarning("Warnung", "Bitte alle Eigenschaften eingeben.")
        
        elif room_type == "Meetingraum":
            if RM.new_meetingroom(room_number,capacity) == -1:
                messagebox.showwarning("Warnung", f"Raumnummer {room_number} bereits vergeben.")
            else:
                messagebox.showinfo("Erfolgreich", "Raum erfolgreich angelegt.")

                room_list.insert(tkinter.END, f"{room_number}   |   {room_type} |   {capacity}")

            area_entry.delete(0, tkinter.END)
            room_number_entry.delete(0, tkinter.END)
            room_type_combobox.delete(0, tkinter.END)
            capacity_entry.delete(0, tkinter.END)
            
            
        
        #pack it parallel to RM object into room_list
       
    else:
        messagebox.showwarning("Warnung", "Bitte alle Eigenschaften eingeben.")


window = tkinter.Tk()
window.title("Raumverwaltung")

frame = tkinter.Frame(window)
frame.pack()


# saving new room
new_room =tkinter.LabelFrame(frame, text="Raum anlegen")
new_room.grid(row= 0, column=0, padx=20, pady=10)

room_number_label = tkinter.Label(new_room, text="Raumnummer")
room_number_label.grid(row=0, column=0)
capacity_label = tkinter.Label(new_room, text="Kapazität")
capacity_label.grid(row=0, column=1)

room_number_entry = tkinter.Entry(new_room)
capacity_entry = tkinter.Entry(new_room)
room_number_entry.grid(row=1, column=0)
capacity_entry.grid(row=1, column=1)

area_label = tkinter.Label(new_room, text="Fläche")
area_entry = tkinter.Entry(new_room)
area_label.grid(row=2, column=0)
area_entry.grid(row=3, column=0)

presentation_medium_label = tkinter.Label(new_room, text="Präsentationsmedium")
presentation_medium_entry = tkinter.Entry(new_room)
presentation_medium_label.grid(row=2, column=1)
presentation_medium_entry.grid(row=3, column=1)

room_type_label = tkinter.Label(new_room, text="Raumart")
room_type_combobox = ttk.Combobox(new_room, values=["Vorlesungsraum", "Abstellraum", "Meetingraum"], state= "readonly")
room_type_label.grid(row=0, column=2)
room_type_combobox.grid(row=1, column=2)


add_button = tkinter.Button(new_room, text="Raum hinzufügen", command=add_room)
add_button.grid(row=3, column=2, sticky="news", padx=20, pady=10)

# Funktion zur Anpassung der Eingabezeile basierend auf dem ausgewählten Raum Typ
def on_room_type_change(event):
    selected_room_type = room_type_combobox.get()
    
    if selected_room_type == "Vorlesungsraum":
        presentation_medium_entry.configure(state="normal")
        area_entry.configure(state="disabled")
    elif selected_room_type == "Abstellraum":
        presentation_medium_entry.configure(state="disabled")
        area_entry.configure(state="normal")
    else:
        presentation_medium_entry.configure(state="disabled")
        area_entry.configure(state="disabled")


room_type_combobox.bind("<<ComboboxSelected>>", on_room_type_change)


for widget in new_room.winfo_children():
    widget.grid_configure(padx=10, pady=5)


############## new customer frame

def add_customer():
    customer_name = customer_name_entry.get()
    customer_mail = customer_mail_entry.get()
        
    if customer_name and customer_mail:
        if RM.new_customer(customer_name, customer_mail) == -1:
            messagebox.showwarning("Warnung", "Kunde bereits angelegt.")
        else:
            messagebox.showinfo("Erfolgreich", "Kunde erfolgreich angelegt.")
            
            customer_list.insert(tkinter.END, f"{customer_name}")

        customer_name_entry.delete(0, tkinter.END)
        customer_mail_entry.delete(0, tkinter.END)       
    else:
        messagebox.showwarning("Warnung", "Bitte alle Kundeneigenschaften eingeben.")

# saving new customer
new_customer =tkinter.LabelFrame(frame, text="Kunden anlegen")
new_customer.grid(row=1, column=0, padx=20, pady=10)


customer_name_label = tkinter.Label(new_customer, text="Kundenname")
customer_name_label.grid(row=0, column=0)
customer_mail_label = tkinter.Label(new_customer, text="Kundenmail")
customer_mail_label.grid(row=0, column=1)

customer_name_entry = tkinter.Entry(new_customer)
customer_mail_entry = tkinter.Entry(new_customer)
customer_name_entry.grid(row=1, column=0)
customer_mail_entry.grid(row=1, column=1)

add_customer_button = tkinter.Button(new_customer, text="Kunden anlegen", command=add_customer)
add_customer_button.grid(row=1, column=2, sticky="news", padx=20, pady=10)


for widget in new_customer.winfo_children():
    widget.grid_configure(padx=10, pady=5)

####show booked rooms and customers and remove them
def remove_room():
    selected_index = room_list.curselection()
    if selected_index:
        room_name = room_list.get(selected_index).split(" ")[0]
        RM.remove_room(room_name)
        room_list.delete(selected_index)
    else:
        messagebox.showwarning("Warnung", "Bitte einen Raum zum entfernen auswählen.")
    

def remove_customer():
    selected_index = customer_list.curselection()
    if selected_index:
        customer_name = customer_list.get(selected_index)
        RM.remove_customer(customer_name)
        customer_list.delete(selected_index)
    else:
        messagebox.showwarning("Warnung", "Bitte einen Kunden zum entfernen auswählen.")
    


display_rooms = tkinter.LabelFrame(frame, text="Raumnummer | Raumart | Kapazität:")
display_customers = tkinter.LabelFrame(frame, text="Kunden: Name")

display_rooms.grid(row=2, column=0, padx=20, pady=10, sticky="w")
display_customers.grid(row=2, column=0, padx=20, pady=10, sticky="e")

room_list = tkinter.Listbox(display_rooms, width = 40)
customer_list = tkinter.Listbox(display_customers, width = 20)
room_list.insert(tkinter.END)
customer_list.insert(tkinter.END)

room_list.grid(row = 0, column= 0)
remove_room_button = tkinter.Button(display_rooms, text="Remove Room", command=remove_room)
remove_room_button.grid(row = 1, column=0)

customer_list.grid(row = 0, column= 0)
remove_customer_button = tkinter.Button(display_customers, text="Remove Customer", command=remove_customer)
remove_customer_button.grid(row = 1, column=0)


for widget in display_rooms.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in display_customers.winfo_children():
    widget.grid_configure(padx=10, pady=5)


## book room
def book_room():
    selected_index_customer = customer_list.curselection()
    selected_index_room = room_list.curselection()

    if selected_index_room:
        customer_name = customer_list.get(selected_index_customer)
        room_name = room_list.get(selected_index_room).split(" ")[0]
        customer_name = messagebox.askquestion("Bitte Kundennamen eingeben.")
        RM.book_room(room_name, customer_name)

    else:
        
        messagebox.showwarning("Warnung", "Bitte Raum auswählen.")
    
    
    pass

booking_room = tkinter.LabelFrame(frame, text="Raum buchen:")
booking_room.grid(row=0, column=1, padx=30, pady=0)

book_room_button = tkinter.Button(booking_room, text = "Raum buchen.", command = book_room)
book_room_button.grid(row = 0, column = 0)



window.mainloop()
##Jason Handling of room management



if __name__ == "__main__":
    #manual json testing
    RM1 = Roommanagement()
    meeting_1 = RM1.new_meetingroom("R0.001", 20)
    closet_1 = RM1.new_closet("R0.002", 10, 20)
    classroom_1 = RM1.new_classroom("R0.003", 10, "Tafel")
    classroom_2 = RM1.new_classroom("R0.004", 20, "Projektor")

    customer_1 = Kunde("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")
    customer_2 = Kunde("Franz Huber", "Franz.Huber@hm.edu")

    RM1.book_room("R0.001", customer_1) 
    RM1.book_room("R0.001", customer_1) 
    RM1.book_room("R0.002", customer_2) 
    RM1.book_room(classroom_1, customer_1)
    
    RM1.new_customer("Johannes Hirschbeck", "Johannes.Hirschbeck@hm.edu")



    #json conversion of data
    data = json.dumps(RM1, default=lambda x: x.__dict__, indent = 4)
    with open('roommanagement.json', 'w', encoding="utf-8") as json_file:
        json_file.write(data)
    
    #converting json back to objects in python
    with open('roommanagement.json', "r", encoding = "utf-8") as json_file:
        raw_RM = json.loads(json_file.read())
        RM = Roommanagement()
        for key, raw_rooms in raw_RM.items():
            if key == "_Roommanagement__rooms":
                    
                for raw_room in raw_rooms:
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
                        
                        new_customer = Kunde(name,mail_address)

                        RM.book_room(new_room, new_customer)
            elif key == "_Roommanagement__customers":
                for raw_customer in raw_rooms:
                    customer_name = raw_customer["_Kunde__name"]
                    customer_mail = raw_customer["_Kunde__mail_address"]
                    
                    RM.new_customer(customer_name, customer_mail)
    # print(RM1)
    # print("\n\n\nNEUER RAUM\n\n\n")
    # print(RM)
    pass