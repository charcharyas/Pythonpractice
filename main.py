#Ask the user their name and save it
import random
goodc= ["good job gang", "if you were robert i would make out with you(you got it right)", "Jeffery epstien would be proud of you"]
badc= ["...\n are you american?", "your a bad kitten pookie", "GRRRRRRR YOU GOT IT WRONG YA TWINK"]
QUESTIONS = ["what is the capital of France",
           "how many tentacles does a 7 armed octopus have"]
OPTIONS = [["paris", "Paris", "Berlin"],
           ["8", "7", "6"]]
SHORTOPTION =["a", "b", "c"]
AWNSER = [2,1]


QUESTIONFORMAT= "{}\na. {}\nb. {}\nc. {} \n"
play ="yes"
score =0
name=input("Hey, what is your name")
#Greet the user and introduce the quiz

#Ask the user a question

while play =="yes":
     while True:
          try:
               tries = input("hello {} welcome to the game show where we awnser questions \n how many attemts do you want" .format(name))
               tries = int(tries)
               break
          except: 
               print ("errrrrrrrrrrrrm what the filp buddy... that wasn't a number pal. D:")
     score =0
     

     #Tell them the correct answer
     attemps=tries
     while attemps > 0:
     awnser = input(QUESTIONFORMAT.format(QUESTIONS[0], OPTIONS[0][0], OPTIONS[0][1], OPTIONS[0][2])).lower()
          if awnser == OPTIONS[0][AWNSER[0]] or awnser == SHORTOPTION[AWNSER[0]]:
               print(random.choice (goodc))
          else 
     attemps=tries
     while attemps > 0:
        

     play == input("Wanna play again")