from quiz_brain import QuizBrain
from question_model import QuestionBank

question_bank = QuestionBank()
quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()