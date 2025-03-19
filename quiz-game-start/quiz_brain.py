class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
# curren q is object from question model with text atrribute
        current_q = self.question_list[self.question_number]
        print(current_q)
        self.question_number += 1
        usr_answer = input(f"question: {current_q.text}, true or false?\n")
        self.check_answer(usr_answer,current_q.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, usr_answer, current_q.answer):
        if user_answer.lower() == 
