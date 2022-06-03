from msilib.schema import Component
import tkinter
from xml.dom.minidom import AttributeList
import customtkinter
from tkinter import ANCHOR, StringVar, filedialog, Text
from datamanagement import *


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):

    WIDTH = 900
    HEIGHT = 600

    def __init__(self):
        super().__init__()

    #Configure window grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    #Configure window
        self.title("Chemical Inventory Manager.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing) 

    #Configure inventory frame
        self.inventory_frame = customtkinter.CTkFrame(master = self, corner_radius=0)
        self.inventory_frame.grid(row=0, column=0, sticky="nswe")

    #Configure inventory frame buttons
        self.inventory_frame.grid_rowconfigure(4, weight=1) 

        self.inventory_label = customtkinter.CTkLabel(master=self.inventory_frame, text="Inventory", text_font=("Roboto Medium", -24))
        self.inventory_label.grid(row=1, column=0, pady=10, padx=7, sticky="w")

        self.inventory_button = customtkinter.CTkButton(master = self.inventory_frame, text= "View Complete Inventory",  fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -16), width = 215)
        self.inventory_button.grid(row=2, column = 0, pady = 10, padx = 15)

        self.inventory_file_button = customtkinter.CTkButton(master = self.inventory_frame, text= "Go To Inventory File",  fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -16), width=215)
        self.inventory_file_button.grid(row=3, column = 0, pady = 10, padx = 15)

        #Storage Scroll Frame
        self.storage_scroll_frame = customtkinter.CTkFrame(master = self.inventory_frame, width=215)
        self.storage_scroll_frame.grid(row=4, column=0, pady=10, padx=15, sticky="nsew")

        self.storage_scroll_frame.grid_columnconfigure(0, weight=1)

        rooms = ["409", "408", "407", "406", "405", "404"]
        for idx, room in enumerate(rooms):
            self.room_button = customtkinter.CTkButton(master = self.storage_scroll_frame, text = "Room " + room, fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -14), width = 135, height = 30)
            self.room_button.grid(row=idx, column=0, pady=15)

        #Storage Frame
        self.add_storage_frame = customtkinter.CTkFrame(master = self.inventory_frame)
        self.add_storage_frame.grid(row=5, column=0, pady=10)

        self.add_room_button = customtkinter.CTkButton(master = self.add_storage_frame, width = 100, text= "Add\nRoom",  fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -12))
        self.add_room_button.grid(row=0, column = 0, pady = 10, padx = (6, 3))

        self.add_container_button = customtkinter.CTkButton(master = self.add_storage_frame, width=100, text= "Add\nContainer",  fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -12))
        self.add_container_button.grid(row=0, column = 1, pady = 10, padx = (3, 6))

        #Center Frame
        self.center_frame = customtkinter.CTkFrame(master = self)
        self.center_frame.grid(row=0, column=1, padx = 15, pady=15, sticky="news")
        self.center_frame.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_rowconfigure(0, weight=0)
        self.center_frame.grid_rowconfigure(1, weight=1)

        #input Frame
        self.input_frame = customtkinter.CTkFrame(master = self.center_frame)
        self.input_frame.grid(row=0, column=0, padx = 10, pady=10, sticky="new")

        self.input_label = customtkinter.CTkLabel(master=self.input_frame, text="Chemical Input", text_font=("Roboto Medium", -16))
        self.input_label.grid(row=0, column=0, pady = 6, padx = 3, sticky="nw")

        #CAS Input
        self.cas_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.cas_frame.grid(row=1, column=0, padx = (30, 10), pady=10, sticky="nw")

        self.cas_label = customtkinter.CTkLabel(master=self.cas_frame, text="CAS Number", text_font=("Roboto Medium", -14))
        self.cas_label.grid(row=0, column=0, sticky="nw", pady = 5)

        self.cas_entry = customtkinter.CTkEntry(master=self.cas_frame, width=150)
        self.cas_entry.grid(row=0, column=1, sticky="nw", padx = (0, 13), pady = 5)

        #Mass Input
        self.mass_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.mass_frame.grid(row=2, column=0, padx = (30, 10), pady=10, sticky="nw")

        self.mass_label = customtkinter.CTkLabel(master=self.mass_frame, text="Mass", text_font=("Roboto Medium", -14))
        self.mass_label.grid(row=0, column=0, sticky="nw", pady = 5)

        self.mass_entry = customtkinter.CTkEntry(master=self.mass_frame, width=150)
        self.mass_entry.grid(row=0, column=1, sticky="nw", padx = (0, 13), pady = 5)

        #Unit Input
        self.unit_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.unit_frame.grid(row=2, column=1, padx = (0,30), pady=10, sticky="nw")

        self.unit_label = customtkinter.CTkLabel(master=self.unit_frame, text="Unit", text_font=("Roboto Medium", -14))
        self.unit_label.grid(row=0, column=0, sticky="nw", pady = 5)

        unit_value = StringVar()
        unit_value.set("g")
        unit_options = customtkinter.CTkOptionMenu(master = self.unit_frame, variable = unit_value, values=["g", "mL", "kg"], fg_color=("gray75", "gray30"), button_color="gray20")
        unit_options.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        #Quantity Input
        self.quantity_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.quantity_frame.grid(row=3, column=0, padx = (30, 10), pady=10, sticky="nw")

        self.quantity_label = customtkinter.CTkLabel(master=self.quantity_frame, text="Quantity", text_font=("Roboto Medium", -14))
        self.quantity_label.grid(row=0, column=0, sticky="nw", pady = 5)

        self.quantity_entry = customtkinter.CTkEntry(master=self.quantity_frame, width=150)
        self.quantity_entry.grid(row=0, column=1, sticky="nw", padx = (0, 13), pady = 5)

        #Unit Input
        self.state_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.state_frame.grid(row=3, column=1, padx = (0, 30), pady=10, sticky="nw")

        self.state_label = customtkinter.CTkLabel(master=self.state_frame, text="State of Matter", text_font=("Roboto Medium", -14))  
        self.state_label.grid(row=0, column=0, sticky="nw", pady = 5)

        state_value = StringVar()
        state_value.set("solid")
        state_options = customtkinter.CTkOptionMenu(master = self.state_frame, variable = state_value, values=["solid", "liquid", "gas"], fg_color=("gray75", "gray30"), button_color="gray20")
        state_options.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        
        #Room Input
        self.room_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.room_frame.grid(row=4, column=0, padx = 30, pady=10, sticky="nw")

        self.room_label = customtkinter.CTkLabel(master=self.room_frame, text="Room", text_font=("Roboto Medium", -14)) 
        self.room_label.grid(row=0, column=0, sticky="nw", pady = 5)

        room_value = StringVar()
        room_value.set(rooms[0])
        room_options = customtkinter.CTkOptionMenu(master = self.room_frame, variable = room_value, values=rooms, fg_color=("gray75", "gray30"), button_color="gray20")
        room_options.grid(row=0, column=1, padx=5, pady=5, sticky="W")

        containers = ["1", "2", "3", "4", "5"]
        #Container Input
        self.container_frame = customtkinter.CTkFrame(master = self.input_frame, corner_radius=5, width= 200)
        self.container_frame.grid(row=4, column=1, padx = (0, 30), pady=10, sticky="nw")

        self.container_label = customtkinter.CTkLabel(master=self.container_frame, text="Container", text_font=("Roboto Medium", -14)) 
        self.container_label.grid(row=0, column=0, sticky="nw", pady = 5)

        container_value = StringVar()
        container_value.set(containers[0])
        container_options = customtkinter.CTkOptionMenu(master = self.container_frame, variable = container_value, values=containers, fg_color=("gray75", "gray30"), button_color="gray20")
        container_options.grid(row=0, column=1, padx=5, pady=5, sticky="W")


        #output Frame
        self.output_frame = customtkinter.CTkFrame(master = self.center_frame)
        self.output_frame.grid(row=1, column=0, padx = 10, pady=10, sticky="news")

        self.output_label = customtkinter.CTkLabel(master=self.output_frame, text="Chemical Output", text_font=("Roboto Medium", -16))
        self.output_label.grid(row=0, column=0, pady = 3, sticky="nw")
        self.output_frame.grid_columnconfigure(0, weight=1)
        self.output_frame.grid_rowconfigure(0, weight=0)


        #Output
        self.chemical_output_frame = customtkinter.CTkFrame(master = self.output_frame, corner_radius=5, height= 100)
        self.chemical_output_frame.grid(row=1, column=0, padx = 20, pady=10, sticky="new")

        def addChemicalClick(cas, mass, quantity, unit, state):
            attributeList = findInfo(cas, mass, quantity, unit, state)
            attributeList[2] = attributeList[2] + " " + attributeList[3]
            attributeList.pop(3)
            chemical = ",   ".join(attributeList)
            self.chemical_component_label = customtkinter.CTkLabel(master = self.chemical_output_frame, text= chemical, text_font=("Roboto Medium", -14))
            self.chemical_component_label.grid(row=0, column=idx, pady=10)

        #Input Buttons
        self.search_inventory_button = customtkinter.CTkButton(master = self.input_frame, text= "Search Inventory",  fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -16))
        self.search_inventory_button.grid(row=5, column = 0, pady = (10, 15), padx = 30, sticky = "w")

        self.add_chemical_button = customtkinter.CTkButton(master = self.input_frame, text= "Enter Chemical", text_font=("Roboto Medium", -16))
        self.add_chemical_button.grid(row=5, column = 1, pady = (10, 15), padx = 30, sticky = "e")

        #Output Butooms
        self.search_inventory_button = customtkinter.CTkButton(master = self.output_frame, text= "Delete",  fg_color=("gray75", "gray30"), text_font=("Roboto Medium", -16))
        self.search_inventory_button.grid(row=3, column = 0, pady = (10, 15), padx = 20, sticky = "w")

        
        
            



        

        





        #TODO delete Button

        #TODO done Button


    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

