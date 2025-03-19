from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =[]
for i in question_data:
    question_bank.append(Question(i['text'],i['answer']))

#print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
#print(question_bank)
