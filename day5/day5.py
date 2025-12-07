with open('day5.txt', 'r') as file:
    data = file.read().splitlines()

def part1():
    answer = 0

    split_ix = data.index('')
    ranges = data[:split_ix]
    ids = data[split_ix + 1:]

    for id in ids:
        is_spoiled = True

        for rang in ranges:
            start, end = rang.split('-')[0], rang.split('-')[1]
            if int(id) >= int(start) and int(id) <= int(end): 
                is_spoiled = False
                break

        if not is_spoiled:
            answer += 1

    return answer

print(f"Part 1: {part1()}")

def part2():
    split_ix = data.index('')
    formatted_ranges = [[int(irange.split('-')[0]), int(irange.split('-')[1])] for irange in data[:split_ix]]

    # first attempt - super brute force. never worked past example.
    # [(start, end)]
    # while True:
    #     range_to_add = ()
    #     ranges_to_remove = []
    #     for i, irange in enumerate(formatted_ranges):
    #         istart, iend = irange[0], irange[1]
    #         for j in range(i + 1, len(formatted_ranges)):
    #             jrange = formatted_ranges[j]
    #             jstart, jend = jrange[0], jrange[1]

    #             new_start, new_end = jstart, jend
                
    #             # check if first range fully inside second
    #             if istart > jstart and iend < jend:
    #                 ranges_to_remove = [irange]
    #                 break
    #             # check if first range starts inside second
    #             if istart > jstart and istart < jend:
    #                 new_end = max(iend, jend)
    #                 range_to_add = (new_start, new_end)
    #                 ranges_to_remove = [irange, jrange]
    #             # first range end inside second
    #             if iend > jstart and iend < jend:
    #                 new_start = min(istart, jstart)
    #                 range_to_add = (new_start, new_end)
    #                 ranges_to_remove = [irange, jrange]

    #             if ranges_to_remove: break
            
    #         if ranges_to_remove: break

    #     if ranges_to_remove:
    #         for irange in ranges_to_remove:
    #             formatted_ranges.remove(irange)
            
    #         if range_to_add: formatted_ranges.append(range_to_add)
    #     else:
    #         # we went through everything and have no merges
    #         break

    # got inspo to try sorted from reddit
    sorted_ranges = sorted(formatted_ranges)
    i = 1
    while i < len(sorted_ranges):
        current_range = sorted_ranges[i]
        last_range = sorted_ranges[i - 1]

        current_start, current_end = current_range[0], current_range[1]
        last_start, last_end = last_range[0], last_range[1]

        # check if current range is fully inside last range
        if current_start >= last_start and current_end <= last_end:
            sorted_ranges.pop(i)
            continue

        # check if current range started inside last range
        if current_start >= last_start and current_start <= last_end:
            # we keep last start but update last end
            last_range[1] = max(current_end, last_end)
            sorted_ranges.pop(i)
            continue

        # check if current range ended inside last range
        if current_end >= last_start and current_end <= last_end:
            # we keep last end but update last start
            last_range[0] = min(current_start, last_start)
            sorted_ranges.pop(i)
            continue
        
        # no merges happened
        i += 1

    answer = 0
    for irange in sorted_ranges:
        start, end = irange[0], irange[1]
        answer += (end - start) + 1

    return answer

print(f"Part 2: {part2()}")
