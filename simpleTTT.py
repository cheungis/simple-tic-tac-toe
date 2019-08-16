class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.

        print(' %c | %c | %c '%(self.board[7],self.board[8],self.board[9]))
        print('-----------')
        print(' %c | %c | %c '%(self.board[4],self.board[5],self.board[6]))
        print('-----------')
        print(' %c | %c | %c '%(self.board[1],self.board[2],self.board[3]))        

    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise

        if ' ' in self.board:
            return False
        else:           
            return True
        
    def cellIsEmpty(self, cell):
       
        return self.board[cell] == ' ' 
    
    def assignMove(self, cell,ch):
    # assigns the cell of the board to the character ch

        self.board[cell] = ch
        
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

        
    def isWinner(self, ch):
    # Given a player's letter, this method returns True if that player has won.
        if self.board[1] == ch and self.board[2] == ch and self.board[3] == ch:
            return True
        elif self.board[4] == ch and self.board[5] == ch and self.board[6] == ch:
            return True
        elif self.board[7] == ch and self.board[8] == ch and self.board[9] == ch:
            return True
        elif self.board[1] == ch and self.board[4] == ch and self.board[7] == ch:
            return True
        elif self.board[2] == ch and self.board[5] == ch and self.board[8] == ch:
            return True
        elif self.board[3] == ch and self.board[6] == ch and self.board[9] == ch:
            return True
        elif self.board[1] == ch and self.board[5] == ch and self.board[9] == ch:
            return True
        elif self.board[3] == ch and self.board[5] == ch and self.board[7] == ch:
            return True
        else:
            return False
            
def main():
    
    # first create instance of tic tac toe
    TTT = TicTacToe()
    is_draw = False
    player_x = 'x'
    player_o = 'o'
    current_player = player_x
    while (not is_draw) and (TTT.whoWon() == ''):
        TTT.drawBoard()
        valid_move = False
        while not valid_move:
            try:
                position = int(input('It\'s player %c\'s turn, which spot would you like to fill? '%current_player))
                if position in range(1,10):
                    valid_move = TTT.cellIsEmpty(position)
                    if not valid_move:
                        print('That spot\'s already taken, please try again.')                
                else:
                    print('that move is invalid, please try again')
            except ValueError:
                print('That\'s not a number...')
        TTT.assignMove(position, current_player)
        winner = TTT.whoWon()
        if TTT.boardFull():
            is_draw = True
        if current_player == player_x:
            current_player = player_o
        elif current_player == player_o:
            current_player = player_x
    TTT.drawBoard()
    if is_draw:
        print('It was a draw.')
    else:
        print('The winner is player %c'%winner)
        
    input('press any key to close')
    
main()
