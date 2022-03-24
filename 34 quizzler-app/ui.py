from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUI:
    
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=1,column=2)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.canvas_text = self.canvas.create_text(150,125,text="Question",font=("Arial",20,"italic"),width=280)
        self.canvas.grid(row=2,column=1,columnspan=2,pady=50)

        true = PhotoImage(file="images/true.png")
        self.true = Button(image=true,highlightthickness=0,padx=20,pady=20,command=self.true_pressed)
        self.true.grid(row=3,column=1)

        false = PhotoImage(file="images/false.png")
        self.false = Button(image=false,highlightthickness=0,padx=20,pady=20,command=self.false_pressed)
        self.false.grid(row=3,column=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="END")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_question)
