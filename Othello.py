import copy
from graphics import *
from math import *
from time import *
from random import *

depth = 1
n = 8
com = 0
opp = 0


class Board:
    board = []
    rows = 0
    cols = 0
    player = True

    def initializeBoard(self, r, c):
        for i in range(0, r):
            new = []
            for j in range(0, c):
                new.append(0)
            self.board.append(new)

    def inputValue(self):
        if (self.player == True):
            r = int(input())
            c = int(input())
            self.board[r][c] = "B"
        else:
            r = int(input())
            c = int(input())
            self.board[r][c] = "W"
        return r, c

    def printBoard(self):
        comScore = 0
        oppScore = 0
        for k in range(0, n):
            print(k, end=" ")
        print()
        for i in range(0, n):
            for j in range(0, n):
                print(self.board[i][j], end=" ")
                if (self.board[i][j] == "B"):
                    comScore = comScore + 1
                elif self.board[i][j] == "W":
                    oppScore = oppScore + 1
            print("-", i)
        print("Computer Score: ", comScore)
        print("Opponent Score: ", oppScore)
        com = comScore
        opp = oppScore


minEvalBoard = -1  # min - 1
maxEvalBoard = 82  # max + 1


def evaluationFunction(board, player):
    total = 0
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if board[i][j] == "B" and player == True:
                if (i == 0 or i == n - 1) and (j == 0 or j == n - 1):
                    total += 4  # corner
                elif (i == 0 or i == n - 1) or (j == 0 or j == n - 1):
                    total += 2  # side
                else:
                    total += 1
    return total


def evaluationFunction2(board):
    black = 0
    white = 0
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if board[i][j] == "B":
                black += 1
            if (board[i][j] == "W"):
                white += 1

    return black - white


def check(board, ri, ci, player):
    if player == True:
        tile = "B"
    else:
        tile = "W"
    i = ri - 1
    j = ci
    while (isInsideBoard(i, j)):  # up
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        i = i - 1
    i = ri - 1
    j = ci - 1
    while (isInsideBoard(i, j)):  # up left
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        i = i - 1
        j = j - 1
    i = ri
    j = ci - 1
    while (isInsideBoard(i, j)):  # left
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        j = j - 1
    i = ri + 1
    j = ci - 1
    while (isInsideBoard(i, j)):  # down left
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        i = i + 1
        j = j - 1
    i = ri + 1
    j = ci
    while (isInsideBoard(i, j)):  # down
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        i = i + 1
    i = ri + 1
    j = ci + 1
    while (isInsideBoard(i, j)):  # down right
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        i = i + 1
        j = j + 1
    i = ri
    j = ci + 1
    while (isInsideBoard(i, j)):  # rifht
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        j = j + 1
    i = ri - 1
    j = ci + 1
    while (isInsideBoard(i, j)):  # up right
        if (board[i][j] == tile):
            return True
        if (board[i][j] == tile):
            return False
        i = i - 1
        j = j + 1
    return False


