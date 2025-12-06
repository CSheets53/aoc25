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

print(f"Part 2: {part2()}")
