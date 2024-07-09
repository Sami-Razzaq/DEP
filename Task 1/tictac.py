from func import getPos, MovesLeft, printBoard, evaluate, getBestMove
from copy import deepcopy
from pdb import set_trace

# Here the player is the computer AI while
# the opponent is the human playing the game.
# The algorithm analyzes the human's move
# and plays the best possible move in return.

def main():
    clean_board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]
    
    move = 0
    board = deepcopy(clean_board)  # Makes copy so original doesn't change
    print("Enter the Move from 1 to 9 corresponding to position board.")
    print("To Clear Board, type 0.")

    while True:
        move = int(input("Enter Your Move: "))

        # Loops until valid input is given
        while (move == 0 or move > 9):
            if move > 9:
                print("Enter valid value from 1 to 9")
            # Clears the board - Resets Game
            if move == 0:
                board = deepcopy(clean_board)
                print("Board Cleared\n")
                printBoard(board)
            move = int(input("Enter Your Move: "))

        # Plays the user given move
        pR, pC = getPos(move)
        if board[pR][pC] == '_':
            board[pR][pC] = 'x'
        else:
            print("Invalid Move")
            break
        print("Your Move:")
        printBoard(board)

        # Plays the AI calculated move
        opR, opC = getBestMove(board)
        if board[opR][opC] == '_':
            board[opR][opC] = 'o'
        print("Opponent's Move:")
        printBoard(board)

        # Checks each loop if any side has won or there is Draw
        if evaluate(board) == 10:
            print("o wins")
            break
        if evaluate(board) == -10:
            print("x wins")
            break
        if not MovesLeft(board):
            print("No Moves Left\nDraw")
            break

    print("Game Over")


main()