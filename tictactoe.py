import random
import json
import random
import math
import pygame
from pygame.locals import *
from GUI import *



board_row = 3
board_col = 3

def hash_state(state):
    return tuple([tuple(t) for t in state])

class TicTacToe:
    def __init__(self, playerX, playerO, row, col,streaks):
        self.row = row
        self.col = col
        self.board = [ [' ' for j in range(0,col)] for i in range(0,row)]
        self.streak = streaks
        self.playerX, self.playerO = playerX, playerO
        self.playerX_turn = random.choice([True,False])
        self.score_x = 0
        self.score_y = 0

    def play_game(self, DISPLAY, board, coords):
        self.playerX.start_game('X',self.row,self.col,self.streak)
        self.playerO.start_game('O',self.row,self.col,self.streak)
        game = True
        while game: #yolo

            if self.playerX_turn:
                turn = "X"
                player, char, other_player = self.playerX, 'X', self.playerO
            else:
                turn = "O"
                player, char, other_player = self.playerO, 'O', self.playerX
            #if player.breed == "human":
            self.display_board()
            ################################
            if self.playerX_turn:
                space_x,space_y = player.move(self.board)
                draw(DISPLAY, board, coords, turn, space_y-1, space_x-1)
                pygame.display.update()
            else:
                findEvent = True
                while findEvent == True:
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            findEvent = False
                            (row, col) = getHumanPos()
                        #    (col, row) = getHumanPos()
                            space_y = row+1
                            space_x = col+1
                            draw(DISPLAY, board, coords, turn, row, col)
                            pygame.display.update()
                        if event.type == pygame.QUIT:
                            findEvent = False
                            game = False
                            pygame.quit()




            #######################################

            if game and self.board[space_x-1][space_y - 1] != ' ': # illegal move
                print("illegal move")
                player.reward(-99, self.board) # score of shame
                continue
            #print "before the move", self.board
            self.board[space_x-1][space_y - 1] = char
            #print "after the move",self.board
            if self.player_wins(char,space_x-1,space_y-1):
                #print "Player win \n"
                #print "winning state the board",self.board
                if char == 'X':
                    self.score_x = 1
                    printResult("X", DISPLAY)
                if char == 'O':
                    self.score_y = 1
                    printResult("O", DISPLAY)
                self.display_board()
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                break
            if self.board_full(): # tie game
                print("tie game")
                printResult("T", DISPLAY)
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                break
            other_player.reward(0, self.board)
            self.playerX_turn = not self.playerX_turn


    def player_wins(self, char,pos_x,pos_y):
        """
            Win Policy will change
        """
        print ("player's char")
        print (char)

        #print "the player's char is",char
        horizontal, vertical, lowerRight, upperRight = 0,0,0,0
        # Horizontal directions
        for i in range(pos_y,-1,-1):
            if self.board[pos_x][i] == char:
                horizontal += 1
            else:
                break

        for i in range(pos_y,self.col):
            if self.board[pos_x][i] == char:
                horizontal += 1
            else:
                break
        print(horizontal)
        print ("horizontal")
        if horizontal == self.streak + 1:
            return True

        #Vertical Directions
        for i in range(pos_x,-1,-1):
            if self.board[i][pos_y] == char:
                vertical += 1
            else:
                break

        for i in range(pos_x,self.row):
            if self.board[i][pos_y] == char:
                vertical += 1
            else:
                break

        print(vertical)
        print("vertical")

        if vertical == self.streak + 1:
            return True

        #lowerRight directions \
        """
            problematic
        """
        j = pos_y
        for i in range(pos_x,-1,-1):
            if i >= 0 and j >= 0:
                if self.board[i][j] == char:
                    lowerRight += 1
                    j -= 1
                else:
                    break;
        j = pos_y
        for i in range(pos_x,self.row):
            if i < self.row and j < self.col:
                if self.board[i][j] == char:
                    lowerRight += 1
                    j += 1
                else:
                    break

        print(lowerRight)
        print("lowerRight")

        if lowerRight == self.streak + 1:
            return True


        #upperRight directions /
        j = pos_y
        for i in range(pos_x,-1,-1):
            if i >= 0 and j < self.col:
                if self.board[i][j] == char:
                    upperRight += 1
                    j += 1
                else:
                    break
        j = pos_y
        for i in range(pos_x,self.row):
            if i < self.row and j >= 0:
                if self.board[i][j] == char:
                    upperRight += 1
                    j -=1
                else:
                    break

        print(upperRight)
        print("upperRight")


        if upperRight == self.streak + 1:
            return True

        return False

    def board_full(self):
        return not any([space == ' ' for row in self.board for space in row])

    def display_board(self):
        """
            Display board will change
        """
        for i in range(0,self.row):
            row = ""
            for j in range(0,self.col):
                row += "|{0}| ".format(self.board[i][j])
            print(row)
    def x_score(self):
        return self.score_x
    def y_score(self):
        return self.score_y

