from tkinter import *
from functools import partial
import random


class Convertor:
    def __init__(self, parent):
        # Initialize variables
        background_colour = "light blue"

        # Converter main frame
        self.converter_frame = Frame(width=300, height=300, pady=10, bg=background_colour)
        self.converter_frame.grid()

        # Temperature conversion heading
        self.tempConverter_label = Label(self.converter_frame, text="Temperature Converter",
                                         font=("Verdana", "16", "bold"),
                                         bg=background_colour,
                                         padx=10, pady=10)
        self.tempConverter_label.grid(row=0)

        # Help button
        self.help_button = Button(self.converter_frame, text="Help", 
                                  padx=10, pady=10,
                                  command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You have asked for help!")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):
        # Initialize variables
        background_colour = "orange" 

        # Disable help button
        partner.help_button.config(state=DISABLED)

        # Creates child window
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI frame
        self.help_frame = Frame(self.help_box, width=300, bg=background_colour)
        self.help_frame.grid()

        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help and Information",
                                font=("Verdana", "16", "bold"),
                                bg=background_colour)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, 
                               bg=background_colour, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss", width=10,bg=background_colour,
                                     font=("Verdana", "10"),
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2,pady=10)
    
    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()







if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Convertor(root)
    root.mainloop()