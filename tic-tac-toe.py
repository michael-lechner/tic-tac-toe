import sys, cmd

class Main(cmd.Cmd):
    intro = '\nwelcome to tic tac toe! you can enter a move at the prompt for a given symbol using x,y ie: 0,3\n'
    symbol = 'X'
    message = '\ntic-tac-toe move for {symbol} '
    prompt = message.format(symbol = symbol)
    board = [[None]*3, [None]*3, [None]*3]

    def do_exit(self, args):
        return True

    def do_move(self, args):
        coordinates = map(lambda x: int(x), args.split(','))
        self.move(*coordinates)
        self.print_board(self.board)

        if self.is_winner():
            print '{symbol} has won!\n'.format(symbol = self.symbol)
            return True
        else:
            self.update_prompt()

    def is_winner(self):
        if self.check_rows(): return True
        if self.check_columns(): return True
        if self.check_diagonals(): return True
        if self.is_board_full():
            print 'cat\'s eye, there is no winner!'
            return True

    def is_board_full(self):
        return len(filter(lambda row: any(cell == None for cell in row), self.board)) == 0

    def does_sequence_match(self, sequence):
        if sequence[0] == None: return False
        return all(x == sequence[0] for x in sequence)

    def check_rows(self):
        for row in self.board:
            if self.does_sequence_match(row): return True
        else: return False

    def check_columns(self):
        columns = []
        for i, row in enumerate(self.board):
            column = []
            for j, el in enumerate(row):
                column.append(self.board[j][i])
            if self.does_sequence_match(column): return True
        else: return False

    def check_diagonals(self):
        right = []
        left = []
        j = 0
        for i, row in enumerate(self.board):
            right.append(self.board[i][j])
            j += 1
        if self.does_sequence_match(right): return True

        for i, row in enumerate(self.board):
            j -= 1
            left.append(self.board[i][j])
        if self.does_sequence_match(left): return True
        return False

    def move(self, x, y):
        if self.is_valid_move(x, y): self.board[y][x] = self.symbol

    def is_valid_move(self, x, y):
        if x > len(self.board[0]) - 1 or y < 0:
            print '\nx-coordinate is invalid {x}'.format(x = x)
            return False
        if y > len(self.board) - 1 or y < 0:
            print '\ny-coordinate is invalid {y}'.format(y = y)
            return False
        if self.board[y][x] == None:
            print '\nplacing {symbol} to x: {x}, y: {y}'.format(symbol = self.symbol, x = x, y = y)
            return True
        else:
            print '\nthis move has already been made x: {x}, y: {y}'.format(x = x, y = y)
            return False

    def update_prompt(self):
        if self.symbol == 'X': self.symbol = 'O'
        else: self.symbol = 'X'
        self.prompt = self.message.format(symbol = self.symbol)

    def print_board(self, board):
        print '\n'
        for row in board:
            print ' | '.join(map(lambda x: x if x != None else ' ', row))
        print '\n'

if __name__ == '__main__':
    Main().cmdloop()
