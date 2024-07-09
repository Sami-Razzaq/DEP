player, opponent = "o", "x"
INF = float('inf')

# Converts given input into position on board
def getPos(move):
    if move <= 3:
        return 0, move-1
    elif move <= 6:
        return 1, move-4
    elif move <= 9:
        return 2, move-7

# Checks for moves
def MovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return True
    return False

# Prints the board in a clean shape
def printBoard(board):
    print("")
    for row in board:
        print(" | ".join(row))
    print("")

# Applies Minimax Algorithm
def minimax(board, depth, isMax):
    score = evaluate(board)
    # Maximizer Won
    if score == 10:
        return score
    # Minimizer Won
    if score == -10:
        return score
    # No Moves Left on board, Draw
    if MovesLeft(board) == False:
        return 0

    # Maximizer's Turn
    # Call minimax recursively to choose the maximum value
    # for each move played and then undo the move
    if isMax:
        bestScore = -INF
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = player
                    bestScore = max(bestScore, minimax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return bestScore

    # Minimizer's Turn
    # Call minimax recursively to choose the minimum value
    # for each move played and then undo the move
    else:
        bestScore = INF
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = opponent
                    bestScore = min(bestScore, minimax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return bestScore

# Check which side won
def evaluate(board):
    # Row match
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == player:
                return 10
            elif board[row][0] == opponent:
                return -10

    # Column match
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == player:
                return 10
            elif board[0][col] == opponent:
                return -10

    # Checking for Diagonals for X or O victory.
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:

        if board[0][0] == player:
            return 10
        elif board[0][0] == opponent:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:

        if board[0][2] == player:
            return 10
        elif board[0][2] == opponent:
            return -10

    # Else if none of them have won then return 0
    return 0

# Returns best possible move.
def getBestMove(board):
    bestVal = -INF
    bestMove = (-1, -1)

    # Evaluates move using MinMax.
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = "_"

                # Updates bestVal on basis of current move 
                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal
    return bestMove