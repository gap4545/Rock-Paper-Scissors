import random

computer_input = random.randint(1,3)
user_input = input("""Rock, Paper, Or Scissors?
""").lower()

if user_input == "rock" :
    user_input = 1
elif user_input == "paper" :
    user_input = 2
elif user_input == "scissors" :
    user_input = 3

if user_input == 1 and computer_input == 1 :
    print("You and the computer both picked rock! It's a draw!")
elif user_input == 2 and computer_input == 2 :
    print("You and the computer both picked paper! It's a draw!")
elif user_input == 3 and computer_input == 3 :
    print("You and the computer both picked scissors! It's a draw!")
elif user_input == 1 and computer_input == 2 :
    print("You picked rock and the computer picked paper! The computer wins!")
elif user_input == 1 and computer_input == 3 :
    print("You picked rock and the computer picked scissors! You win!")
elif user_input == 2 and computer_input == 1 :
    print("You picked paper and the computer picked rock! You win!")
elif user_input == 2 and computer_input == 3 :
    print("You picked paper and the computer picked scissors! The computer wins!")
elif user_input == 3 and computer_input == 1 :
    print("You picked scissors and the computer picked rock! The computer wins!")
elif user_input == 3 and computer_input == 2 :
    print("You picked scissors and the computer picked paper! You win!")
    
    
    
    #Rock = 1 Paper = 2 Scissors = 3