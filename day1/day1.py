with open('day1.txt', 'r') as file:
    data = file.read().splitlines()

def part1():
    # password is # of times the dial is left pointing at 0 after any rotation in sequence
    current_dial_pos = 50
    password = 0

    for rotation in data:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            current_dial_pos = (current_dial_pos - distance) % 100
        else:
            current_dial_pos = (current_dial_pos + distance) % 100
        
        if current_dial_pos == 0: password += 1

    return password

print(f"Part 1: {part1()}")

def part2():
    # password is # times any click causes dial to point at 0
    current_dial_pos = 50
    password = 0

    for rotation in data:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'L':
            dividend = current_dial_pos - distance
            if dividend <= 0: 
                # need to account for when current_dial_pos starts at 0 or not - if starting at 0, it's not truly going back
                password += (abs(dividend) // 100) + (1 if current_dial_pos > 0 else 0)
        else:
            dividend = current_dial_pos + distance
            if dividend >= 100: 
                password += dividend // 100
        
        current_dial_pos = dividend % 100

    return password

print(f"Part 2: {part2()}")
