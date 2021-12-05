from aocd import lines
from aocd import submit

drawn_numbers = lines[0].split(",")
boards = [[]]

def read_input():
    i = 0
    for line in lines[2:]:
        if not line:
            boards.append([])
            i=i+1
        else:
            boards[i].append(line.split())

def is_winning(board):
    for row in board:
        if not any(row):
            return True

    transpose=[list(a) for a in zip(*board)]
    for row in transpose:
        if not any(row):
            return True

    return False

def apply_called_number(board, number):
    for row in board:
        for index in range(len(row)): #is there a way to iterate with index but no range(len())?
            if row[index] == number:
                row[index] = False

def get_winning_board_and_number():
    while len(boards) >= 1:
        for number in drawn_numbers:
            boards_to_remove = []
            for board in boards:
                apply_called_number(board, number)
                if is_winning(board):
                    boards_to_remove.append(board)

            for board in boards_to_remove:
                if len(boards) == 1:
                    return (board, number)
                else:
                    boards.remove(board)
                    
def sum_board(board):
    return sum([int(cell) for row in board for cell in row])

read_input()
winning_board, winning_number = get_winning_board_and_number()
ans =sum_board(winning_board) * int(winning_number)
print(ans)

submit(ans)

