from tkinter import *
from tkinter import messagebox as mb
import json
import random

root = Tk()
root.geometry("455x400")
root.configure(bg="light blue")
root.title("Punctuation Quiz")
with open('quiz.json') as f:
    obj = json.load(f)
q = (obj['ques'])
options = (obj['options'])
a = (obj['ans'])
z = zip(q, options, a)
L = list(z)
random.shuffle(L)
q, options, a = zip(*L)



class Quiz:
    def __init__(self):
        self.qn = 8
        self.qno = 1
        self.quest = StringVar()
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0
        #self.histroy = self.opt_selected


    def history(self):
        return False


    def question(self, qn):
        t = Label(root, text="Punctuation quiz questions", width=50, bg="blue", fg="white", font=("times", 12, "bold"))
        t.place(x=0, y=2)
        self.quest.set(str(self.qno) + ". " + q[qn])
        qn = Label(root, textvariable=self.quest, width=60, font=("times", 12, ""), bg="light blue", anchor="w")
        qn.place(x=5, y=50)
        return qn

    def radio_buttons(self):
        val = 0
        b = []
        yp = 100
        while val < 4:
            btn = Radiobutton(root, text=" ", command=self.next_button, variable=self.opt_selected, value=val + 1,
                              width=30,
                              bg="pink", fg="black", font=("times", 16, "bold"), anchor="w")
            b.append(btn)
            btn.place(x=25, y=yp)
            val += 1
            yp += 50
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[val]['text'] = op
            val += 1

    def buttons(self):
        n_button = Button(root, text="Next", command=self.next_button, width=10, bg="green", fg="white",
                          font=("times", 16, "bold"))
        n_button.place(x=60, y=330)
        quit_button = Button(root, text="Quit", command=root.destroy, width=10, bg="red", fg="white",
                             font=("times", 16, "bold"))
        quit_button.place(x=260, y=330)

    def checkins(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True

    def next_button(self):
        if self.checkins(self.qn):
            self.correct += 1
        self.qn += 1
        self.qno += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.quest.set(str(self.qno) + ". " + q[self.qn])
            self.display_options(self.qn)

    def display_result(self):
        score = int(self.correct / len(q) * 200)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc - 8)
        #history = "list. of questions: " + str(self.histroy)
        #answers = str(self.history)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))





quiz = Quiz()
root.mainloop()
