import time

with open('day2.txt', 'r') as file:
    data = file.readline().split(',')

def part1():
    # add up all invalid ids
    answer = 0

    for id_range in data:
        start, end = id_range.split('-')[0], id_range.split('-')[1]
        
        # naive: iterate through every number in start -> end to see if digits repeat twice
        for id in range(int(start), int(end) + 1):
            sid = str(id)
            if sid[:len(sid)//2] == sid[len(sid)//2:]:
                answer += int(sid)

    return answer

print(f"Part 1: {part1()}")

def part2():
    # add up all invalid ids
    answer = 0

    # my original solution - still ran fast but had a noticeable half-second delay
    for id_range in data:
        start, end = id_range.split('-')[0], id_range.split('-')[1]
        
        for id in range(int(start), int(end) + 1):
            sid = str(id)
            
            window_size = 1
            while window_size < len(sid) // 2 + 1:
                substr = sid[:window_size]
                if sid.count(substr) * window_size == len(sid):
                    answer += id
                    break
                
                window_size += 1

    return answer

t0 = time.time()
print(f"Part 2: {part2()}")
t1 = time.time()
print(f"\tTime: {(t1 - t0):0.3}s")

def part2_new():
    answer = 0

    # new solution
    # read that this is similar to LC 459, and there's a trick that if you duplicate a string that repeats, the original will still be in the middle with first and last removed
    # ex: ABCDABCD -> BCDABCDABCDABC (doubled with first and last removed)
    # https://seanstuber.com/2025/12/05/advent-of-code-2025-day-2/
    for id_range in data:
        start, end = id_range.split('-')[0], id_range.split('-')[1]
        
        for id in range(int(start), int(end) + 1):
            sid = str(id)
            if sid in (sid + sid)[1:-1]: answer += id

    return answer

t0 = time.time()
print(f"Part 2 (new): {part2_new()}")
t1 = time.time()
print(f"\tTime: {(t1 - t0):0.3}s")
