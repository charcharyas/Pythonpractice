#functions
def intro():
    name = input("hey, whats your name")
    print("Hey",name, "there welcome to my Top 10 Quiz!!!")
def getlives():
    while True:
        lives =input("how many lives do you want")
        try:
            lives = int(lives)
            if lives > 0:
                return lives
            else:
                print("Your not cool buddy, I know you may think you are sooooooo smart for putting a number that is 0 or under but did you know that not a single person actually likes you? ")
        except: 
            print ("errrrrrrrrrrrrm what the filp buddy... that wasn't a number pal. D:")
def getpassword():
    while True:
        password = input("Whats the password")
        if password == ("password"):
            return
        else:
            print ("Nah uh bro, try again")
#maincode
intro()
lives = getlives()
print("coolio then one more this before we get started")
getpassword()