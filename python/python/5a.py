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
lines = sample

def read_input():
    # how do i stop having to wrap things in list everywhere
    return [list(map(lambda x : list(map(int, x.split(","))), vent.split(" -> "))) for vent in lines]

def board_size(vents):
    return tuple(map(lambda elt : max(elt)+1, list(zip(*[point for vent in vents for point in vent]))))

def is_not_diagonal(vent):
    return vent[0][0] != vent[1][0] and vent [1][0] != vent[1][1]

def apply_vent_to_floor(ocean_floor, vent):    
    # row vent
    if vent[0][1] == vent[1][1]:
        start_column = min(vent[0][0], vent[1][0])
        end_column = max(vent[0][0], vent[1][0])+1
        for column in range(start_column, end_column):
            ocean_floor[vent[0][1]][column] += 1
        return

    # column vent
    if vent[0][0] == vent[1][0]:
        start_row = min(vent[0][1], vent[1][1])
        end_row = max(vent[0][1], vent[1][1])+1
        for row in range(start_row, end_row):
            ocean_floor[row][vent[0][0]] += 1
        return

    # print(vent)
    
    # goes top left to bottom right
    # 1,2 -> 4,5 
    # 4,5 -> 1,2
    # can cut clauses from vvvv
    if (vent[0][0] < vent[1][0] and vent[0][1] < vent[1][1]) or (vent[0][0] > vent[1][0] and vent[0][1] > vent[1][1]):
        # swap the points if the second point is the top left one
        if vent[0][0] > vent[1][0] and vent[0][1] > vent[1][1]:
            vent = [vent[1], vent[0]]
        
        start_row = vent[0][1]
        stop_row = vent[1][1]+1

        for index, row in enumerate(range(start_row, stop_row)):
            # print("setting row", row, "column", vent[0][0]+index)
            ocean_floor[row][vent[0][0]+index] += 1
    else:
        # goes top left to bottom right
        # 8,0 -> 0,8
        # 0,8 -> 8,0 

        # swap the points if the second point is the top right one
        if vent[0][1] > vent[1][1]:
            vent = [vent[1], vent[0]]

        start_row = vent[0][1]
        stop_row = vent[1][1]+1

        for index, row in enumerate(range(start_row, stop_row)):
            # print("setting row", row, "column", vent[0][0]+index)
            ocean_floor[row][vent[0][0]-index] += 1




def count_twos(ocean_floor):
    count = 0
    for row in ocean_floor:
        for col in row:
            if col >= 2:
                count += 1
    return count
            
    # pprint(list(map(lambda row : len(list(filter(lambda vent : vent >= 2, row))), ocean_floor)))

vents = read_input()
width, height = board_size(vents)

ocean_floor = [[0] * width for _ in range(height)] 

print(vents)

for vent in vents:
    apply_vent_to_floor(ocean_floor, vent)

pprint(ocean_floor)
print(count_twos(ocean_floor))

# submit(count_twos(ocean_floor))

