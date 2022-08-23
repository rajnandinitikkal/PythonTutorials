# snake water gun game
import random
lst = ['s','w','g']
chance = 100
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t\t\t\tsnake,water,gun game\n\n")
print("s for snake \n w for water \n g for gun")

# making the game in while
while no_of_chance < chance:
    _input = input('snake ,water, gun : ')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie both 0 point to each \n")

    # if user enter s
    elif _input == "s" and _random == "g" :
        computer_point = computer_point +1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"")