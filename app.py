from Question import Question

question_prompt = [
    "warna apel? \n (a) red/green\n(b) purlpe\n(c) orange\n\n",
    "warna pisang? \n (a) red/green\n(b) purlpe\n(c) yelow\n\n",
    "warna stroberi? \n (a) green\n(b) red\n(c) orange\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]



def run_test(questions):
    score = 0;
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("you got "+str(score))



run_test(questions)