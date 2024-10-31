from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Title", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true = Button(image= true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row= 2)

        false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
