import random

def play_game():
    human_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        human_choice = input("Enter your choice (rock, paper, scissors): ")
        while human_choice not in choices:
            human_choice = input("Invalid choice. Enter your choice (rock, paper, scissors): ")

        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        if (human_choice == 'rock' and computer_choice == 'scissors') or \
           (human_choice == 'scissors' and computer_choice == 'paper') or \
           (human_choice == 'paper' and computer_choice == 'rock'):
            human_score += 1
            print("You won!")
        elif human_choice == computer_choice:
            print("You tied!")
        else:
            computer_score += 1
            print("You lost!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print(f"Your score: {human_score}, Computer's score: {computer_score}")
            break

play_game()