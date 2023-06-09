import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

RM = Roommanagement()

def submit():
    room_number = entry_room_number.get()
    room_type = dropdown_room_type.get()
    capacity = entry_capacity.get()
    
    if room_number and room_type and capacity:
        if room_type == "Vorlesungsraum":
            presentation_medium = entry_presentation_medium.get()
            
            if presentation_medium:
                if RM.new_classroom(room_number,capacity, presentation_medium) == -1:
                    messagebox.showwarning("Warning", f"Raumnummer {room_number} bereits vergeben.")
                entry_presentation_medium.delete(0, tk.END)
                entry_room_number.delete(0, tk.END)
                dropdown_room_type.delete(0, tk.END)
                entry_capacity.delete(0, tk.END)
                room_list.insert(tk.END, room_number)

            else:
                messagebox.showwarning("Warning", "Please enter all properties.")

        elif room_type == "Abstellraum":
            area = entry_area.get()
            

            if area:
                if RM.new_closet(room_number, capacity, area) == -1:
                    messagebox.showwarning("Warning", f"Raumnummer {room_number} bereits vergeben.")
                entry_area.delete(0, tk.END)
                entry_room_number.delete(0, tk.END)
                dropdown_room_type.delete(0, tk.END)
                entry_capacity.delete(0, tk.END)
                room_list.insert(tk.END, room_number)

            else:
                messagebox.showwarning("Warning", "Please enter all properties.")
        
        elif room_type == "Meetingraum":
            if RM.new_meetingroom(room_number,capacity) == -1:
                messagebox.showwarning("Warning", f"Raumnummer {room_number} bereits vergeben.")
            entry_area.delete(0, tk.END)
            entry_room_number.delete(0, tk.END)
            dropdown_room_type.delete(0, tk.END)
            entry_capacity.delete(0, tk.END)
            room_list.insert(tk.END, room_number)
        
        #pack it parallel to RM object into room_list
       
    else:
        messagebox.showwarning("Warning", "Please enter all properties.")


def remove_room():
    selected_index = room_list.curselection()
    if selected_index:
        RM.remove_room(room_list.get(selected_index))
        room_list.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select a room to remove.")

root = tk.Tk()
root.title("Raumverwaltungssystem")

# Frame für die linke Seite
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)

#Frame für die rechte Seite
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10)

# Raum Name Eingabe
label_room_number = tk.Label(frame_left, text="Raumnummer:")
label_room_number.pack()
entry_room_number = tk.Entry(frame_left)
entry_room_number.pack()

# Kapazität Eingabe
label_capacity = tk.Label(frame_left, text="Kapazität:")
label_capacity.pack()
entry_capacity = tk.Entry(frame_left)
entry_capacity.pack()

# Dropdown-Menü für Raum Typ
label_room_type = tk.Label(frame_left, text="Raum Typ:")
label_room_type.pack()
dropdown_room_type = ttk.Combobox(frame_left, values=["Vorlesungsraum", "Meetingraum", "Abstellraum"])
dropdown_room_type.pack()

# Funktion zur Anpassung der Eingabezeile basierend auf dem ausgewählten Raum Typ
def on_room_type_change(event):
    selected_room_type = dropdown_room_type.get()
    
    if selected_room_type == "Vorlesungsraum":
        entry_presentation_medium.configure(state="normal")
        entry_area.configure(state="disabled")
    elif selected_room_type == "Abstellraum":
        entry_presentation_medium.configure(state="disabled")
        entry_area.configure(state="normal")
    else:
        entry_presentation_medium.configure(state="disabled")
        entry_area.configure(state="disabled")

dropdown_room_type.bind("<<ComboboxSelected>>", on_room_type_change)

# Eingabezeile für presentation_medium
label_presentation_medium = tk.Label(frame_left, text="presentation_medium:")
label_presentation_medium.pack()
entry_presentation_medium = tk.Entry(frame_left, state="disabled")
entry_presentation_medium.pack()

# Eingabezeile für area
label_area = tk.Label(frame_left, text="area:")
label_area.pack()
entry_area = tk.Entry(frame_left, state="disabled")
entry_area.pack()

# Submit Button
submit_button = tk.Button(frame_left, text="Raum hinzufügen", command=submit)
submit_button.pack()

#listbox with rooms of contextmanager
room_list = tk.Listbox(root)
room_list.pack()

# Create a "Remove Room" button
remove_button = tk.Button(root, text="Remove Room", command=remove_room)
remove_button.pack()



root.mainloop()