import random

class TicTacToe:
    def __init__(self):
        self.board = [ [ 0 for i in range(3) ] for j in range(3) ]
        #self.testSetup()

    def setPosition(self,key,position):
        row,col = int(position/3),position%3
        self.board[row][col] = key if self.board[row][col]==0 else self.board[row][col]

    def unsetPosition(self,position):
        row,col = int(position/3),position%3
        self.board[row][col] = 0  

    def testSetup(self):
        self.setPosition('X',0)
        self.setPosition('X',2)
        self.setPosition('X',3)
        self.setPosition('X',5)
        self.setPosition('O',6)
        self.setPosition('O',4)
        self.setPosition('O',8)  

    def getEmptyCells(self):
        emptyCells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    emptyCells.append(i*3+j)
        return emptyCells

    def checkWinner(self):
        #checking rows
        for row in self.board:
            if len(set(row)) ==1 and row[0]!=0:
                return row[0]
        #checking columns
        for i in range(3):
            col = [row[i] for row in self.board]
            if len(set(col)) ==1 and col[0]!=0:
                return col[0] 
        #checking diagonals
        d1 = [self.board[i][i] for i in range(len(self.board))]
        d2 = [self.board[i][len(self.board)-i-1] for i in range(len(self.board))]
        if len(set(d1)) ==1 and d1[0]!=0:
                return d1[0] 
        if len(set(d2)) ==1 and d2[0]!=0:
                return d2[0]
        return 0

    def botMakeMove(self,key):
        if len(self.getEmptyCells()) == 9:
            self.setPosition(key,random.randint(0,8))
            return 0
        if(self.checkWinner()==0 and len(self.getEmptyCells())!=0):
            self.botMove(key)

    def botMove(self,key,mode='max',layer=1):
        #print(key,mode,layer)
        #print('winner',self.checkWinner())
        #self.printBoard()
        cells = self.getEmptyCells()
        scores = []
        if(key == 'X'):
            oppkey = 'O'
        else:
            oppkey = 'X'
        if layer > 1:
            #print(key,mode)
            #print(self.checkWinner())
            if(self.checkWinner() == key):
                #print('called1')
                #self.printBoard()
                #print('return ',1*(len(self.getEmptyCells())+1))
                return 1*(len(self.getEmptyCells())+1)
            elif (self.checkWinner() == oppkey):
                #print('called2')
                #self.printBoard()
                #print('return ',-1*(len(self.getEmptyCells())+1))
                return -1*(len(self.getEmptyCells())+1)           
            else:
                #print('called3')
                if len(self.getEmptyCells())==0:
                    #print('return ',0)
                    return 0
                else:
                    #print(cells)
                    for cell in cells:
                        self.setPosition(oppkey if layer%2 == 0 else key ,cell)
                        #print(cell, layer)
                        scores.append(self.botMove(key,'min' if mode=='max' else 'max',layer+1))
                        self.unsetPosition(cell)
                    if mode == 'max':
                        return max(scores)
                    else:
                        return min(scores)
        else:
            #print(cells)
            for cell in cells:
                self.setPosition(key,cell)
                #print(cell,layer)
                #print(self.getEmptyCells())
                scores.append(self.botMove(key,'min' if mode=='max' else 'max',layer+1))
                self.unsetPosition(cell)
                #print(self.getEmptyCells())
        #print(scores)
        index = scores.index(max(scores))
        self.setPosition(key,cells[index]) 

    def printBoard(self):
        for i in range(0,3):
            print(" ",self.board[i][0] if self.board[i][0]!=0 else ' '," | ",self.board[i][1] if self.board[i][1]!=0 else ' '," | ",self.board[i][2] if self.board[i][2]!=0 else ' ')
    
    def getBoard(self):
        return self.board
    