class Player(object):
    def __init__(self):
        self.breed = "human"

    def start_game(self, char,row,col,streak):
        print("\nNew game!")
        #self.board = board

    def move(self, board):
        x = int(input("X coordinate? "))
        y = int(input("Y coordinate? "))
        return (x,y)

    def reward(self, value, board):
        print ("{} rewarded: {}".format(self.breed, value))

    def available_moves(self,board,row,col):
        return [ (i+1,j+1) for i in range(0,row) for j in range(0,col) if board[i][j] == ' ']

class RandomPlayer(Player):
    def __init__(self):
        self.breed = "random"

    def reward(self, value, board):
        print("Random's reward {}".format(value))

    def start_game(self, char, row, col, streak):
        self.me = char
        self.row = row
        self.col = col
        self.streak = streak

    def move(self, board):
        return random.choice(self.available_moves(board, self.row, self.col))

class MinimaxPlayer(Player):
    def __init__(self):
        self.breed = "minimax"
        self.best_moves = {} # board -> moves
        self.last_move_me = ()
        self.last_move_other = ()

    def start_game(self, char,row,col,streak):
        self.me = char
        self.row = row
        self.col = col
        self.enemy = self.other(char)
        self.streak = streak

    def other(self, char):
        return 'O' if char == 'X' else 'X'


    def move(self, board):

        if hash_state(board) in self.best_moves:
            return random.choice(self.best_moves[hash_state(board)])
        if len(self.available_moves(board,self.row,self.col)) == self.row * self.col:
            return random.choice(self.available_moves(board,self.row,self.col))

        best_yet = -2
        choices = []
        for pos_x,pos_y in self.available_moves(board,self.row,self.col):
            board[pos_x-1][pos_y-1] = self.me
            self.last_move_me = (pos_x,pos_y)
            optimal = self.minimax(board, self.enemy, -2, 2) # me is the maximazier
            board[pos_x-1][pos_y-1] = ' '
            if optimal > best_yet:
                choices = [(pos_x,pos_y)]
                best_yet = optimal
            elif optimal == best_yet:
                choices.append((pos_x,pos_y))
        self.best_moves[hash_state(board)] = choices
        return random.choice(choices)

    def minimax(self, board, char, alpha, beta):
        if len(self.last_move_me) > 0 and \
            self.player_wins(self.me, board, self.last_move_me[0]-1,self.last_move_me[1]-1):
            return 1
        if len(self.last_move_other) > 0 and \
            self.player_wins(self.enemy, board,self.last_move_other[0]-1,self.last_move_other[1]-1):
            return -1
        if self.board_full(board):
            return 0
        for pos_x,pos_y in self.available_moves(board,self.row,self.col):
            board[pos_x-1][pos_y-1] = char
            if char == self.me:
                self.last_move_me = (pos_x,pos_y)
            if char == self.other:
                self.last_move_other = (pos_x,pos_y)
            val = self.minimax(board, self.other(char), alpha, beta)
            board[pos_x-1][pos_y-1] = ' '
            if char == self.me:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if char == self.me:
            return alpha
        else:
            return beta

    def player_wins(self, char,board,pos_x,pos_y):
        """
            Win Policy will change
        """

        #print "the player's char is",char
        horizontal, vertical, lowerRight, upperRight = 0,0,0,0
        # Horizontal directions
        for i in range(pos_y,-1,-1):
            if board[pos_x][i] == char:
                horizontal += 1
            else:
                break

        for i in range(pos_y,self.col):
            if board[pos_x][i] == char:
                horizontal += 1
            else:
                break
        if horizontal == self.streak + 1:
            return True

        #Vertical Directions
        for i in range(pos_x,-1,-1):
            if board[i][pos_y] == char:
                vertical += 1
            else:
                break

        for i in range(pos_x,self.row):
            if board[i][pos_y] == char:
                vertical += 1
            else:
                break


        if vertical == self.streak + 1:
            return True

        #lowerRight directions \
        """
            problematic
        """
        j = pos_y
        for i in range(pos_x,-1,-1):
            if i >= 0 and j >= 0:
                if board[i][j] == char:
                    lowerRight += 1
                    j -= 1
                else:
                    break;
        j = pos_y
        for i in range(pos_x,self.row):
            if i < self.row and j < self.col:
                if board[i][j] == char:
                    lowerRight += 1
                    j += 1
                else:
                    break


        if lowerRight == self.streak + 1:
            return True


        #upperRight directions /
        j = pos_y
        for i in range(pos_x,-1,-1):
            if i >= 0 and j < self.col:
                if board[i][j] == char:
                    upperRight += 1
                    j += 1
                else:
                    break
        j = pos_y
        for i in range(pos_x,self.row):
            if i < self.row and j >= 0:
                if board[i][j] == char:
                    upperRight += 1
                    j -=1
                else:
                    break


        if upperRight == self.streak + 1:
            return True

        return False

    def board_full(self, board):
        return not any([space == ' ' for row in board for space in row])

    def reward(self, value, board):
        print("minimax's reward {}".format(value))

