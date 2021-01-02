def rps():
	""" this function takes no inputs but inputs are defined inside """

	print("Welcome to Rock-Paper-Scissors Game!")
	global rounds
	rounds = 0
	global input_list

	input_list = []
	movePlayer1 = input("Player 1's move:")
	input_list.append(movePlayer1)
	movePlayer2 = input("Player 2's move:")
	input_list.append(movePlayer2)
	movePlayer3 = input("Player 3's move:")
	input_list.append(movePlayer3)


	def rps_2_person(rounds, input_list): 
		""" Rock paper scissors with two players
		This function takes rounds and input_list
		if third user is Taylor Swift it will take the users down below
		but if it's called from 3-person-rps it will take input_list as empty
		and rounds from 3-person rps to break the die"""

		# if there's an input list it means we're on taylor swift case
		# else case is when the function is called from 3 person fps
		if len(input_list):
			input_list = input_list
		else:
			new_input_list = []
			input_list = new_input_list
			movePlayer1 = input("Player 1's move:")
			input_list.append(movePlayer1)
			movePlayer2 = input("Player 2's move:")
			input_list.append(movePlayer2)
		#iterating over user inputs and comparing them
		for i in range(1):
			if input_list[i] == "Rock":
				if input_list[i+1] == "Paper":
					print(f"Winner is second user")
					rounds = 6
					return rounds, input_list
				elif input_list[i+1] == "Scissors":
					print(f"Winner is first user")
					rounds = 6
					return rounds, input_list

				else:
					print("Tie, everyone will play again")
					rps_2_person(rounds=rounds, input_list=[])
					rounds = rounds + 1

			elif input_list[i] == "Paper":
					if input_list[i+1] == "Paper":
						print("Tie, everyone will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						break

					elif input_list[i+1] == "Scissors":
						print("Winner is second user")
						rounds = 6
						return rounds, input_list
					else:
						print(f"Winner is first user")
						rounds = 6
						return rounds, input_list


			elif input_list[i] == "Scissors":
					if input_list[i+1] == "Paper":
						print(f"Winner is first user")
						rounds = 6
						break

					elif input_list[i+1] == "Scissors":
						print("Tie, everyone will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
					else:
						print(f"Winner is second user")
						rounds = 6
						return rounds, input_list

	def rps_3_person(input_list, rounds):
		""" 3 person rock paper scissors
		if input_list is empty it means there was a tie in 3 person rps
		and the game is restarted, but if it isn't empty,
		it was initialized
		it also takes rounds, if it's just started, rounds will be 0 """

		if input_list == []:
			movePlayer1 = input("Player 1's move:")
			input_list.append(movePlayer1)
			movePlayer2 = input("Player 2's move:")
			input_list.append(movePlayer2)
			movePlayer3 = input("Player 3's move:")
			input_list.append(movePlayer3)
		for i in range(2):

			#first person plays rock	
			if input_list[i] == "Rock":

				#second person plays paper
				if input_list[i+1] == "Paper": 
					#third person plays scissors, paper
					if input_list[i+2] == "Scissors":
						# There's a tie where everyone played a different move
						print("Tie, everyone will play") 
						rounds = rounds + 1
						# we restart the 3 person rps again with rounds and empty list
						rps_3_person(rounds=rounds, input_list=[])
						break


					elif input_list[i+2] == "Paper":
						print("Tie, user 2 and 3 will play")
						rounds = rounds + 1
						# One person is eliminated, two player stays
						# 2 person rps is called with empty list and rounds
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list

					elif input_list[i+2] == "Rock":
						# there's a win, we return rounds and input list
						print("Player 2 wins")
						rounds = 6
						return rounds, input_list


				# second person plays scissor
				elif input_list[i+1] == "Scissors": 
					#third person plays rock, scissors, paper
					if input_list[i+2] == "Scissors":
						print("First person wins")
						rounds = 6
						return rounds, input_list

					elif input_list[i+2] == "Paper":
						print("Tie, everyone will play")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break


					elif input_list[i+2] == "Rock":
						print("Tie, user 1 and 3 will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list


				# second person plays rock
				elif input_list[i+1] == "Rock": 
					#third person plays scissors, paper
					if input_list[i+2] == "Scissors":
						print("User 1 and 2 will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list

					elif input_list[i+2] == "Paper":
						print("Player 3 wins")
						rounds = 6
						return rounds, input_list
					else: 
						print("Tie, everyone will play")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break


			#first person plays paper	
			if input_list[i] == "Paper":

				#second person plays paper
				if input_list[i+1] == "Paper": 
					#third person plays scissors, paper
					if input_list[i+2] == "Scissors":
						print("Player 2 wins")
						rounds = 6
						return rounds, input_list

					elif input_list[i+2] == "Paper":
						print("Tie, user 2 and 3 will play")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list

					elif input_list[i+2] == "Rock":
						print("Tie, everyone will play")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break


				# second person plays scissor
				elif input_list[i+1] == "Scissors": 
					#third person plays rock, scissors, paper
					if input_list[i+2] == "Scissors":
						print("Tie, user 2 and 3 will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list

					elif input_list[i+2] == "Paper":
						print("Second person wins")
						rounds = 6
						return rounds, input_list

					elif input_list[i+2] == "Rock":
						print("Tie, everyone will play again")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break


				# second person plays rock
				elif input_list[i+1] == "Rock": 
					#third person plays scissors, paper
					if input_list[i+2] == Scissors:
						print("Tie, everyone will play")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break

					elif input_list[i+2] == "Paper":
						print("User 1 and 3 will play again")
						rounds = rounds + 1
						rps_2_person()
						return rounds, input_list
					else: 
						print("First person wins")
						rounds = 6
						return rounds, input_list


			#first person plays scissor	
			if input_list[i] == "Scissors":
				#second person plays paper
				if input_list[i+1] == "Paper": 
					#third person plays scissors, paper
					if input_list[i+2] == "Scissors":
						print("Tie, user 1 and 3 will play")
						rounds = rounds + 1
						rps_2_person()
						return rounds, input_list

					elif input_list[i+2] == "Paper":
						print("Player 1 wins")
						rounds = 6
						return rounds, input_list

					elif input_list[i+2] == "Rock":
						print("Tie, everyone will play")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break


				# second person plays scissor
				elif input_list[i+1] == "Scissors": 
					#third person plays rock, scissors, paper
					if input_list[i+2] == "Scissors":
						print("Tie, everyone will play again")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break
						

					elif input_list[i+2] == "Paper":
						print("Tie, user 1 and 2 will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list

					elif input_list[i+2] == "Rock":
						print("Player 3 wins")
						rounds = 6
						return rounds, input_list

				#second player plays rock
				elif input_list[i+1] == "Rock": 
					#third person plays rock, scissors, paper
					if input_list[i+2] == "Scissors":
						print("Player 2 wins")
						rounds = 6
						return rounds, input_list
						
					elif input_list[i+2] == "Paper":
						print("Tie, everyone will play again")
						rounds = rounds + 1
						rps_3_person(rounds=rounds, input_list=[])
						break

					elif input_list[i+2] == "Rock":
						print("Tie, user 2 and 3 will play again")
						rounds = rounds + 1
						rps_2_person(rounds=rounds, input_list=[])
						return rounds, input_list

	if input_list[2] == "Taylor Swift":
		rps_2_person(rounds = 0, input_list = input_list)
	else:
		rps_3_person(input_list, rounds=0)

if __name__=="__main__":
	rps()
