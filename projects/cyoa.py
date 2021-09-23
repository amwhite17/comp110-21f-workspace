"""Create Your Own Adventure."""

__author__ = "730281821"


import random
points: int = 0
player: str = ''
count: int = 0
grinning_emoji = "\U0001f600"


def main() -> None:
    global points
    global player 
    greet()
    while(True):
        print("Home Page.")
        print("1 - Rules.")
        print("2 - Begin the Game.")
        print("3 - Arcade.")
        print("4 - End the Game.")
        option = int(input("Choose what you would like to do from the options by entering the corresponding number. "))
        if(option == 1):
            print(f"Welcome, {player} these are the rules.")
            print(f"So far, {player} has {points} points.")
            rules()
            input("Press enter.")
        if(option == 2):
            print(f"{player} has {points} points.")
            print(f"Let's get started, {player}.")
            coin = flip()
            game(coin)  
        if(option == 3):
            print(f"{player} has {points} points.")
            arcade()
        if(option == 4):
            print("Thank you for playing!")
            print(f"Your final score was {points}.")
            print(f"Goodbye, {player}.")


def game(coin: int) -> int:
    global points
    count = 0
    while(True):
        flip: int = random.randint(0, 1)
        print(flip)
        guess = int(input("Guess whether the coin will land on heads or tails. Choose heads by entering 0 or choose tails by entering 1."))
        if (guess == 0):
            print("You guessed heads.")
        else: 
            print("You guessed tails.")
        if (flip == guess):
            global points
            print("You guessed correctly! You will be awarded points!")
            count = count + 1
            if (count == 1):
                points = points + 2
            else:
                if (count == 2):
                    points = points + 4
                else:
                    if (count == 3):
                        points = points + 8
                    else:
                        if (count > 3):
                            points = points + 16
        
        else: 
            print("Sorry, you guessed incorrectly! However, you will receive 1 point for playing.")
            points = points + 1
            count = 0
        return points    
        break 


def arcade() -> int:
    global grinning_emoji
    print("Welcome to the Arcade!")
    print("1 - Words of Encouragement for 1 point.")
    print("2 - Compliment for 2 points.")
    print("3 - Emoji for 3 points.")
    prize = int(input("Select your prize by entering the corresponging number. "))
    if(prize == 1):
        global points
        if points >= 1:
            points = points - 1 
            print("You can do this!")
            input("Press enter to return to Home Page.")
        else:
            print("Not enough points available for this prize.")
            input("Press enter to return to Home Page.") 
    if(prize == 2): 
        if points >= 2:
            points = points - 2
            print("You are so smart!")
            input("Press enter to return to Home Page.")
        else:
            print("Not enough points available for this prize.")
            input("Press enter to return to Home Page.")
    if(prize == 3):
        if points >= 3:
            points = points - 3
            print(f"{grinning_emoji}")
        else:
            print("Not enough points available for this prize.")
            input("Press enter to return to Home Page.")
    return points


def greet() -> None:
    global player
    print("Hello! Thanks for playing CoinFlip! In this game, you will try to correctly guess whether a coin will land on Heads or Tails. ")
    player = str(input("What is your name?"))


def rules() -> None:
    print("A coin will be flipped. It is your job to correctly guess what side the coin will land on. ")
    print("The more correct guesses you have in a row, the more points you will earn! ")
    print("For 1 correct guess, you will receive 2 point.")
    print("For 2 correct guesses, you will receive 4 points.")
    print("For 3 correct guesses you will receive 8 points.")
    print("For 4 or more correct guesses you will receive 16 points.")
    print("For an incorrect guess, you will receive 1 point.")


def flip() -> int: 
    flip = random.randint(0, 1)
    return (flip)


if __name__ == "__main__":
    main()