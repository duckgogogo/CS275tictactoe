import random
import math
import pygame
from pygame.locals import *
from tictactoe import *

# board图片的size，如果更换图片需要改这里
board_width = 960
board_height = 640


X_image = pygame.image.load("X.png")
O_image = pygame.image.load("O.png")

####### initialize board #######
board_image = pygame.image.load("initial_board.jpg")
button33 = pygame.image.load("3_3.png")
button43 = pygame.image.load("4_3.png")
button44 = pygame.image.load("4_4.png")

####### game scene three game scene ######
board_image33 = pygame.image.load("3_3map.jpg")
board_image43 = pygame.image.load("4_3map.jpg")
board_image44 = pygame.image.load("4_4map.jpg")

####### game result show
game_Owin = pygame.image.load("Owin.jpg")
game_Xwin = pygame.image.load("Xwin.jpg")
game_tie = pygame.image.load("tie.jpg")


# row和col应该由界面获取读入，暂时没做
# board_row = 3
# board_col = 3

X = "X"
O = "O"

########################################################################

#def draw(DISPLAY, board, coords, turn, row, col): # 每次下一个棋子的时候调用，turn是”X“或者”O“，char类型
def draw(DISPLAY, board, coords, turn, row, col):
	print("row: ", row, "col: ", col)
	print("row*board_col + col")
	# print("board in draw", board)
	if board[row*board_col+col] == None:
		board[row*board_col+col] = turn
		# print("pos: ", row, col)
		print(coords[row*board_col+col])
		if turn == X:
			DISPLAY.blit(X_image, (coords[row*board_col+col]))
		if turn == O:
			DISPLAY.blit(O_image, (coords[row*board_col+col]))


def getHumanPos(): # 获取到click时调用，计算棋子位置，返回的row时0到m-1，col时0到n-1
	X, Y = pygame.mouse.get_pos()
	#print("The position we have is: row: ", Y, "col: ", X)
	if board_row == 3 and board_col == 3:
		print("It is 3*3!!!!!")
		if X >= 279 and X <= 404 and Y >= 147 and Y <= 262:
			row = 0
			col = 0
		elif X > 404 and X <= 544 and Y >= 147 and Y <= 262:
			row = 0
			col = 1
		elif X > 544 and X <= 679 and Y >= 147 and Y <= 262:
			row = 0
			col = 2
		elif X >= 279 and X <= 404 and Y > 262 and Y <= 410:
			row = 1
			col = 0
		elif X > 404 and X <= 544 and Y > 262 and Y <= 410:
			row = 1
			col = 1
		elif X > 544 and X <= 679 and Y > 262 and Y <= 410:
			row = 1
			col = 2
		elif X >= 279 and X <= 404 and Y > 410 and Y <= 547:
			row = 2
			col = 0
		elif X > 404 and X <= 544 and Y > 410 and Y <= 547:
			row = 2
			col = 1
		elif X > 544 and X <= 679 and Y > 410 and Y <= 547:
			row = 2
			col = 2
	else:
		row = 1
		col = 1
	return (row, col)


def printResult(turn, DISPLAY): # 显示结果，字体的位置与大小需要改
	print("Player ", turn, "win!")
	# myfont = pygame.font.SysFont("monospace", 30)

	# render text
	if turn == "X":
		DISPLAY.blit(game_Xwin, (0,0))
	elif turn == "O":
		DISPLAY.blit(game_Owin, (0,0))
	else:
		DISPLAY.blit(game_tie, (0,0))
	pygame.display.update()
	#DISPLAY.blit(result, (0, board_width/2-40))
#	info = myfont.render("Press space to restart!", 1, (255,0,0))
#	DISPLAY.blit(info, (0, board_width/2))
