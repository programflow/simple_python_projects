# TODO: asking the questions
# TODO: Checking if the answer was correct
# TODO: checking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, c_answer):
        if c_answer.lower() == u_answer.lower():
            print("You are right.")
            self.score += 1
        else:
            print("You are wrong. Idiot!")
        print(f"The correct answer was : {c_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        """ This will pull up the question from the  question_list"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(response, current_question.answer)
