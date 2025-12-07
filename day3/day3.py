with open('day3.txt', 'r') as file:
    data = file.read().splitlines()

def part1():
    answer = 0

    for bank in data:
        first_digit, first_pos = int(bank[0]), 0
        for i in range(1, len(bank) - 1):
            digit = int(bank[i])

            if digit > first_digit:
                first_digit = digit
                first_pos = i

        second_digit = int(bank[first_pos + 1])
        for i in range(first_pos + 1, len(bank)):
            second_digit = max(second_digit, int(bank[i]))

        joltage = str(first_digit) + str(second_digit)
        answer += int(joltage)
    
    return answer

print(f"Part 1: {part1()}")
