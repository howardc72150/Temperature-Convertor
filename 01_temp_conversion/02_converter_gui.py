from tkinter import *
from functools import partial
import random

class Converter:
    def __init__(self):

        # Initalize variables.
        background_colour = "light blue"

        # Converter Frame
        self.converter_frame = Frame(width=400, bg=background_colour,
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

        # Answer label (row 4)

        # History and help button frame (row 5)

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    var = Converter()
    root.mainloop()