class MinimuddledPlayer(MinimaxPlayer):
    def __init__(self, confusion=0.1):
        super(MinimuddledPlayer, self).__init__()
        self.breed = "muddled"
        self.confusion = confusion
        self.ideal_player = MinimaxPlayer()

    def start_game(self, char):
        self.ideal_player.me = char
        self.ideal_player.enemy = self.other(char)

    def move(self, board):
        if random.random() > self.confusion:
            return self.ideal_player.move(board)
        else:
            return random.choice(self.available_moves(board))

class QLearningPlayer(Player):
    def __init__(self, epsilon=0.4, alpha=0.3, gamma=0.9):
        self.breed = "Qlearner"
        self.harm_humans = False
        self.q = {} # (state, action) keys: Q values
        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards

    def start_game(self, char, row,col,streak):
        self.last_board = [ [' ' for j in range(0,col)] for i in range(0,row)]
        self.last_move = None
        self.streak = streak

    def getQ(self, state, action):
        # encourage exploration; "optimistic" 1.0 initial values
        if self.q.get(str((state, action))) is None:
            self.q[str((state, action))] = 1.0
        return self.q.get(str((state, action)))

    def move(self, board):
        self.last_board = hash_state(tuple(board))
        actions = self.available_moves(board,len(board),len(board[0]))

        if random.random() < self.epsilon: # explore!
            self.last_move = random.choice(actions)
            return self.last_move

        qs = [self.getQ(self.last_board, a) for a in actions]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        #print "Q player move return ", actions[i]
        return actions[i]

    def reward(self, value, board):
        if self.last_move:
            #print self.last_board, "last board"
            #print board,"this board"
            self.learn(self.last_board, self.last_move, value, hash_state(tuple(board)))

    def learn(self, state, action, reward, result_state):
        prev = self.getQ(state, action)
        maxqnew = max([self.getQ(result_state, a) for a in self.available_moves(state,len(state),len(state[0]))])
        self.q[str((state, action))] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)
    def getStates(self):
        return self.q
    def setStates(self,qvector):
        self.q = qvector


def main():
    # p1 = RandomPlayer()
    # p1 = MinimaxPlayer()
    # p1 = MinimuddledPlayer()
    p1 = QLearningPlayer()
    p2 = QLearningPlayer()
    p6 = MinimaxPlayer()
    p7 = RandomPlayer()

    # for i in range(0,20):
    #     t = TicTacToe(p1,p2,3,3,3)
    #     t.play_game()

    """
    persist = shelve.open('train.txt')
    try:
        persist['qvalue'] = p1.getStates()
    finally:
        persist.close()
    persist = shelve.open('train.txt', writeback=True)
    try:
        p4.setStates(persist['qvalue'])
    finally:
        persist.close()
    """
    p4 = QLearningPlayer()

    """
    with open('train.txt', 'w') as outfile:
        json.dump(p1.getStates(), outfile)
    """

    with open('train.txt', 'r') as infile:
        p4.setStates(json.load(infile))
    p3 = Player()
    p2.epsilon = 0

    print("reach")

    # x_win,y_win = 0,0
    # for i in range(0,1001):
    #     test = TicTacToe(p4,p7,3,3,3)
    #     test.play_game()
    #     if test.x_score():
    #         x_win += 1
    #     if test.y_score():
    #         y_win += 1

    #####################GUI#######################
    pygame.init()

