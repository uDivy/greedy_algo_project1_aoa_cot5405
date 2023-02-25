import heapq

def max_painted_houses(houses, n):
    # sort houses based on startDay
    houses.sort(key=lambda h: h[0])

    # initialize priority queue with houses available on day 1
    pq = []
    for location, house in enumerate(houses):
        if house[0] <= 1:
            heapq.heappush(pq, (house, location+1))

    # iterate over days and paint houses
    painted = []
    for day in range(1, n+1):
        while pq and pq[0][0][1] < day:
            # remove houses from pq that are no longer available to be painted
            heapq.heappop(pq)
        while pq and pq[0][0][0] <= day:
            # paint earliest available house on current day
            house, location = heapq.heappop(pq)
            if (location, house) not in painted:
                painted.append(location)
                break
        for location, house in enumerate(houses):
            if house[0] == day+1:
                # add unpainted houses available on current day to pq
                heapq.heappush(pq, (house, location+1))

    return painted

# read input
# n, m = map(int, input().split())
# houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
with open("input_50.txt", "r") as f:
	n, m = map(int, f.readline().split())
	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_painted_houses(houses, n)
print(' '.join(map(str, painted)))
print(len(painted))
