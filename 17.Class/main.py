from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    txt = question["text"]
    answer = question["answer"]
    question_bank.append(Question(txt,answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz completed")
print(f"Score = {quiz.score}/{quiz.question_number}")