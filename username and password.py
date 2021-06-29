username = 'OGB'

password = '#008701Boucher'

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")
    
userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")

no = 'no'
yes = 'yes'

hint = (input("do you need a hint "))
if hint == no:
        userInput = input("What is your username?\n")

    if userInput == username:
        a=input("Password?\n")   
        if a == password:
            print("Welcome!")
        else:
            print("That is the wrong password.")
    else:
        print("That is the wrong username.")
        sys.exit()

username = 'username'
password = 'password'

if hint == yes:
    uorp (input("do you need your username hint or password "))
    if uorp == username:
        #replace 'you inissals' with you username
        print("your inissals")
    if uorp == password:
        #replace 'your school name' with you password
        print("your school name")

userInput = input("What is your username?\n")

if userInput == username:
    a=input("Password?\n")   
    if a == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")

a = 'a'
b = 'b'
c = 'c'
d = 'd'

num = input("pick the amount of number you need a=2,b=3 ")

if num == a:
    print ("a=* b=/ c=+ d=-")
    maths1 = input("pick a calc ulation\n")
    if maths1 == a:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        answer=a*b
        print("your answer is "+ str(answer))
    if maths1 == b:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        answer=a/b
        print("your answer is "+ str(answer))
    if maths1 == c:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        answer=a+b
        print("your answer is "+ str(answer))
    if maths1 == d:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        answer=a-b
        print("your answer is "+ str(answer))


    
if num == b:
    print ("a=* b=/ c=+ d=-")
    maths2 = input("pick a calc ulation\n")
    if maths2 == a:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        c=int(input("number 3 "))
        answer=a*b*c
        print("your answer is "+ str(answer))
    if maths2 == b:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        c=int(input("number 3 "))
        answer=a/b/c
        print("your answer is "+ str(answer))
    if maths2 == c:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        c=int(input("number 3 "))
        answer=a+b+c
        print("your answer is "+ str(answer))
    if maths2 == d:
        a=int(input("number 1 "))
        b=int(input("number 2 "))
        c=int(input("number 3 "))
        answer=a-b-c
        print("your answer is "+ str(answer))
