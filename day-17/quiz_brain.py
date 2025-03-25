from question_model import QuestionBank

class QuizBrain:
    def __init__(self, question_bank: QuestionBank):
        # Clone question list to avoid modifying the original list
        self.question_list = question_bank.questions[:]
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = None
        while user_answer is None:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            user_answer = QuizBrain.format_answer(user_answer)
        self.check_answer(user_answer, current_question.answer)

    @staticmethod
    def format_answer(answer: str) -> bool | None:
        answer = answer.lower()
        if answer == "t" or answer == "true":
            return True
        elif answer == "f" or answer == "false":
            return False
        else:
            return None

    def check_answer(self, user_answer: bool, correct_answer: bool):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")