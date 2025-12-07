with open('day7.txt', 'r') as file:
    data = file.read().splitlines()

def part1():
    answer = 0

    first_row = data[0]
    beam_positions = [first_row.find('S')]
    for row in data[1:]:
        if '^' not in row: continue

        new_positions = set([])
        for pos in beam_positions:
            if row[pos] == '^':
                new_positions.add(pos - 1)
                new_positions.add(pos + 1)
                answer += 1
            else:
                # carry over unused positions
                new_positions.add(pos)
    
        beam_positions = list(new_positions)

    return answer

print(f"Part 1: {part1()}")
