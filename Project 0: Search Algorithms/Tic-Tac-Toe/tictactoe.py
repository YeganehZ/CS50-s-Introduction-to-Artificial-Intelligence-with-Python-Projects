"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    number_of_Empty=sum(E.count(EMPTY) for E in board)    
    print(number_of_Empty)
    if (number_of_Empty %2)==0:
        return O
    else:
        return X         

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    positions_of_Empty=[]
    row=0
    for E in board:
        for col, value in enumerate(E):
            if value== EMPTY:
                 positions_of_Empty.append((row,col))        
        row +=1
    
    if  positions_of_Empty== []:
        return None 
    else:
        return positions_of_Empty

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy=copy.deepcopy(board)    
    if action not in actions(board):
        raise Exception("Invalid action")
    else:
        action_row=action[0]
        action_col=action[1]
        if player(board_copy) == X:
            board_copy[action_row][action_col] = X
        else: 
            board_copy[action_row][action_col] = O   

        return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]
    
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    
    for i in range(len(board)):
        vertical=[]
        for j in range(len(board)):
            vertical.append(board[j][i])
        if len(set(vertical))==1:
            return vertical[0]
    
    return None



    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    elif actions(board) == None:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)== X:
        return 1
    elif winner(board)== O:
        return -1
    else:
        return 0

    
def max_value(board):
    if terminal(board):
        return utility(board)
       
    v=-math.inf
    for action in actions(board):
        v=max(v,min_value(result(board,action)))
    return v


def min_value(board):   
    if terminal(board):
        return utility(board)
       
    v=math.inf
    for action in actions(board):
        v=min(v,max_value(result(board,action)))
    return v

def minimax(board):

    if terminal(board):
        return None
    
    if player(board)==X:
        possible_sets=[]

        for action in actions(board):
            score=min_value(result(board,action))
            move=action
            possible_sets.append([score,move])
        best_move=sorted(possible_sets, key=lambda x: x[0], reverse=True)[0][1]
        return best_move

    elif player(board)==O:
        possible_sets=[]

        for action in actions(board):            
            score=max_value(result(board,action))
            move=action
            possible_sets.append([score,move])
        best_move=sorted(possible_sets, key=lambda x: x[0])[0][1]
        return best_move






'''
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    else:
        return random.choice(actions(board))


    raise NotImplementedError

def minimax(board):
    Bestscore = -math.inf

    
    for actio in actions(board):
        board_copy=copy.deepcopy(board)    
        Score_F = FindBestScore(result(board,actio),0, False)
        board=board_copy
        if Score_F > Bestscore:
            Bestscore = Score_F
            Bestmove = actio
    
    return Bestmove


def FindBestScore(board,depth,isMaximizng):

    if terminal(board):
        return utility(board)
    
    if isMaximizng:
        best_score=-math.inf
        for act in actions(board):
            score=FindBestScore(result(board,act),depth+1, False)
            best_score=max(score,best_score)       
        return best_score
    
    else:
        best_score=math.inf
        for acti in actions(board):
            score=FindBestScore(result(board,acti),depth+1,True)
            best_score=min(score,best_score)       
        return best_score
    






'''