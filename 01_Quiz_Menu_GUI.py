from tkinter import *
import random


class Quiz_menu:
    def __init__(self,):
        # Formatting variables
        background_color = "light blue"

        #Quiz menu Frame
        self.quiz_menu_frame = Frame(width=300, height=300, bg=background_color)
        self.quiz_menu_frame.grid()

        #Punctuation quiz Heading (row 0)
        self.quiz_heading_label = Label(text="Punctuation Quiz",
                                        font="Arial 20 bold",
                                        bg=background_color,
                                        padx=10, pady=10)
        self.quiz_heading_label.grid(row=0, sticky="N")




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Punctuation Quiz Menu")
    something = Quiz_menu()
    root.mainloop()