######## initial board, choose from the three mode
    DISPLAY = pygame.display.set_mode((board_width,board_height))
    pygame.display.set_caption('Tic Tac Toe')

    DISPLAY.blit(board_image, (0,0))
#    DISPLAY.blit(button3_3, (400,230))
    DISPLAY.blit(button33, (150,380))
    DISPLAY.blit(button43, (345,380))
    DISPLAY.blit(button44, (540,380))

    pygame.display.update()

######## choose the type of game that you want to play
# determine the size of the board
    row_of_board = 3   # default value of the board
    col_of_board = 3   # default value of the board

    running = True;
    while running:
        for event in pygame.event.get():
        #     if the player press the mouse down, we need to capture the location of the mouse, if it is in the button's location, we need to jump out from the loop and continue our game.
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x >= 200 and mouse_x <= 360 and mouse_y >= 380 and mouse_y <= 490:
                    row_of_board = 3
                    col_of_board = 3
                #    print("3*3!!!!!")
                    running = False
                    break;
                elif mouse_x >= 395 and mouse_x <= 555 and mouse_y >= 380 and mouse_y <= 490:
                    row_of_board = 3
                    col_of_board = 4
            #        print("4*3!!!!!")
                    running = False
                    break;
                elif mouse_x >= 590 and mouse_x <= 750 and mouse_y >= 380 and mouse_y <= 490:
                    row_of_board = 4
                    col_of_board = 4
                #    print("4*4!!!!!")
                    running = False
                    break;

    board_row = row_of_board
    board_col = col_of_board


########### calculate the position to place the checker
    # board是一个list。长度为m*n，记录borad上现有的棋子，不断更新
    board = [None] * row_of_board * col_of_board
    # coords是一个list，长度为m*n，保存每个格子左上角的坐标，生成以后不变
    coords = []
    ### calculate the location of each checker in different map;
    if row_of_board == 3 and col_of_board == 3:
        coords = [(314,171),(450,171),(592,171),(314,310),(450,310),(592,310),(314,450),(450,450),(592,450)]
    elif row_of_board == 3 and col_of_board == 4:
        coords = [(335,161),(452,161),(569,161),(335,261),(452,261),(569,261),(335,361),(452,361),(569,361),(335,463),(452,463),(569,463)]
    elif row_of_board == 4 and col_of_board == 4:
        coords = [(296,162),(401,162),(502,162),(602,162),(296,262),(401,262),(502,262),(602,262),(296,358),(401,358),(502,358),(602,358),(296,465),(401,465),(502,465),(602,465)]

#    for row in range(0, row_of_board):
#        for col in range(0, col_of_board):
#            coords.append((row * board_width / row_of_board, col * board_height / col_of_board))

########### starting the real game scene!

    if row_of_board == 4 and col_of_board == 4:
        num_of_streaks = 4
    else:
        num_of_streaks = 3

    new_game = TicTacToe(p4,p3,row_of_board,col_of_board,num_of_streaks) # board size需要获取 # 规定humanplayer必须在后面
    #erase the surface
    DISPLAY.fill((0,0,0))
    # try to figure out which play game scence should be used.
    # the game image that we are going to play on:
    if row_of_board == 3 and col_of_board == 3:
        board_game_image = board_image33
    elif row_of_board == 3 and col_of_board == 4:
        board_game_image = board_image43
    elif row_of_board == 4 and col_of_board == 4:
        board_game_image = board_image44

    DISPLAY.blit(board_game_image, (0,0))
    pygame.display.update()

    new_game.play_game(DISPLAY, board, coords)

    running = True
    while running:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]: # 按空格重开一局
            DISPLAY.blit(board_game_image, (0,0)) # 覆盖一层背景，重开一局
            pygame.display.update()
            board = [None] * row_of_board * col_of_board
            new_game = TicTacToe(p4,p3,row_of_board,col_of_board,num_of_streaks) # board size需要获取
            new_game.play_game(DISPLAY, board, coords)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        # clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
