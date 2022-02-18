class QuizBrain:
    def __init__(self, list) -> None:
        self.question_number = 0
        self.questions_list = list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Question {self.question_number}: {question.text} (True/False): ")
        self.check_answer(answer,question.answer)

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Good answer!")
            self.score += 1
        else:
            print("Bad answer!")
        print(f"Correct answer was {correct_answer}")
        print(f"Current score = {self.score}/{self.question_number}")
        print("\n")
