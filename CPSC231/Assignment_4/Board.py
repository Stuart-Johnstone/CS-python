#30086585
#Stuart Johnstone

#THis is a file that is supposed to be used in conjunction with the tictactoe.py file
#this file containst the class Board that has the purpose of dealing with the creation of the playing board and other functions
#It also contains the win conditions aswell as: checking if the board is full, giving the player an easy hint


#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:
    board = None
    lst = None
    def __init__(self,row=3,colomns=3):     #initalizes the object and creates the board
        self.board = []                     #starts with an emptry board
        self.row = row                      #gets the # of rows, default is 3
        self.colomns = colomns              #gets the # of cols, default is 3

        for x in range(row):                #loops for len rows, creates the y axis
            self.lst = []                   #creates an empty list
            for i in range(colomns):        #loops for len colomns, creates the x axis
                self.lst.append(0)          #adds 0's to the list
            self.board.append(self.lst)     #Creates the rows

    def rows(self):                         #returns the # of rows
        return self.row

    def cols(self):                         #returns the # of collomns
        return self.colomns

    def canPlay(self,Row,Col):              #returns true of the spot is open
        if self.board[Row][Col] == EMPTY:
            return True
        else:
            return False

    def play(self,Row,Col,piece):           #changes the empty position to an X or O
        self.board[Row][Col] = piece
        pass

    def full(self):                         #checks if the row is full
        for i in self.board:
            for x in i:
                if x == EMPTY:
                    return False
        return True

    def winInRow(self,Row,piece):                               #checks to see if there was a win in a row
        for x in range(len(self.board[Row])-2):                 #for the length of the list - 2(to prevent out of range)
            if self.board[Row][x:x+3] == [piece,piece,piece]:   #if the 3 pieces are in a row then it returns true
                return True
        return False

    def winInCol(self,Col,piece):                               #chechs to see if there was a win in a col
        lst = []                                                #empty list used for storing the contents of a colloum
        for i in self.board:                                    #for the length of the board fill the empty list with a col
            lst.append(i[Col])
        
        for i in range(len(lst)-2):                             #for the len of the col list check if there is a win in a col
            if lst[i:i+3] == [piece,piece,piece]:
                return True
        return False
    
    def winInDiag(self,piece):                                                                                      #checks to see if there is a win in a diagnal
        for i in range(len(self.board)-2):
            for x in range(len(self.board[0])-2):
                if self.board[i][x] == piece and self.board[i+1][x+1] == piece and self.board[i+2][x+2] == piece:   #if the / diagonal has a win then it returns true
                    return True
        for i in range((len(self.board)-2)):
            for x in range((len(self.board[0])-2)):
                if self.board[i+2][x] == piece and self.board[i+1][x+1] == piece and self.board[i][x+2] == piece:   #if the \ diagonal has a win then it returns true
                    return True
        return False 

    def won(self, piece):                    #checks the win condidtions
        for i in range(len(self.board)):    #checks all of the rows for a win
            if self.winInRow(i,piece):
                return True
        for x in range(len(self.board[0])): #checks all of the colomns for a win
            if self.winInCol(x,piece):
                return True
        if self.winInDiag(piece):           #checks the diagonals for a win
            return True
        return False

    def hint(self, piece):                            #gives the player an easy hint
        for row in range(len(self.board)):            #for the row in the board
            for col in range(len(self.board[0])):     #for the col in the board
                if self.canPlay(row,col):
                    self.play(row,col,piece)
                    if self.won(piece):               #if the piece would cause a win then it returns that as a hint
                        self.board[row][col] = EMPTY
                        return row,col
                    else:                             #if not then it will return -1,-1
                        self.board[row][col] = EMPTY
        return -1, -1

    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False