def isValidMove(board, ri, ci, player):
    if (player == True):
        tile = "W"
    else:
        tile = "B"
    if ((ri == 0 and ci == 0) and board[ri][ci] == 0 and (
            board[ri + 1][ci] == tile or board[ri + 1][ci + 1] == tile or board[ri][ci + 1] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ci == 0 and ri != 0 and ri != n - 1) and board[ri][ci] == 0 and (
            board[ri + 1][ci] == tile or board[ri + 1][ci + 1] == tile or board[ri][ci + 1] == tile or board[ri - 1][
        ci + 1] == tile or board[ri - 1][ci] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ri == n - 1 and ci == 0) and board[ri][ci] == 0 and (
            board[ri][ci + 1] == tile or board[ri - 1][ci + 1] == tile or board[ri - 1][ci] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ri == n - 1 and ci != 0 and ci != n - 1) and board[ri][ci] == 0 and (
            board[ri][ci + 1] == tile or board[ri - 1][ci + 1] == tile or board[ri - 1][ci] == tile or board[ri][
        ci - 1] == tile or board[ri - 1][ci - 1] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ri == n - 1 and ci == n - 1) and board[ri][ci] == 0 and (
            board[ri - 1][ci] == tile or board[ri - 1][ci - 1] == tile or board[ri][ci - 1] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ci == n - 1 and ri != 0 and ri != n - 1) and board[ri][ci] == 0 and (
            board[ri + 1][ci] == tile or board[ri + 1][ci - 1] == tile or board[ri][ci - 1] == tile or board[ri - 1][
        ci - 1] == tile or board[ri - 1][ci] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ri == 0 and ci == n - 1) and board[ri][ci] == 0 and (
            board[ri][ci - 1] == tile or board[ri + 1][ci - 1] == tile or board[ri + 1][ci] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ri == 0 and ci != 0 and ci != n - 1) and board[ri][ci] == 0 and (
            board[ri][ci + 1] == tile or board[ri + 1][ci + 1] == tile or board[ri + 1][ci] == tile or board[ri][
        ci - 1] == tile or board[ri][ci - 1] == tile)):
        if check(board, ri, ci, player):
            return True
    elif ((ri != 0 and ri != n - 1 and ci != 0 and ci != n - 1) and board[ri][ci] == 0 and (
            board[ri + 1][ci] == tile or board[ri + 1][ci + 1] == tile or board[ri][ci + 1] == tile or board[ri - 1][
        ci + 1] == tile or board[ri - 1][ci] == tile or board[ri - 1][ci - 1] == tile or board[ri + 1][
                ci - 1] == tile or board[ri][ci - 1] == tile)):
        if check(board, ri, ci, player):
            return True
    return False


def move(board, x, y, player):
    array = copy.deepcopy(board)
    if player == False:
        colour = "W"
    else:
        colour = "B"
    array[x][y] = colour
    # Determining the neighbours to the square
    neighbours = []
    for i in range(max(0, x - 1), min(x + 2, 8)):
        for j in range(max(0, y - 1), min(y + 2, 8)):
            if array[i][j] != None:
                neighbours.append([i, j])

    # Which tiles to convert
    convert = []
    # For all the generated neighbours, determine if they form a line
    # If a line is formed, we will add it to the convert array
    for neighbour in neighbours:
        neighX = neighbour[0]
        neighY = neighbour[1]
        # Check if the neighbour is of a different colour - it must be to form a line
        if array[neighX][neighY] != colour:
            # The path of each individual line
            path = []
            # Determining direction to move
            deltaX = neighX - x
            deltaY = neighY - y

            tempX = neighX
            tempY = neighY

            # While we are in the bounds of the board
            while 0 <= tempX <= n - 1 and 0 <= tempY <= n - 1:
                path.append([tempX, tempY])
                value = array[tempX][tempY]
                # If we reach a blank tile, we're done and there's no line
                if value == 0:
                    break
                # If we reach a tile of the player's colour, a line is formed
                if value == colour:
                    # Append all of our path nodes to the convert array
                    for node in path:
                        convert.append(node)
                    break
                # Move the tile
                tempX += deltaX
                tempY += deltaY

    # Convert all the appropriate tiles
    for node in convert:
        array[node[0]][node[1]] = colour
    return array


def isTerminalNode(board, player):
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if isValidMove(board, i, j, player):
                return False
    return True


def minmax(board, player, depth, isMax):
    if depth == 0 or isTerminalNode(board, player):
        return evaluationFunction2(board)
    if isMax:
        bestValue = minEvalBoard
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                if (isValidMove(board, i, j, player)):
                    boardTemp = move(copy.deepcopy(board), i, j, player)
                    v = minmax(boardTemp, player, depth - 1, False)
                    bestValue = max(bestValue, v)
    else:  # minimizingPlayer
        bestValue = maxEvalBoard
        for i in range(0, n - 1):
            for j in range(0, n - 1):
                if isValidMove(board, i, j, player):
                    boardTemp = move(copy.deepcopy(board), i, j, player)
                    v = minmax(boardTemp, player, depth - 1, True)
                    bestValue = min(bestValue, v)
    return bestValue


