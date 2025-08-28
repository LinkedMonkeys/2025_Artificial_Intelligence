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


def increment(x):
    return x+1

puzzle = Puzzle()
print(puzzle)
print(increment(42))