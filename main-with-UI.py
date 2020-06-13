import pygame
import tictactoe

pygame.init()

game=tictactoe.Game()

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 

human_img = pygame.image.load('images/human.jpg')
table_img = pygame.image.load('images/table.jpg')
computer_img = pygame.image.load('images/computer.jpg')
X_img = pygame.image.load('images/X.jpg')
O_img = pygame.image.load('images/O.jpg')

def writeText(messege):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(messege, True, green)
    return text,text.get_rect()

def playTurn(p1_turn,p1,p2,position):
    row, col = int(position/3), position%3
    if(game.board[row][col]!=0):
        return p1_turn
    if(p1_turn==True):
        if(p1 == 'computer'):
            game.botMakeMove('X')
        else:
            game.setPosition('X',position)
            game.botMakeMove('O')
            p1_turn = False if p1_turn == True else True
    else:
        if(p2 == 'computer'):
            game.botMakeMove('O')
        else:
            game.setPosition('O',position)
            game.botMakeMove('X')
            p1_turn = False if p1_turn == True else True
    p1_turn = False if p1_turn == True else True
    return p1_turn
screenX = 550
screenY = 550 

screen = pygame.display.set_mode((screenX,screenY))
pygame.display.set_caption('Unbeatable TicTacToe')

run = True
startPlayerChosen = False
initialFill = True
p1_turn = True
p1 = ''
p2 = ''
iter = 0
while run:
    iter += 1
    if startPlayerChosen == False: 
        text,textRect = writeText('Who will go first?')  
        textRect.center = (screenX // 2, screenY // 6)
        screen.blit(text, textRect)
        human = pygame.draw.rect(screen,(255,255,255),(25,150,240,309))
        computer = pygame.draw.rect(screen,(255,255,255),(285,150,240,309))
        screen.blit(human_img,human)
        screen.blit(computer_img,computer)
    elif initialFill == True:
        screen.fill((0,0,0))
        table = pygame.draw.rect(screen,(255,255,255),(35,50,480,480))
        screen.blit(table_img,table)
        zero = pygame.draw.rect(screen,(0,0,0),(35,45,150,140))
        one = pygame.draw.rect(screen,(0,0,0),(210,45,150,140))
        two = pygame.draw.rect(screen,(0,0,0),(370,45,150,140))
        three = pygame.draw.rect(screen,(0,0,0),(40,215,150,150))
        four = pygame.draw.rect(screen,(0,0,0),(210,215,150,150))
        five = pygame.draw.rect(screen,(0,0,0),(370,215,150,150))
        six = pygame.draw.rect(screen,(0,0,0),(40,375,150,150))
        seven = pygame.draw.rect(screen,(0,0,0),(210,375,150,150))
        eight = pygame.draw.rect(screen,(0,0,0),(370,375,150,150))
        initialFill = False
    elif initialFill == False:
        if(game.checkWinner()=='X'):
            text,textRect = writeText(p1.upper()+' Wins!')  
            textRect.center = (screenX // 2, 50//2)
            screen.blit(text, textRect)
        elif (game.checkWinner()=='O'):
            text,textRect = writeText(p2.upper()+' Wins!')  
            textRect.center = (screenX // 2, 50//2)
            screen.blit(text, textRect)
        elif game.checkWinner()==0 and len(game.getEmptyCells())==0:
            text,textRect = writeText('Draw Game!')  
            textRect.center = (screenX // 2, 50//2)
            screen.blit(text, textRect)
        for i in range(0,3):
            for j in range(0,3):
                position = i*3+j
                if(position == 0):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,zero) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,zero) 
                elif(position == 1):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,one) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,one)
                elif(position == 2):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,two) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,two)
                elif(position == 3):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,three) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,three)
                elif(position == 4):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,four) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,four)
                elif(position == 5):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,five) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,five)
                elif(position == 6):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,six) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,six)
                elif(position == 7):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,seven) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,seven)
                elif(position == 8):
                    if game.board[i][j]=='X':
                        screen.blit(X_img,eight) 
                    elif game.board[i][j]=='O':
                        screen.blit(O_img,eight)
    #print(iter)
    #screen.fill((255, 255, 255))
    pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if startPlayerChosen == False:
                #print('Hello1')
                pos = pygame.mouse.get_pos()
                if human.collidepoint(pos):
                    print('Human Selected!')
                    p1 = 'human'
                    p2 = 'computer'
                    startPlayerChosen = True
                elif computer.collidepoint(pos):
                    print('Computer Selected!')
                    p1 = 'computer'
                    p2 = 'human'
                    game.botMakeMove('X')
                    p1_turn = False
                    startPlayerChosen = True
            else:
                #print('Hello2')
                pos = pygame.mouse.get_pos()
                if zero.collidepoint(pos):
                    print('Zero Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,0)
                elif one.collidepoint(pos):
                    print('One Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,1)
                    #p1_turn = False if p1_turn == True else True
                elif two.collidepoint(pos):
                    print('Two Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,2)
                    #p1_turn = False if p1_turn == True else True
                elif three.collidepoint(pos):
                    print('Three Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,3)
                    #p1_turn = False if p1_turn == True else True
                elif four.collidepoint(pos):
                    print('Four Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,4)
                    #p1_turn = False if p1_turn == True else True
                elif five.collidepoint(pos):
                    print('Five Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,5)
                    #p1_turn = False if p1_turn == True else True
                elif six.collidepoint(pos):
                    print('Six Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,6)
                    #p1_turn = False if p1_turn == True else True
                elif seven.collidepoint(pos):
                    print('Seven Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,7)
                    #p1_turn = False if p1_turn == True else True
                elif eight.collidepoint(pos):
                    print('Eight Selected!')
                    p1_turn = playTurn(p1_turn,p1,p2,8)
                    #p1_turn = False if p1_turn == True else True
            #print(pos)
    pygame.display.update()

pygame.quit()