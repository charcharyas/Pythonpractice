#Ask the user their name and save it
QUESTIONFORMAT= "{}\na. {}\nb. {}\nc. \n"
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
               print ("errrrrrrrrrrrrm what the filp buddy... that wasn't a numper pal. D:")
     score =0
     

     #Tell them the correct answer
     attemps=tries
     while attemps > 0:
          awnser=input("So, whats the capital of france")
          if awnser == " Paris":
               score +=1
               print ("goodjob! you awnserd paris your score is now {}!" .format(score))
               break
          elif awnser == "":
               print ("why aint you awnsering pookie, i know its you henry")  #End the quiz
               attemps -= 1
          else:
               score -=1
               print("... \n Are you American? also your score is now",score, )
               attemps -= 1
     
     attemps=tries
     while attemps > 0:
          questions = "So now, how many tentacles does a 7 armed octopus have."
          a= 8
          b= 7
          c= 4
          awnser =input(" {}\nA. {} B. {} C {}}" QUESTIONFORMAT.format (questions, a, b, c)).lower()
          if awnser == a or awnser== "a":
               score +=1
               print ("goodjob! you awnserd 8 your score is now {}!" .format(score))
          elif awnser == "":
               print ("why aint you awnsering pookie, i know its you henry")
          elif awnser != "a" or awnser != "a" or awnser != "a":
               print("thats not an awnser buddy")
          else:
               score -=1
               print("... \n Nah man its an octopus of course its gonna be 8 duh. also you now have a total score of",score,)

     play == input("Wanna play again")
     
     


      