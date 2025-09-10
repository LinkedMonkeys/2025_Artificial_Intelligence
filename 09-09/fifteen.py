import random

class Puzzle():
    def __init__(self):
        self.board = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, None]
        ]
        self.empty_row = 3
        self.empty_col = 3
    
    def __str__(self):
        result = ''
        for row in self.board:
            for item in row:
                if item == None:
                    result += '## '
                elif item < 10:
                    result += f' {item} '
                else:
                    result += f'{item} '
            result += '\n'
            
        return result

    def make_move(self, direction):
        match direction:
            case 'U':
                if self.empty_row < len(self.board)-1:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row+1][self.empty_col]
                    self.empty_row += 1
                    self.board[self.empty_row][self.empty_col] = None
            case 'D':
                if self.empty_row > 0:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row-1][self.empty_col]
                    self.empty_row -= 1
                    self.board[self.empty_row][self.empty_col] = None
            case 'L':
                if self.empty_col < len(self.board[self.empty_row])-1:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row][self.empty_col+1]
                    self.empty_col += 1
                    self.board[self.empty_row][self.empty_col] = None
            case 'R':
                if self.empty_col > 0:
                    self.board[self.empty_row][self.empty_col] = self.board[self.empty_row][self.empty_col-1]
                    self.empty_col -= 1
                    self.board[self.empty_row][self.empty_col] = None

    def scramble(self, num_moves):
        dirs = 'UDLR'
        for i in range(num_moves):
            direction = dirs[random.randint(0, 3)]
            self.make_move(direction)

puzzle = Puzzle()
print(puzzle)
puzzle.scramble(3)
print(puzzle)
