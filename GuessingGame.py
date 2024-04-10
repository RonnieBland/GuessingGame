import random

def display_title():
    print("Guessing Game")
    print()
    
def play_game(limit):
    number = random.randint(1, limit)
    print(f"I am thinking of a number from 1 to {limit}\n")
    count = 1
    guess = int(input("your guess?:  "))
    
    while(guess != number):
        if guess < number:
            print("too low")
            count += 1
        elif guess > number:
            print("too High")
            count += 1
        guess = int(input("your guess?: "))
    print (f"you guess it in {count} tries.\n")
    
def main():
    display_title()
    again = "yes"
    while again.lower() == "yes":
        limit = int(input("enter the limit: "))
        play_game(limit)
        again = input("Want to play again? Enter (Yes/No)")
        print()
        print ("thanks for playing")
        
if __name__ == "__main__":
    main()