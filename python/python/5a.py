from aocd import lines
from aocd import submit
from pprint import pprint

sample = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2"
]
# lines = sample
# ans 21140

def read_input():
    # how do i stop having to wrap things in list everywhere
    return [list(map(lambda x : list(map(int, x.split(","))), vent.split(" -> "))) for vent in lines]

def board_size(vents):
    return tuple(map(lambda elt : max(elt)+1, list(zip(*[point for vent in vents for point in vent]))))

def count_twos(ocean_floor):
    return sum(map(lambda row : list(map(lambda cell : True if cell >= 2 else False, row)).count(True), ocean_floor))

def apply_vent_to_floor(ocean_floor, vent):    
    # row vent
    if vent[0][1] == vent[1][1]:
        start_column = min(vent[0][0], vent[1][0])
        end_column = max(vent[0][0], vent[1][0])+1
        for column in range(start_column, end_column):
            ocean_floor[vent[0][1]][column] += 1
        return

    if (vent[0][0] < vent[1][0] and vent[0][1] < vent[1][1]) or (vent[0][0] > vent[1][0] and vent[0][1] > vent[1][1]):
        # goes top left to bottom right
        # 1,2 -> 4,5 
        # 4,5 -> 1,2
        col_step_coefficient = 1
    elif vent[0][0] == vent[1][0]:
        # column vent
        col_step_coefficient = 0
    else:
        # goes from top right to bottom left
        # 0,8 -> 8,0
        # 8,0 -> 0,8
        col_step_coefficient = -1

    # make sure vent[0] is always higher
    if vent[0][1] > vent[1][1]:
        vent = [vent[1], vent[0]]
    
    start_row = vent[0][1]
    stop_row = vent[1][1]+1

    for index, row in enumerate(range(start_row, stop_row)):
        ocean_floor[row][vent[0][0]+index*col_step_coefficient] += 1

vents = read_input()
width, height = board_size(vents)
ocean_floor = [[0] * width for _ in range(height)]
[apply_vent_to_floor(ocean_floor, vent) for vent in vents]

print(count_twos(ocean_floor))
# submit(count_twos(ocean_floor))

