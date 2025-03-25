from data import data

class Question:
    def __init__(self, text: str, answer: bool):
        self.text = text
        self.answer = answer

class QuestionBank:
    def __init__(self):
        self.questions: list = []
        for question in data:
            self.questions.append(Question(question["text"], question["answer"]))