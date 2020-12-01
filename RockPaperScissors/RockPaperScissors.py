import random


def calculator():

	computer_input = random.randint(1, 3)
	user_input = input("""Welcome to Rock, Paper, Scissors!
	Select your input!
	1. Rock
	2. Paper
	3. Scissors
	""")

	if isinstance(user_input, int):
		print("Not a number asshole.")

	else:

		while user_input.lower() == "rock" or "paper" or "scissors":
		
			if isinstance(user_input, int):
				print("Not a number asshole.")
				break

			elif user_input.lower() == "rock" and computer_input == 1:
				print("You and the computer both picked rock! It's a draw!")
				break

			elif user_input.lower() == "paper" and computer_input == 2:
				print("You and the computer both picked paper! It's a draw!")
				break

			elif user_input.lower() == "scissors" and computer_input == 3:
				print("You and the computer both picked scissors! It's a draw!")
				break

			elif user_input.lower() == "rock" and computer_input == 2:
				print("You picked rock and the computer picked paper! The computer wins!")
				break

			elif user_input.lower() == "rock" and computer_input == 3:
				print("You picked rock and the computer picked scissors! You win!")
				break

			elif user_input.lower() == "paper" and computer_input == 1:
				print("You picked paper and the computer picked rock! You win!")
				break

			elif user_input.lower() == "paper" and computer_input == 3:
				print("You picked paper and the computer picked scissors! The computer wins!")
				break

			elif user_input.lower() == "scissors" and computer_input == 1:
				print("You picked scissors and the computer picked rock! The computer wins!")
				break

			elif user_input.lower() == "scissors" and computer_input == 2:
				print("You picked scissors and the computer picked paper! You win!")
				break

			else:
				print("Wrong selection retard. Learn to spell.")
				break

		quit()
	
		print("Wrong selection or you used weird ass casing. Fix your shit dumbass.")


calculator()
