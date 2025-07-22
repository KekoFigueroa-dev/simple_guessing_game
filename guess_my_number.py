import random
#Guess my number app

#Welcome
print("Welcome to my Guess my number app")

#Getting player name
while True:
        player_name = input("Hello! what is your name?: ")
        if player_name != "":
            print(f"Well {player_name.title()}, I am thinking of a number between 1 and 20. Ill give you five chances to take a guess.")
            break
        else:
            print("Please enter a user name")

#Answer = random int 
answer = random.randint(1, 20)

#Main loop getting guess - 5  checkss 
for i in range(5):
    player_guess = int(input("Take a guess: "))
    if player_guess == answer:
        print(f"Congratulations {player_name.title()}! You got it in {i + 1} guesses!")
        break
    elif player_guess > answer:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
else:  
    print(f"Sorry! The number I was thinking of was {answer}")


#Thank you - msg
print("Thank you for testing my little app here's a reward")
