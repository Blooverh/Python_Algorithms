class TicTacToe:
    def __init__(self):
        self._board= [[' '] *3 for i in range(3)] # creates a list of 3 lists containing 3 empty strings
        self._player='X' # X is what we use to mark our spot in the game

    def mark(self,i,j):
        """Function that will place the mark in the matrix based on the players position"""

        if not (0<= i <= 2 and 0<=j<=2): #if player puts mark out of matrix bounds, raise error
            raise ValueError('Invalid board position')

        if self._board[i][j] != ' ':  # if player puts a mark in a position that is not empty raise error
            raise ValueError('Board Position taken')
        
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        
        self._board[i][j]=self._player #we assign to position i j the character X onto the empty value of the board

        if self._player== 'X':
            self._player=='O'
        else:
            self._player=='X'

    def _is_win(self, mark):
        """Check whether the board config is a win for a given player or a tie"""
        board= self._board # create empty matrix as the board

        return(mark == board[0][0] == board[0][1] == board[0][2] or # row 0
                mark == board[1][0] == board[1][1] == board[1][2] or # row 1
                mark == board[2][0] == board[2][1] == board[2][2] or # row 2
                mark == board[0][0] == board[1][0] == board[2][0] or # column 0
                mark == board[0][1] == board[1][1] == board[2][1] or # column 1
                mark == board[0][2] == board[1][2] == board[2][2] or # column 2
                mark == board[0][0] == board[1][1] == board[2][2] or # diagonal
                mark == board[0][2] == board[1][1] == board[2][0]) #reverse diagonal
        
    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
            
        return None
        
    def __str__(self):
        """Return string representation of current game board"""

        rows=['|'.join(self._board[r]) for r in range(3)]
        return'\n---------\n'.join(rows)
    
game=TicTacToe()

game.mark(1,1)
#need for more marks
print(game)