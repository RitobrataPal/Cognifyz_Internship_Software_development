import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Player makes a choice
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if player_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
        
        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the game
rock_paper_scissors()
