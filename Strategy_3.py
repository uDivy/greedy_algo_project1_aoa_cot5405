import heapq

def max_houses_painted(n, m, houses):
    # sort houses based on startDay and endDay (if startDay is same)
    houses.sort(key=lambda h: (h[0],h[1]))

    # Initialize the priority queue and other variables
    pq = []
    houses_painted = []
    location = 0
    
    # Iterate over each day
    for day in range(1, n+1):

        # Build the heap for the shortest duration
        while houses and houses[0][0] <= day:
            start_day, end_day = houses.pop(0)
            location += 1
            heapq.heappush(pq, ((end_day-start_day+1,end_day),location))
        
        # Paint the house which is available for the least period
        while pq:
            (_, end_day), pos = heapq.heappop(pq)
            if end_day >= day:
                houses_painted.append(pos)
                break
    
    return houses_painted

# read input
n, m = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
# with open("input_3000.txt", "r") as f:
# 	n, m = map(int, f.readline().split())
# 	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_houses_painted(n, m, houses)
print(' '.join(map(str, painted)))
# print(len(painted))