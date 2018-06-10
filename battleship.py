from random import randint

board = []
large_board = []
small_board = []

for x in range(0, 5):
	large_board.append(["O"] * 5)
	board.append(["O"] * 5)
	small_board.append(["O"] * 5)

def print_board(board):
	for row in board:
		print(" ".join(row))

def large_battleship(board):
	x = randint(0,4)
	for i in range(0,4): 	
		board[x][i] = "X"
	

def small_battleship(board):
	x = randint(0,3)
	for i in range(0,3): 
		board[i][x] = "X" 
		
large_battleship(large_board)
small_battleship(small_board)

print_board(board)
print(" ")
print_board(large_board)
print(" ")
print_board(small_board)



for turn in range(10):
	guess_row =  int(input("Guess Row: "))
	guess_col =  int(input("Guess Column: "))
	board[guess_row][guess_col] = "X"
	print_board(board)
	if board == large_board:
		print("You sank the large battleship!")
	elif board == small_board:
		print("You sank the small battleship!")
	elif board == large_board and board == small_board:
		print("You won!")
		break
	else:
		print("Turn ", turn  + 1)