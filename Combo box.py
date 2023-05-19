#importing the tkinter class library and importing ttk from the library
import tkinter as tk 
from tkinter import ttk

#creating a fucntion for the event choosing a item from the widget
def on_select(event):
    #create an item object tha obtains the value fo the selected item
    selected_item = event.widget.get()
    print("selected item", selected_item)

#Creating root window called "Combo Box"
root = tk.Tk()
root.title("Combo Box")


#Creating an array of objects called "items"
items = ["Item1", "Item 2", "Item3", "Item 4", "Item 5"]
#Create the combo box object put he object in the root window and populate values
combo_box = ttk.Combobox(root, values=items)

#The bind function will tie the unselected item to the on_select function
combo_box.bind("<<ComboboxSelected>>", on_select)
#pack the object to the screen with the geometry manager
combo_box.pack()

#mainloop keeps the root parent window visable
root.mainloop()

