def max_houses_painted(n, m, houses):
    house_groups = {}
    for i in range(m):
        start, end = houses[i]
        if start in house_groups:
            house_groups[start].append(end)
        else:
            house_groups[start] = [end]
    
    current_day = 1
    num_houses_painted = []
    for day in range(1, n+1):
        if day in house_groups:
            available_houses = house_groups[day]
            min_start = min(available_houses)
            index = current_day + available_houses.index(min_start)
            if min_start >= current_day:
                num_houses_painted.append(index)
                current_day = min_start + 1
    
    return num_houses_painted

# read input
n, m = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
# with open("input_5000.txt", "r") as f:
# 	n, m = map(int, f.readline().split())
# 	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_houses_painted(n, m, houses)
print(' '.join(map(str, painted)))
print(len(painted))

# 7 8
# 1 2
# 3 4
# 4 5
# 4 5
# 5 6
# 5 6
# 5 8
# 9 10