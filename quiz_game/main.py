from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    n_text = question["question"]
    n_answer = question["correct_answer"]
    new_question = Question(n_text, n_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()

print("You're complete the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
