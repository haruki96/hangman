import random

def hangman(word):
	wrong = 0
	stages = ["",
			  "_________        ",
			  "|        |       ",
			  "|        |       ",
			  "|        O       ",
			  "|       -|-      ",
			  "|       / L      ",
			  "|                "
			  ]
	rletters = list(word)
	board = ["_"] * len(word)
	win = False
	print("Welcome to hangman!")
	print("\n")

	######hint######
	if choice in list_animals:
		hint = "hint:animal"
		print(hint)
	if choice in list_sports:
		hint ="hint:sports"
		print(hint)

	print(" ".join(board))
	################

	while wrong	< len(stages) - 1:
		print("\n")
		msg = "Anticipate a character."
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		
		print(" ".join(board))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "_" not in board:
			print("You win!")
			print(" ".join(board))
			win = True
			break

	if not win:
		print("\n".join(stages[0:wrong+1]))
		print("You lose! The answer is {}.".format(word))


list_animals = ["cat", "dog", "fish", "bird"]
list_sports = ["soccer", "baseball", "swimming", "basketball", "golf"]
words_list = [list_animals, list_sports]

x = []
for s in words_list:
    x.extend(s)

choice = random.choice(x)
hangman(choice)

