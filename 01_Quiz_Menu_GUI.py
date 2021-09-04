from tkinter import *


class Quiz_menu:
    def __init__(self, ):
        # Formatting variables
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.quiz_menu_frame = Frame(width=300, height=300,
                                     bg=background_color, pady=10)
        self.quiz_menu_frame.grid()

        # Temperture Conversion Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_menu_frame,
                                        text="Punctuation Quiz",
                                        font=("Arial", "20", "bold"),
                                        bg=background_color,
                                        padx=10, pady=10)
        self.quiz_heading_label.grid(row=0, sticky="N")

        # help button (row 1)
        self.start_button = Button(self.quiz_menu_frame, text="Start Quiz",
                                   font=("Arial", "14"),
                                   padx=10, pady=10, command=self.questions)
        self.start_button.grid(row=1)

    def questions(self):
        print("questions")
        self.question_box = Toplevel()
        background_color = "light blue"



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Punctuation Quiz Menu")
    something = Quiz_menu()
    root.mainloop()
