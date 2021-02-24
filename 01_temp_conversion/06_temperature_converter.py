from tkinter import *
from functools import partial
import random



class Converter:
    def __init__(self):

        # Initalize variables
        background_colour = "light blue"

        # Converter frame
        self.converter_Frame = Frame(bg=background_colour, pady=10)
        self.converter_Frame.grid()

        # Temperature converter heading (row=0)
        self.temp_heading_label = Label(self.converter_Frame, text="Temperature Converter",
                                        font=("Verdana", "19", "bold"), bg=background_colour,
                                        pady=10, padx=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row=1)
        self.temp_instructions_label = Label(self.converter_Frame,
                                             text="Type in the amount to be converted"
                                             " and then push one of the buttons below",
                                             font=("Verdana", "15"), wrap=290, justify=LEFT,
                                             bg=background_colour, padx=10, pady=10)