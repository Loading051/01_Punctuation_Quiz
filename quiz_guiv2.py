from tkinter import *

# root for the gui
root = Tk()
root.geometry("455x400")
root.configure(bg="light blue")
root.title("Punctuation Quiz")


class Quiz:
    # defining the terms
    def __init__(self):
        self.qn = 8
        self.qno = 1
        self.quest = StringVar()
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options(self.qn)
        self.buttons()

    # this will add the question to the quiz
    def question(self, qn):
        t = Label(root, text="~\b Punctuation ._. quiz questions \b~", width=50, bg="blue", fg="white",
                  font=("arial", 12, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, textvariable=self.quest, width=60, font=("arial", 11, ""), bg="light blue", anchor="w")
        qn.place(x=5, y=50)
        return qn

    # this will add buttons for the answers to the gui.
    def radio_buttons(self):
        val = 0
        b = []
        yp = 100
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1,
                              width=30,
                              bg="pink", fg="black", font=("arial", 16, "bold"), anchor="w")
            b.append(btn)
            btn.place(x=25, y=yp)
            val += 1
            yp += 50
        return b

    # will add a plus one to the numbers on the questions
    def display_options(self, qn):
        self.opt_selected.set(0)

    # this will add buttons for the next and quit button of the gui
    def buttons(self, mode="normal"):
        if mode == "normal":
            n_button = Button(root, text="Next", command=self.next_button, width=10, bg="green", fg="white",
                              font=("arial", 16, "bold"))
            n_button.place(x=60, y=330)

        quit_button = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                             font=("arial", 16, "bold"))
        quit_button.place(x=260, y=330)

    # when clicking the next button this will check if the answer is right or not and then add to the score
    def next_button(self):
        self.qn += 1
        self.qno += 1


quiz = Quiz()
root.mainloop()
