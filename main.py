#Ask the user their name and save it
score =0
name=input("Hey, what is your name")
#Greet the user and introduce the quiz
print ("hello" ,name, "welcome to the game show where we awnser questions")
#Ask the user a question
awnser=input("So, whats the capital of france")

#Tell them the correct answer
if awnser == " Paris":
    score +=1
    print ("goodjob! your score is now",score, "!")
elif awnser == " ":
     print ("why aint you awnsering pookie, i know its you henry")  #End the quiz
else:
     print("... \n Are you American? also your score is now",score, )
     score -=99999999999999999999999999999999999999999


      