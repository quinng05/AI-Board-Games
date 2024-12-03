import numpy as np
import pygame
import sys
import math

GREY = (159, 186, 191)
BLACK = (47, 55, 56)
P1COLOR = (38, 77, 148)
P2COLOR = (59, 128, 128)
ROW_COUNT = 6
COL_COUNT = 7

def create_board():
	board = np.zeros((ROW_COUNT, COL_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT - 1][col] == 0

def get_next_open_row (board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

def winning_move(board, piece):
	#Check horizontal locations for winning pattern
	for c in range(COL_COUNT - 3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == board[r][c + 3] == piece:
				return True

	#Check verticals
	for c in range(COL_COUNT):
		for r in range(ROW_COUNT - 3):
			if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == board[r + 3][c] == piece:
				return True

	#Check positive diagonals
	for c in range(COL_COUNT - 3):
		for r in range(ROW_COUNT - 3):
			if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == board[r + 3][c + 3] == piece:
				return True

	#Check negative diagonals
	for c in range(COL_COUNT - 3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == board[r - 3][c + 3] == piece:
				return True


def draw_board(board):
	for c in range(COL_COUNT):
		for r in range (ROW_COUNT):
			pygame.draw.rect(screen, GREY, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
			
	for c in range(COL_COUNT):
		for r in range (ROW_COUNT):
			if board[r][c] == 1:
					pygame.draw.circle(screen, P1COLOR, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2:
					pygame.draw.circle(screen, P2COLOR, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)

	pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100
RADIUS = (SQUARESIZE/2 - 7)

width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()


while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			# print(event.pos)

			# Ask for player 1 input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece (board, row, col, 1)

					if winning_move(board, 1):
						print("Player 1 Wins!")
						game_over = True

			# #Ask for player 2 input
			else:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece (board, row, col, 2)

					if winning_move(board, 2):
						print("Player 2 Wins!")
						game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2
