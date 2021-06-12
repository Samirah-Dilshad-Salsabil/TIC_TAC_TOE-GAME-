import pygame, sys
import numpy as np
pygame.init()

Line_color = (11,30,51)
Circle_color =(245,162,1)
Circle_radius = 60
Circle_width = 10
Cross_color = (155,191,72)
Cross_width = 15
Gape = 55

#sreen size
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("TIC TAC TOE")
#screen color
screen.fill((0,83,122))

#backgroung music
soundObj = pygame.mixer.Sound("background.wav")
soundObj.play()
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.stop()

#Setting no of rows and column
board = np.zeros((3,3))

def draw_lines ():
    pygame.draw.line(screen, Line_color, (0,200), (600,200), 10)

    pygame.draw.line(screen, Line_color, (0,400), (600,400), 10)

    pygame.draw.line(screen, Line_color, (200,0), (200,600), 10)

    pygame.draw.line(screen, Line_color, (400,0), (400,600), 10)

def draw_figures ():
    for row in range(3):
        for col in range (3):
            if board[row][col] == 1:
                pygame.draw.circle(screen,Circle_color,(int( col*200+100),int(row*200+100)),Circle_radius,Circle_width)
            elif board[row][col] == 2:
                pygame.draw.line(screen,Cross_color,(col*200+Gape,row*200+200-Gape),(col*200+200-Gape,row*200+Gape),Cross_width)
                pygame.draw.line(screen,Cross_color,(col*200+Gape,row*200+Gape),(col*200+200-Gape,row*200+200-Gape),Cross_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row,col):
    return   board[row][col] == 0

def is_board_full():
    for row in range(3):
        for col in range (3):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range (3):
        if board[0][col] == player and board [1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range (3):
        if board[row][0] == player and board [row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line( row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board [2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = Circle_color

    elif player == 2:
        color = Cross_color
    pygame.draw.line(screen, color, (posX, 15), (posX, 600 - 15), 15 )

def draw_horizontal_winning_line(row, player):
    posY = row* 200 +100
    if player == 1:
        color = Circle_color
    elif player ==2:
        color = Circle_color
    pygame.draw.line(screen, color, (15, posY) , (600 - 15 ,posY ) , 15 )

def draw_asc_diagonal(player):
    if player == 1:
        color = Circle_color
    elif player ==2:
        color = Circle_color
    pygame.draw.line(screen, color, (15,600- 15),(600- 15 , 15), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = Circle_color
    elif player == 2:
        color = Circle_color
    
    pygame.draw.line(screen, color, (15,15), (600 - 15 ,600 - 15), 15)

def restart():
    screen.fill((0,83,122))
    draw_lines()
    player = 1

    for row in range (3):
        for col in range (3):
            board[row][col] = 0
    
draw_lines()
player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] 
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col) :
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win (player):
                        game_over = True
                    player = 2

                elif player == 2 :
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over =True
                    player = 1
                
                draw_figures()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
