from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create a question data bank
question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_brain = QuizBrain(question_bank)

quiz_brain.next_question()
