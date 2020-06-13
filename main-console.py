import tictactoe

def checkWinOrDraw(game):
    if(game.checkWinner()!=0):
        return 'WINS'
    if(game.checkWinner()==0 and len(game.getEmptyCells())==0):
        return 'DRAW'
    return 'NONE'

print('---Rules---')
print('1. The player who makes a move first will get X')
print('2. Table orientation is given below. Choose one number between 0-8 to mark the position.')
print('\n')
print(' 0 | 1 | 2 ')
print('---|---|---')
print(' 3 | 4 | 5 ')
print('---|---|---')
print(' 6 | 7 | 8 ')
print('           ')
game = tictactoe.Game()
start =(input('Who starts?(P/C): '))
print('\n')
while(game.checkWinner()==0 and len(game.getEmptyCells())!=0):
    if(start == 'C'):
        game.botMakeMove('X')
        game.printBoard()
        if(checkWinOrDraw(game) != 'NONE'):
            if(checkWinOrDraw(game) == 'WINS'):
                print('Computer Wins!')
                break
            else:
                print('Game Drawn!')
                break
        var = int(input('\nEnter position:'))
        if(var in game.getEmptyCells()):
            game.setPosition('O',var)
            if(checkWinOrDraw(game) != 'NONE'):
                if(checkWinOrDraw(game) == 'WINS'):
                    print('You Win!')
                    break
                else:
                    print('Game Drawn!')
                    break
        else:
            print('Position already filled. Retry!')
            continue
    else:
        var = int(input('\nEnter position:'))
        if(var in game.getEmptyCells()):
            game.setPosition('X',var)
            if(checkWinOrDraw(game) != 'NONE'):
                if(checkWinOrDraw(game) == 'WINS'):
                    print('You Win!')
                    break
                else:
                    print('Game Drawn!')
                    break
        else:
            print('Position already filled. Retry!')
            continue
        game.botMakeMove('O')
        game.printBoard()
        if(checkWinOrDraw(game) != 'NONE'):
            if(checkWinOrDraw(game) == 'WINS'):
                print('Computer Wins!')
                break
            else:
                print('Game Drawn!')
                break