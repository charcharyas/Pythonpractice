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
<<<<<<< HEAD
     #Tell them the correct answer

     score==0

          for i in range(len(QUESTIONS)):
     attemps=tries
     while attemps > 0:
          awnser = input(QUESTIONFORMAT.format(QUESTIONS[i], OPTIONS[i][0], OPTIONS[i][1], OPTIONS[i][2])).lower()
          if awnser == OPTIONS[0][AWNSER[0]] or awnser == SHORTOPTION[AWNSER[0]]:
          print(random.choice (goodc))
     elif awnser in SHORTOPTION or awnser in OPTIONS[0]:
          print(random.choice (badc))
     else
          print("wrong!")
          print("That wasn't an awnser pal.\nGRRRRRRR daddy is now mad at you")
play == input("Wanna play again")
=======
     #Tell them the correct answe
     for i in range(len(QUESTIONS)):
          attemps=tries
          while attemps > 0:
               awnser = input(QUESTIONFORMAT.format(QUESTIONS[i], OPTIONS[i][0], OPTIONS[i][1], OPTIONS[i][2])).lower()
               if awnser == OPTIONS[i][AWNSER[i]] or awnser == SHORTOPTION[AWNSER[i]]:
                    print(random.choice (goodc))
                    break
               elif awnser in SHORTOPTION or awnser in OPTIONS[i]:
                  print(random.choice (badc))
                  print("super rizz")
               else:    
                    print("That wasn't an awnser pal.\nGRRRRRRR daddy is now mad at you")
          play == input("Wanna play again")
>>>>>>> c3490f02653c49216f4f71e3da997aea5051660e
