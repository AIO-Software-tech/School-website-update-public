username = 'OGB'

password = '1234'

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")
