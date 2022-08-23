# snake water gun game
import random
lst = ['s','w','g']
chance = 20
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t\t\t\tsnake,water,gun game\n\n")
print("s for snake \nw fur water \ng for gun")

#making the game in while
while no_of_chance < chance:
    _input = input('snake , water , gun :')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie both 0 point to each \n")

   # if user enter s
    elif _input == "s" and _random == "g" :
        computer_point = computer_point +1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f" computer_point is {computer_point} and your point is {human_point}\n")

    elif _input == "s" and _random == "w" :
        human_point = human_point +1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("human wins 1 point \n")
        print(f" computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random == "g":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer is {_random} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    #if user enter g
    elif _input == "g" and _random == "s":
        computer_point = computer_point +1
        print(f"your guess {_input} and computer is {_random} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    elif _input == "g" and _random == "w" :
        computer_point = computer_point +1
        print(f"your guess {_input} and computer is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point}")

    else:
        print("you have input wrong \n")

