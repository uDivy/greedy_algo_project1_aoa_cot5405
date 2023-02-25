import heapq

import heapq

def max_houses(n, m, houses):
    houses.sort(key=lambda x: x[0])
    available_houses = []
    houses_painted = 0
    current_day = 1
    
    for day in range(1, n+1):
        while houses and houses[0][0] <= day:
            heapq.heappush(available_houses, (-houses[0][1], houses[0][0]))
            houses.pop(0)
        if available_houses:
            end_day, start_day = heapq.heappop(available_houses)
            houses_painted += 1
        current_day += 1
        if not houses and not available_houses:
            break
    
    return houses_painted

# read input
n, m = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
# with open("input.txt", "r") as f:
# 	n, m = map(int, f.readline().split())
# 	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_painted_houses(n, m, houses)
for i in painted:
	print(i)
