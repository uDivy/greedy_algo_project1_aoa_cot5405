import heapq

def max_houses(n, m, houses):
    # sort houses based on startDay and endDay (if startDay is same)
    houses.sort(key=lambda h: (h[0],h[1]))

    # Initialize the priority queue and other variables
    pq = []
    houses_painted = []
    location = 0
    day = 1
    ptr = 0

    # Building Priority Queue based startDay in ascending order.
    for i in range(m):
        start_day, end_day = houses[i]
        location += 1
        heapq.heappush(pq, ((start_day,end_day),location))
    
    while day <= n and pq:

        start_day, end_day = houses[ptr]

        # Skip the day if there is no available house
        if start_day > day:
            day += 1
            continue
        (start_day, end_day), pos = heapq.heappop(pq)

        # Paint a house
        if start_day <= day and end_day >= day:
            houses_painted.append(pos)
            day += 1
            ptr = pos
        
    return houses_painted

# read input
n, m = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
# with open("input_1000.txt", "r") as f:
# 	n, m = map(int, f.readline().split())
# 	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_houses(n, m, houses)
print(' '.join(map(str, painted)))
# print(len(painted))