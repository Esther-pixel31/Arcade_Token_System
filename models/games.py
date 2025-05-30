import random

def guessing_game():
        number = random.randint(1, 10)
        tries = 3
        print("Guess a number between 1 and 10")
        while tries > 0:
            guess = int(input("Your guess: "))
            if guess == number:
                print("🎉 Correct!")
                return 10  # Score
            else:
                print("❌ Try again")
                tries -= 1
        print(f"Game over. The number was {number}.")
        return 0

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    player = input("Choose rock, paper, or scissors: ").lower()
    print(f"Computer chose: {computer}")
    if player == computer:
        print("🤝 It's a tie!")
        return 5
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        print("✅ You win!")
        return 10
    else:
        print("❌ You lose!")
        return 0