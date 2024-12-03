import numpy as np
import pygame
import math
import random
import sys

BOARDWIDTH = 4
BOARDLENGTH = 4
INAROW = 4



board = np.zeros((BOARDLENGTH, BOARDWIDTH))


print(board)

def is_valid_location(y, x):
	return board[y][x] == 0

def check_win(board, piece):
	#Check Horizontal In A Row
	for y in range(BOARDLENGTH):
		if board[y][0] == piece and board[y][1] == piece and board[y][2] == piece and board[y][3] == piece:
			gameOver(piece)

	#Check Vertical In A Column
	for x in range(BOARDWIDTH):
		if board[0][x] == piece and board[1][x] == piece and board[2][x] == piece and board[3][x] == piece:
			gameOver(piece)


	#Check Pos Diagonals
	if board[0][3] == piece and board[1][2] == piece and board[2][1] == piece and board[3][0] == piece: 
		gameOver(piece)


	#Check Neg Diagonals
	if board[0][0] == piece and board[1][1] == piece and board[2][2] == piece and board[3][3] == piece: 
		gameOver(piece)


	#Check Four Corners
	if board[0][0] == piece and board[3][0] == piece and board[0][3] == piece and board[3][3] == piece:
		gameOver(piece)


	#Check 2 by 2 Units
	for y in range(BOARDLENGTH-1):
		for x in range(BOARDWIDTH-1):
			if board[y][x] == piece and board[y][x+1] == piece and board[y+1][x] == piece and board[y+1][x+1] == piece:
				gameOver(piece)

def draw_board():
	for x in range(BOARDWIDTH):
		for y in range(BOARDLENGTH):
			pygame.draw.rect(SCREEN, WHITE, (x*BGSIZE, y*BGSIZE, BGSIZE, BGSIZE))
			pygame.draw.rect(SCREEN, GREY, (x*BGSIZE+5, y*BGSIZE+5, GRIDSIZE, GRIDSIZE))

	for x in range(BOARDWIDTH):
		for y in range(BOARDLENGTH):
			if board[y][x] == 1:
				pygame.draw.rect(SCREEN, BLUE, (x*BGSIZE+5, y*BGSIZE+5, GRIDSIZE, GRIDSIZE))

			if board[y][x] == 2:
				pygame.draw.rect(SCREEN, RED, (x*BGSIZE+5, y*BGSIZE+5, GRIDSIZE, GRIDSIZE))


	pygame.display.update()

def gameOver(p):
	
	for x in range(4):
		for y in range(4):
			pygame.time.wait(50)
			if p == 1:
				pygame.draw.rect(SCREEN, BLUE, (x*BGSIZE+5, y*BGSIZE+5, GRIDSIZE, GRIDSIZE))
			if p == 2:
				pygame.draw.rect(SCREEN, RED, (x*BGSIZE+5, y*BGSIZE+5, GRIDSIZE, GRIDSIZE))
			pygame.display.update()

	print("Player " + str(p) + " wins!")
	
	pygame.time.wait(700)
	sys.exit()

pygame.init()

BGSIZE = 120
GRIDSIZE = 110
SIZE = (BGSIZE*BOARDWIDTH, BGSIZE*BOARDLENGTH)
SCREEN = pygame.display.set_mode(SIZE)

WHITE = (227, 228, 230)
GREY = (210, 211, 214)
BLUE = (41, 73, 166)
RED = (173, 31, 31)

turn = random.randint(0,1)
game_over = False
draw_board()


while not game_over:

	if game_over == True:
		sys.exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:

			if turn == 0:
				print("Player 1's turn:")
				piece = 1
				posx = round((event.pos[0]+50)/BGSIZE)
				posy = round((event.pos[1]+50)/BGSIZE)
				if is_valid_location(posy - 1, posx - 1) == True:
					board[int(posy - 1), int(posx - 1)] = piece
					draw_board()
					check_win(board, 1)
					print(board)

					turn += 1

			if turn == 1:
				print("Player 2's turn:")
				piece = 2
				posx = round((event.pos[0]+50)/BGSIZE)
				posy = round((event.pos[1]+50)/BGSIZE)
				if is_valid_location(posy - 1, posx - 1) == True:
					board[int(posy - 1), int(posx - 1)] = piece
					draw_board()
					check_win(board, 2)
					print(board)

					turn += 1

			turn = turn%2


