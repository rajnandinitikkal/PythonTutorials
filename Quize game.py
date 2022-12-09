print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()
    
print("okay! let's play ")
score = 0

answer = input("What does CPU satnds for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1  
else:
    print("Incorrect!")
    
answer = input("What does GPU satnds for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1  
else:
    print("Incorrect!")
    
answer = input("What does PPP satnds for? ")
if answer.lower() == "point-to-point":
    print("Correct!")
    score += 1  
else:
    print("Incorrect!")
    
answer = input("What does VS satnds for? ")
if answer.lower() == "visiual studio":
    print("Correct!")
    score += 1  
else:
    print("Incorrect!")
    
answer = input("What RAM satnds for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1  
else:
    print("Incorrect!")
    
print("you got " + str(score) + " questions correct! ")
print("you got " + str((score/4) * 100) + "%.")


