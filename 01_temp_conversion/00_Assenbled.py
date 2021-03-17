from tkinter import *
from functools import partial
import random
import re



class Converter:
    def __init__(self):

        # Initalise variables
        background_colour = "light blue"
        self.all_calc_list = []

        # Converter frame
        self.converter_frame = Frame(bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature converter heading (row=0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                        font=("Verdana", "19", "bold"), bg=background_colour,
                                        pady=10, padx=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row=1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be converted"
                                             " and then push one of the buttons below",
                                             font=("Verdana", "15"), wrap=290, justify=LEFT,
                                             bg=background_colour, padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row=2)
        self.to_convert_entry = Entry(self.converter_frame, width=20, font=("Verdana", "14"))
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)  

        # buttons (two columns)
        self.to_c_button = Button(self.conversion_buttons_frame, text="To Centigrade", 
                                  font=("Verdana", "10", "bold"), padx=10, pady=10,
                                  bg="Khaki1", command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame, text="To Fahrenheit", 
                                  font=("Verdana", "10", "bold"), bg="Orchid1", padx=10,
                                  pady=10, command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0,column=1)

        # Answer label (row 4)
        self.converted_label = Label(self.converter_frame, font=("Verdana", "10", "bold"),
                                     fg="purple", bg=background_colour, pady=10,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font=("Verdana", "10", "bold"),
                                       text="Calculation History", width=15,
                                       command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font=("Verdana", "10", "bold"),
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        error_colour = "#ffafaf"

        # Retrieve amount entered into entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = False

            # Check and convert to fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)
            
            # Check and convert to centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)
            
            else:
                answer = "Too cold"
                has_errors = True
            
            # Display answer
            if has_errors == False:
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error_colour)
            
            # Add answer to list for history
            if answer != "Too cold":
                self.all_calc_list.append(answer)
                self.history_button.config(state=NORMAL)
        
        except ValueError:
            self.converted_label.configure(text="Enter a number", fg="red")
            self.to_convert_entry.configure(bg=error_colour)
    
    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        
        return rounded

    def help(self):
        print("You have asked for help!")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

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
        history_string = ""
        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)
                                               -item-1]+"\n"
        else:
             for item in range(0,len(calc_history)):
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
                                    font=("Verdana", "10", "bold"), command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font=("Verdana", "10", "bold"), 
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def export(self, calc_history):
        get_export = Export(self, calc_history)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

class Export:
    def __init__(self, partner, calc_history):
        background = "#a9ef99"       # --  Pale green

        # Disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window
        self.export_box = Toplevel()

        # If users press cross at top, closes export
        # and releases export button.
        self.export_box.protocol('WM_DELETE_WINDOW', 
                                 partial(self.close_export, partner))
        
        # Set up GUI frame
        self.export_frame = Frame(self.export_box, width=3000, bg=background)
        self.export_frame.grid()

        # Set up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text="Export and Instructions",
                                 font=("Verdana", "14", "bold"),
                                 bg=background)
        self.how_heading.grid(row=0)

        # Export instrutcions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box"
                                 " below and press the save button to save your calculation"
                                 " history to a text file.",
                                 justify=LEFT, width=10, wrap=250, bg=background)
        #self.export_text.grid(row=1)

        # Warning text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below"
                                " already exists, its contents will be replaced with your"
                                " calculation history", justify=LEFT, bg="#ffafaf", fg="maroon",
                                font=("Verdana", "10", "italic"), wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,font=("Verdana", "10", "italic"),
                                    justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)
        
        # Error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)


        # Save and cancel frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and cancel buttons (row 0 of save_Cancel frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, calc_history):
        # Regular expression to check filename is valid
        regex = "[A-Za-z0-9]"
        has_errors = "no"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(regex, letter):
                continue
        
            elif letter == " ":
                problem = "(no spaces allowed)"
            
            else:
                problem = (" (no {}'s allowed)".format(letter))
            has_errors = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_errors = "yes"
        
        if has_errors == "yes":
            # Display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            # Change entry box background to pink
            self.filename_entry.config(bg="#ffafaf")
            print()
        
        else:
            filename = filename + ".txt"
            f = open(filename, "w+")

            for item in calc_history:
                f.write(item + "\n")
            
            f.close()
            self.close_export(partner)

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

# Main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    var = Converter()
    root.mainloop()