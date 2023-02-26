import heapq

def max_houses_painted(n, m, houses):
    # sort houses based on startDay
    houses.sort(key=lambda h: h[0])

    # Initialize the priority queue and other variables
    pq = []
    houses_painted = []
    painted = [False] * (m+1)
    location = 0
    
    # Iterate over each day
    for day in range(1, n+1):
        # Add all unpainted houses that are available on this day to the priority queue

        while houses and houses[0][0] <= day:
            start_day, end_day = houses.pop(0)
            location += 1
            heapq.heappush(pq, (end_day-start_day+1,location))
        
        # Paint the house with the shortest available duration
        if pq:
            print(pq)
            duration, pos = heapq.heappop(pq)
            if not painted[pos]:
                houses_painted.append(pos)
                painted[pos] = True

        print("h_p", houses_painted)
    
    return houses_painted

# read input
# n, m = map(int, input().split())
# houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
with open("input_3000.txt", "r") as f:
	n, m = map(int, f.readline().split())
	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_houses_painted(n, m, houses)
print(' '.join(map(str, painted)))
print(len(painted))

#INPUT
# 9 10
# 1 2 1(ON DAY 1)
# 2 4 5
# 2 3 2
# 3 4 3
# 4 6 6
# 4 5 4
# 5 8 7
# 5 9 8
# 5 9
# 9 10