def bestMove(board, player):
    ri = -1
    ci = -1
    max = -9999
    val = 0
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            # tilesToTurn=isValidMove2(board,i,j,player)
            if isValidMove(board, i, j, player):
                tempboard = move(copy.deepcopy(board), i, j, player)
                val = minmax(tempboard, player, depth, True)
            if val > max:
                max = val
                ri = i
                ci = j
    board[ri][ci] = "B"
    return ri, ci


def isValidMove2(board, ri, ci, player):
    if (board[ri][ci] != 0 or isInsideBoard(ri, ci)) == False:
        return False
    if (player == True):
        tile = "B"
    else:
        tile = "W"
    board[ri][ci] = tile
    if tile == 'B':
        againstTile = 'W'
    else:
        againstTile = 'B'

    tilesToTurn = []
    for r_dir, c_dir in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        r, c = ri, ci
        r += r_dir
        c += c_dir
        if isInsideBoard(r, c) and board[r][c] == againstTile:
            r += r_dir
            c += c_dir
            if not isInsideBoard(r, c):
                continue
            while board[r][c] == againstTile:
                r += r_dir
                c += c_dir
                if not isInsideBoard(r, c):
                    break
            if not isInsideBoard(r, c):
                continue
            if board[r][c] == tile:
                while True:
                    r -= r_dir
                    c -= c_dir
                    if r == ri and c == ci:
                        break
                    tilesToTurn.append([r, c])

    board[ri][ci] = 0
    if len(tilesToTurn) == 0:
        return False
    else:
        return True


def isInsideBoard(x, y):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    else:
        return False


def drawBoard(win, board, n, winSize):
    factor = winSize / n
    x = 0
    y = 0
    for i in range(0, n):
        for j in range(0, n):
            rect = Rectangle(Point(x, y), Point(x + factor, y + factor))
            if (board[i][j] == "B"):
                rect.setFill(color_rgb(10, 10, 10))
                # sleep(1)
            elif (board[i][j] == "W"):
                rect.setFill(color_rgb(255, 255, 255))
                # sleep(1)
            else:
                rect.setFill(color_rgb(255, 0, 0))
            rect.draw(win)
            x = x + factor
        x = 0
        y = y + factor
    return win


def move2(board, tilesToTurn, player):
    if (player == True):
        tile = "B"
    else:
        tile = "W"
    for x, y in tilesToTurn:
        board[x][y] = tile
    return board


def main():
    game = Board()
    game.initializeBoard(n, n)
    game.board[3][3] = "B"
    game.board[3][4] = "W"
    game.board[4][4] = "B"
    game.board[4][3] = "W"
    game.player = True
    flag = True
    win = GraphWin("Othello", 640, 800)
    factor = 640 / n
    r = 0
    c = 0
    while (flag):
        if (isTerminalNode(game.board, game.player)):
            if (com > opp):
                print("Winner Is Computer.")
            elif opp > com:
                print("Winner is Opponent.")
            else:
                print("Tied.")
            flag = False
        if (game.player == True):
            ri, ci = bestMove(game.board, game.player)
            if not (ri == -1 and ci == -1):
                game.board = move(game.board, ri, ci, game.player)
                game.board = move(game.board, ri, ci, game.player)
                print("After Computer Turn:")
                game.printBoard()
                win = drawBoard(win, game.board, n, 640)
        else:
            print("User Turn")

            point = win.getMouse()
            x = point.getX()
            y = point.getY()
            c = int(x / factor)
            r = int(y / factor)

            while (isValidMove(game.board, r, c, game.player) == False):
                print("Wrong Move. Enter the input again")
                point = win.getMouse()
                x = point.getX()
                y = point.getY()
                c = int(x / factor)
                r = int(y / factor)
            game.board = move(game.board, r, c, game.player)
            game.printBoard()
            win = drawBoard(win, game.board, n, 640)
        game.player = not game.player


if __name__ == "__main__":
    main()
