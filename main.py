#Ask the user their name and save it
import random

good_comments = [
    "Good job, gang!",
    "If you were Robert, I would make out with you (you got it right)",
    "Jeffrey Epstein would be proud of you"
]

bad_comments = [
    "...\n Are you American?",
    "You're a bad kitten, pookie",
    "GRRRRRR, YOU GOT IT WRONG!!!"
]

questions = [
    "What is the capital of France?",
    "How many tentacles does a 7-armed octopus have?"
]

options = [
    ["paris", "Berlin", "Paris"],
    ["8", "7", "6"]
]

short_options = ["a", "b", "c"]
answers = [2,0]

question_format = "{}\na. {}\nb. {}\nc. {} \n"
play = "yes"

name = input("Hey, what is your name? ")

while play.lower() == "yes":
    # Greet the user and introduce the quiz
    while True:
        try:
            tries = input(f"Hello {name}, welcome to the game show where we answer questions!\nHow many attempts do you want? ")
            tries = int(tries)
            break
        except ValueError:
            print("Errrrrrrrrrrrrm, what the flip buddy... that wasn't a number, pal. D:")

    score = 0

    for i in range(len(questions)):
        attempts = tries
        while attempts > 0:
            answer = input(question_format.format(questions[i], options[i][0], options[i][1], options[i][2])).lower()
            if answer == options[i][answers[i]].lower() or answer == short_options[answers[i]]:
                print(random.choice(good_comments))
                score += 1
                break
            elif answer in short_options or answer in options[i]:
                print(random.choice(bad_comments))
                score -= 1
                attempts -= 1
            elif answer == "":
                print("Why aren't you answering, pookie?")
            else:
                print("That wasn't an answer, pal.\nGRRRRRR, daddy is now mad at you")
                attempts -= 1

    print("well done {} you got a score of {}".format(name,score))
    play = input("Wanna play again? (yes/no) ")

print("Thanks for playing!")
