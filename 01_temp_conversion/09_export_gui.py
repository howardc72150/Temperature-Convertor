from tkinter import *
from functools import partial
import random


class Convertor:
    def __init__(self, parent):
        # Initialize variables
        background_colour = "light blue"
        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 104 degrees F',
                              '40 degrees C is 4.4 degrees F',
                              '12 degrees C is 53.6 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F']

        # Converter main frame
        self.converter_frame = Frame(width=300, height=300, pady=10, bg=background_colour)
        self.converter_frame.grid()

        # Temperature conversion heading
        self.tempConverter_label = Label(self.converter_frame, text="Temperature Converter",
                                         font=("Verdana", "16", "bold"),
                                         bg=background_colour,
                                         padx=10, pady=10)
        self.tempConverter_label.grid(row=0)

        # history button
        self.history_button = Button(self.converter_frame, text="History", 
                                  padx=10, pady=10,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)
class History:
    def __init__(self, partner, calc_history):
        # Initialize variables
        background_colour = "#a9ef99" # -- Pale Green 

        # Disable history button
        partner.history_button.config(state=DISABLED)

        # Creates child window
        self.history_box = Toplevel()
        
        # If users press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background_colour)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                font=("Verdana", "16", "bold"),
                                bg=background_colour)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations. "
                                  "Please use the export button to create a text file of all your "
                                  "calculations for this session.",
                                  font=("Verdana", "10", "italic"), fg="maroon", justify=LEFT, width=40, 
                                  bg=background_colour, wrap=250)
        self.history_text.grid(row=1)

        # History output goes here (row, 3)

        # Generate string from list of calculations
        histroy_string = ""
        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)
                                               -item-1]+"\n"

        # Label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background_colour, font=("Verdana", "12"),
                                justify=LEFT)
        self.calc_label.grid(row=2)

        # Export and dismiss button frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font=("Verdana", "10", "bold"))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font=("Verdana", "10", "bold"), 
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)
                                     
    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Convertor(root)
    root.mainloop()