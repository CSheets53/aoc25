from copy import deepcopy

with open('day4.txt', 'r') as file:
    data = file.read().splitlines()

def part1():
    answer = 0

    for i, row in enumerate(data):
        for j, col in enumerate(data[i]):
            if col == '@':
                adj_roll_count = 0
                # check 8 adjacent positions
                if i > 0 and j > 0 and data[i - 1][j - 1] == '@': adj_roll_count += 1 #tl
                if i > 0 and data[i - 1][j] == '@': adj_roll_count += 1 #t
                if i > 0 and j < len(row) - 1 and data[i - 1][j + 1] == '@': adj_roll_count += 1 #tr
                if j > 0 and data[i][j - 1] == '@': adj_roll_count += 1 #l
                if j < len(row) - 1 and data[i][j + 1] == '@': adj_roll_count += 1 #r
                if i < len(data) - 1 and j > 0 and data[i + 1][j - 1] == '@': adj_roll_count += 1 #bl
                if i < len(data) - 1 and data[i + 1][j] == '@': adj_roll_count += 1 #b
                if i < len(data) - 1 and j < len(row) - 1 and data[i + 1][j + 1] == '@': adj_roll_count += 1 # br

                if adj_roll_count < 4: answer += 1

    return answer

print(f"Part 1: {part1()}")

def part2():
    answer = 0
    mdata = deepcopy(data)

    # surprised this wasn't super time-consuming!
    roll_positions_to_remove = []
    while True:
        for i, row in enumerate(mdata):
            for j, col in enumerate(mdata[i]):
                if col == '@':
                    adj_roll_count = 0
                    # check 8 adjacent positions
                    if i > 0 and j > 0 and mdata[i - 1][j - 1] == '@': adj_roll_count += 1 #tl
                    if i > 0 and mdata[i - 1][j] == '@': adj_roll_count += 1 #t
                    if i > 0 and j < len(row) - 1 and mdata[i - 1][j + 1] == '@': adj_roll_count += 1 #tr
                    if j > 0 and mdata[i][j - 1] == '@': adj_roll_count += 1 #l
                    if j < len(row) - 1 and mdata[i][j + 1] == '@': adj_roll_count += 1 #r
                    if i < len(mdata) - 1 and j > 0 and mdata[i + 1][j - 1] == '@': adj_roll_count += 1 #bl
                    if i < len(mdata) - 1 and mdata[i + 1][j] == '@': adj_roll_count += 1 #b
                    if i < len(mdata) - 1 and j < len(row) - 1 and mdata[i + 1][j + 1] == '@': adj_roll_count += 1 # br

                    if adj_roll_count < 4: 
                        answer += 1
                        roll_positions_to_remove.append((i, j))

        if len(roll_positions_to_remove) == 0: break

        # remove rolls
        for pos in roll_positions_to_remove:
            i, j = pos
            row_str_list = [c for c in mdata[i]]
            row_str_list[j] = '.'
            mdata[i] = ''.join(row_str_list)

        roll_positions_to_remove = []

    return answer

print(f"Part 2: {part2()}")

