from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self):

        # Initalize variables.
        background_colour = "light blue"

        # Converter Frame
        self.converter_frame = Frame(width=300, bg=background_colour,
                                    pady=10)
        self.converter_frame.grid()

        # Temperature converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font=("Verdana", "16", "bold"),
                                        bg=background_colour, padx=10,
                                        pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                            text="Type in the amount to be converted and then push"
                                            " one of the buttons below.", font=("Verdana", "12", "italic"),
                                            wrap=250, justify=CENTER, bg=background_colour, padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font=("Verdana", "10"))
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3), orchid3 | khakil
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font=("Verdana", "10"),
                                  bg="Khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)
        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Verdana", "10"),
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)
        
        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame,
                                     font=("Verdana", "10"), fg="purple",
                                     bg=background_colour, pady=10,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)       

        # History and help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font=("Verdana", "10"),
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font=("Verdana", "10"),
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)


# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    var = Converter()
    root.mainloop()
