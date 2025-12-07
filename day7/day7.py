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

def part2():
    first_row = data[0]
    beam_counts = [0] * len(first_row)
    beam_counts[first_row.find('S')] = 1
    for row in data[1:]:
        if '^' not in row: continue

        for i in range(len(beam_counts)):
            if beam_counts[i] > 0 and row[i] == '^':
                beam_counts[i - 1] += beam_counts[i]
                beam_counts[i + 1] += beam_counts[i]
                beam_counts[i] = 0

    return sum(beam_counts)

print(f"Part 2: {part2()}")
