energy = 10
import random
while 20 > energy > 0:
    print(f"Current energy: {energy}")
    
    action = input ("Choose an action: move, rest, or guess: ")
    if action == "move":
        action_happen = random.randint(1, 10)
        if action_happen >= 2:
            print("You found food! +3 energy")
            energy += 3
        elif 5 >= action_happen >2:
            print("Nothing happened.")
        elif action_happen > 5:
            print("You got hurt! -2 energy")
            energy -= 2

    elif action == "rest":
        print("You rested. +2 energy")
        energy += 2
    elif action == "guess":
        number = random.randint(1, 5)
        guess = int(input("Guess a number between 1 and 5: "))
        if guess == number:
            print("You guessed right! +5 energy")
            energy += 5
        else:
            print(f"Wrong! The correct number was {number}. -2 energy")
            energy -= 2
    else:
        print("Invalid action. Please choose move, rest, or guess. You lose an energy point.")
        energy -= 1

if energy >= 20:
    print("Congratulations! You have escaped the loop with enough energy.")
elif energy <= 0:
    print("You have run out of energy and cannot continue.")