#canvas = tk.Canvas(root, height=300, width=500, bg="#263D42")
#canvas.pack() 

#frame = tk.Frame(root, bg="#263D42")
#frame.place(relwidth=0.95, relheight=0.9, relx=0.025, rely=0.025)

#openFile = tk.Label(frame, text="CAS Number", bg="white", fg="#263D42")
#openFile.grid(row=0, column=0, padx= 5, pady= 5)

#casNumber = tk.Entry(frame, bg="white", fg="#263D42")
#casNumber.grid(row=0, column=1, padx= 5, pady= 5)

#massLabel = tk.Label(frame, text= "Mass", bg="white", fg="#263D42")
#massLabel.grid(row=1, column=0, padx= 5, pady= 5)

#massEntry = tk.Entry(frame, bg="white", fg="#263D42")
#massEntry.grid(row=1, column=1, padx= 5, pady= 5)

#quantityLabel = tk.Label(frame, text= "Quantity", bg="white", fg="#263D42")
#quantityLabel.grid(row=2, column=0, padx= 5, pady= 5)

#quantityEntry = tk.Entry(frame, bg="white", fg="#263D42")
#quantityEntry.grid(row=2, column=1, padx= 5, pady= 5)

#stateValue = StringVar()
#stateValue.set("solid")
#stateOptions = tk.OptionMenu(frame, stateValue, "solid", "liquid", "gas")
#stateOptions.grid(row=2, column=2, padx=5, pady=5, sticky="W")

#value = StringVar()
#value.set("g")
#unitOptions = tk.OptionMenu(frame, value, "g", "mL", "kg")
#unitOptions.grid(row=1, column=2, padx=5, pady=5, sticky="W")

#enterButton = tk.Button(frame, text="Enter", padx=10, pady=5, 
#                    fg="#263D42", bg="white", command= lambda: findInfo(casNumber.get(), massEntry.get(), quantityEntry.get(), value.get(), stateValue.get()))
#enterButton.grid(row=2, column=3, padx= 5, pady= 5, sticky="E")

#root.mainloop()