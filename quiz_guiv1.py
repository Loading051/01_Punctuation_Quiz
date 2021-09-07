from tkinter import *


# root for the gui
root = Tk()
root.geometry("455x400")
root.configure(bg="light blue")
root.title("Punctuation Quiz")


class Quiz:
    # defining the terms
    def __init__(self):
        self.quest = StringVar()
        self.opt_selected = IntVar()
        self.buttons()

    # this will add buttons for the next and quit button of the gui
    def buttons(self, mode="normal"):
        if mode == "normal":
            n_button = Button(root, text="Next", width=10, bg="green", fg="white",
                              font=("arial", 16, "bold"))
            n_button.place(x=60, y=330)

        quit_button = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                             font=("arial", 16, "bold"))
        quit_button.place(x=260, y=330)


quiz = Quiz()
root.mainloop()
