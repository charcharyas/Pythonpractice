#Ask the user their name and save it
play =yes
score =0
name=input("Hey, what is your name")
#Greet the user and introduce the quiz
print ("hello" ,name, "welcome to the game show where we awnser questions")
#Ask the user a question
while play =="yes":
     score =0
     awnser=input("So, whats the capital of france")

     #Tell them the correct answer
          if awnser == " Paris":
          score +=1
          print ("goodjob! you awnserd paris your score is now {}!" .format(score))
          elif awnser == "":
          print ("why aint you awnsering pookie, i know its you henry")  #End the quiz
          else:
          score -=1
          print("... \n Are you American? also your score is now",score, )
     
     awnser ==input("So now, how many tentacles does a 7 armed octopus have. is it \nA.8\nB.7\nC.4 ")
          if awnser == "C":
          score +=1
          print ("goodjob! you awnserd paris your score is now {}!" .format(score))
          elif awnser == "":
          print ("why aint you awnsering pookie, i know its you henry")
          elif awnser != "A" or awnser != "B" or awnser != "C":
          print("thats not an awnser buddy")
          else:
          score -=1
          print("... \n Nah man its an octopus of course its gonna be 8 duh. also you now have a total score of",score,)

     play == input("Wanna play again")
     
     


      