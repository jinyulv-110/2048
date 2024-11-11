import pygame, sys, random
from pygame.locals import *

winwidth = 600
winheight = 600
snow = (205, 201, 201)
framecolor = (139, 137, 137)
black = (0, 0, 0)
blocksize = 90
boardsize = 4
margin_x = int((winwidth - blocksize * boardsize) / 2)
margin_y = int((winheight - blocksize * boardsize) / 2)
direction = 0

pygame.init()
screen = pygame.display.set_mode((winwidth, winheight))
pygame.display.set_caption('2048')
numfont = pygame.font.Font(None, 50)
fpsclock = pygame.time.Clock()
fps = 30


def get_newboard():
    newboard = []
    for y in range(boardsize):
        newboard.append([])
        for x in range(boardsize):
            newboard[y].append(0)
    return newboard


def draw_block(x, y):
    blockrect = pygame.Rect(margin_x + x * blocksize + 1, margin_y + y * blocksize + 1, blocksize - 2, blocksize - 2)
    pygame.draw.rect(screen, (205, 79, 57 + board[y][x]), blockrect)
    numfontsurface = numfont.render(str(board[y][x]), True, black)
    numfontrect = numfontsurface.get_rect()
    numfontrect.center = blockrect.center
    screen.blit(numfontsurface, numfontrect)


def draw_board(board):
    boardframerect = pygame.Rect(margin_x - 3, margin_y - 3, blocksize * boardsize + 6, blocksize * boardsize + 6)
    pygame.draw.rect(screen, framecolor, boardframerect, 3)
    for y in range(boardsize):
        for x in range(boardsize):
            if board[y][x] != 0:
                draw_block(x, y)


def add_newnum(board, direction):
    randnum = random.randint(1, 2) * 2
    if direction == 1:
        optionalcolumns = []
        for x in range(boardsize):
            if board[boardsize - 1][x] == 0:
                optionalcolumns.append(x)
        chosecolumn = random.choice(optionalcolumns)
        for y in range(boardsize):
            if board[y][chosecolumn] == 0:
                board[y][chosecolumn] = randnum
                break
    elif direction == 2:
        optionalcolumns = []
        for x in range(boardsize):
            if board[0][x] == 0:
                optionalcolumns.append(x)
        chosecolumn = random.choice(optionalcolumns)
        for y in range(boardsize - 1, -1, -1):
            if board[y][chosecolumn] == 0:
                board[y][chosecolumn] = randnum
                break
    elif direction == 3:
        optionalrows = []
        for y in range(boardsize):
            if board[y][boardsize - 1] == 0:
                optionalrows.append(y)
        choserow = random.choice(optionalrows)
        for x in range(boardsize):
            if board[choserow][x] == 0:
                board[choserow][x] = randnum
                break
    elif direction == 4:
        optionalrows = []
        for y in range(boardsize):
            if board[y][0] == 0:
                optionalrows.append(y)
        choserow = random.choice(optionalrows)
        for x in range(boardsize - 1, -1, -1):
            if board[choserow][x] == 0:
                board[choserow][x] = randnum
                break


def move_allnum(board, direction):
    moved = False
    if direction == 1:
        for x in range(boardsize):
            added = False
            for y in range(boardsize):
                if board[y][x] != 0 :
                    for yy in range(y - 1, -1, -1):
                        if board[yy][x] == board[y][x] and added == False:
                            board[yy][x] *= 2
                            board[y][x] = 0
                            moved = True
                            added = True
                            break
                        if board[yy][x] != board[y][x] and board[yy][x] != 0:
                            if yy + 1 != y:
                                board[yy + 1][x] = board[y][x]
                                board[y][x] = 0
                                moved = True
                            break
                        if yy == 0 and board[yy][x] == 0:
                            board[yy][x] = board[y][x]
                            board[y][x] = 0
                            moved = True
    elif direction == 2:
        for x in range(boardsize):
            added = False
            for y in range(boardsize - 1, -1, -1):
                if board[y][x] != 0 :
                    for yy in range(y + 1, boardsize):
                        if board[yy][x] == board[y][x] and added == False:
                            board[yy][x] *= 2
                            board[y][x] = 0
                            moved = True
                            added = True
                            break
                        if board[yy][x] != board[y][x] and board[yy][x] != 0:
                            if yy - 1 != y:
                                board[yy - 1][x] = board[y][x]
                                board[y][x] = 0
                                moved = True
                            break
                        if yy == boardsize - 1 and board[yy][x] == 0:
                            board[yy][x] = board[y][x]
                            board[y][x] = 0
                            moved = True
    elif direction == 3:
        for y in range(boardsize):
            added = False
            for x in range(boardsize):
                if board[y][x] != 0 :
                    for xx in range(x - 1, -1, -1):
                        if board[y][xx] == board[y][x] and added == False:
                            board[y][xx] *= 2
                            board[y][x] = 0
                            moved = True
                            added = True
                            break
                        if board[y][xx] != board[y][x] and board[y][xx] != 0:
                            if xx + 1 != x:
                                board[y][xx + 1] = board[y][x]
                                board[y][x] = 0
                                moved = True
                            break
                        if xx == 0 and board[y][xx] == 0:
                            board[y][xx] = board[y][x]
                            board[y][x] = 0
                            moved = True
    elif direction == 4:
        for y in range(boardsize):
            added = False
            for x in range(boardsize - 1, -1, -1):
                if board[y][x] != 0:
                    for xx in range(x + 1, boardsize):
                        if board[y][xx] == board[y][x] and added == False:
                            board[y][xx] *= 2
                            board[y][x] = 0
                            moved = True
                            added = True
                            break
                        if board[y][xx] != board[y][x] and board[y][xx] != 0:
                            if xx - 1 != x:
                                board[y][xx - 1] = board[y][x]
                                board[y][x] = 0
                                moved = True
                            break
                        if xx == boardsize - 1 and board[y][xx] == 0:
                            board[y][xx] = board[y][x]
                            board[y][x] = 0
                            moved = True
    return moved


board = get_newboard()
randnum = random.randint(1, 2) * 2
randx = random.randint(0, boardsize - 1)
randy = random.randint(0, boardsize - 1)
board[randy][randx] = randnum

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                direction = 1
                ismoved = move_allnum(board, direction)
                if ismoved:
                    add_newnum(board, direction)
            if event.key == K_DOWN or event.key == K_s:
                direction = 2
                ismoved = move_allnum(board, direction)
                if ismoved:
                    add_newnum(board, direction)
            if event.key == K_LEFT or event.key == K_a:
                direction = 3
                ismoved = move_allnum(board, direction)
                if ismoved:
                    add_newnum(board, direction)
            if event.key == K_RIGHT or event.key == K_d:
                direction = 4
                ismoved = move_allnum(board, direction)
                if ismoved:
                    add_newnum(board, direction)

    screen.fill(snow)
    draw_board(board)
    pygame.display.update()
    fpsclock.tick(fps)

