import random

# Possible choices
choices = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0
round_number = 1

print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit the game.\n")

# Game loop
while True:
    print(f"\n--- Round {round_number} ---")
    user_choice = input("Your choice: ").strip().lower()

    if user_choice == 'quit':
        print("\n👋 Thanks for playing!")
        break

    if user_choice not in choices:
        print("❌ Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine result
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "✅ You win this round!"
        user_score += 1
    else:
        result = "❌ You lose this round."
        computer_score += 1

    # Show result
    print(result)
    print(f"Score => You: {user_score} | Computer: {computer_score}")

    # Ask to play again
    play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if play_again not in ['yes', 'y']:
        print("\n🎉 Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! 👋")
        break

    round_number += 1
