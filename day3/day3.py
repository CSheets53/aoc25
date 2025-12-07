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

def part2():
    # struggled on this one, ended up looking for hints at the reddit and started reading about a monotonic stack
    # https://www.geeksforgeeks.org/dsa/introduction-to-monotonic-stack-2/
    answer = 0

    for bank in data:
        # go backwards, to always swap in the highest numbers on the left
        start_ix = len(bank) - 12
        og_bank = [int(c) for c in bank]
        stack = og_bank[start_ix:]

        # now compare every element in the stack to further up the bank to see if any swaps should be made
        # we don't want to look further ahead than where the last swap happened
        last_swap_bank_ix = -1
        for i in range(len(stack)):
            end_ix = last_swap_bank_ix
            for j in range(start_ix + i, end_ix, -1):
                if og_bank[j] >= stack[i]: 
                    stack[i] = og_bank[j]
                    last_swap_bank_ix = j

        joltage = ''.join([str(digit) for digit in stack])
        answer += int(joltage)
    
    return answer

print(f"Part 2: {part2()}")
