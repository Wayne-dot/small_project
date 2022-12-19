from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        trueimage = PhotoImage(file="./images/true.png")
        self.truebutton = Button(image=trueimage, highlightthickness=0, command=self.true_press)
        self.truebutton.grid(column=0, row=2)

        falseimage = PhotoImage(file="./images/false.png")
        self.falsebutton = Button(image=falseimage, highlightthickness=0, command=self.false_press)
        self.falsebutton.grid(column=1, row=2)

        self.score_lable = Label(text="Score: 0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score_lable.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have finish the quiz!")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")

    def true_press(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)  #need fucntion on input
