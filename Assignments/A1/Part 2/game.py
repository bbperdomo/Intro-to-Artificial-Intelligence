#Assignment 1
#Team members: Tyler Nguyen, Bryan Perdomo, Peterling Etienne
#Due Date: June 11th 2021
from player import AIPlayer, HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # keep track of winner
    def print_board(self):
        for row in [self.board[i*3: (i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        '''This function will print the numbered board for guide'''
        number_board = [[str(i) for i in range(j*3, (j+1)* 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        '''This function will make the move'''
        if self.board[square] == ' ': #if the board have empty space
            self.board[square] = letter #set the letter X or O
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        '''This function check if there is a winner'''
        #check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column ]):
            return True
        #check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all of these fail
        return False

def play(game, x_player, o_player, print_game=True):
    '''This function will start to play the game'''
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        #define a function to make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X' # other turn's
    if print_game:
        print('It is a tie!')


#driver code
if __name__ == '__main__':
    print('')
    print('''This TicTacToe game AI robot vs player will use MinMax algorithm to perform an adversarial search \nwhich will find the best stragery to play 3x3 tictactoe game, \nit will try to find the best way to win or tie a game''')
    # print('')
    next_game = True
    while next_game:
        x_player = HumanPlayer('X') #set human X
        o_player = AIPlayer('O') #robot O
        t = TicTacToe() #set up the board
        play(t, x_player, o_player, True) #start playing
        choice = input('Do you want to play again? (y/n): ') #ask user if they want to continue
        if choice != 'Y' or 'y':
            next_game = False

        