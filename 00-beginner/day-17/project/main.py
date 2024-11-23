from question_model import Question
from data import question_data

# create a question data bank
question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

