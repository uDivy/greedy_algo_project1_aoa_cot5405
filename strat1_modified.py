import heapq

def max_houses(n, m, houses):
    # sort houses based on startDay and endDay (if startDay is same)
    houses.sort(key=lambda h: (h[0],h[1]))

    # Initialize the priority queue and other variables
    pq = []
    houses_painted = []
    location = 0
    day = 1

    for i in range(m):
        start_day, end_day = houses[i]
        location += 1
        heapq.heappush(pq, ((start_day,end_day),location))
    
    # (start_day, end_day), pos = heapq.heappop(pq)
    ptr = 0
    while day <= n and pq:

        # Paint the house which is recently published
        print(pq)
        start_day, end_day = houses[ptr]
        if start_day > day:
            day += 1
            continue
        (start_day, end_day), pos = heapq.heappop(pq)
        if start_day <= day and end_day >= day:
            houses_painted.append(pos)
            day += 1
            ptr = pos
        
    return houses_painted

# read input
n, m = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(m)]

# read input from file
# with open("input_5000.txt", "r") as f:
# 	n, m = map(int, f.readline().split())
# 	houses = [tuple(map(int, line.split())) for line in f]

# call the function and print the output
painted = max_houses(n, m, houses)
print(' '.join(map(str, painted)))
print(len(painted))

# 10 5
# 1 2
# 1 2
# 1 5
# 1 5
# 3 4



# import heapq

# def max_painted_houses(houses, n):
#     # sort houses based on startDay and endDay (if startDay is same)
#     houses.sort(key=lambda h: (h[0],h[1]))

#     # Initialize the priority queue and other variables
#     pq = []
#     houses_painted = []
#     location = 0

#     for day in range(1, n+1):

#         # Paint the house with the earliest start day
        
#         while houses and houses[0][0] <= day:
#             start_day, end_day = houses.pop(0)
#             location += 1
#             heapq.heappush(pq, ((start_day, end_day),location))
        
#         while pq:
#             print(pq)
#             (start_day, end_day), pos = heapq.heappop(pq)
#             if end_day >= day:
#                 houses_painted.append(pos)
#                 break

#     return houses_painted

# # read input
# n, m = map(int, input().split())
# houses = [tuple(map(int, input().split())) for _ in range(m)]

# # read input from file
# # with open("input_5000.txt", "r") as f:
# # 	n, m = map(int, f.readline().split())
# # 	houses = [tuple(map(int, line.split())) for line in f]

# # call the function and print the output
# painted = max_painted_houses(houses, n)
# print(' '.join(map(str, painted)))
# print(len(painted))

# 7 10
# 1 2
# 2 3
# 2 3
# 3 4
# 4 5
# 4 5
# 5 6
# 5 6
# 5 8
# 9 10

# # 7 11
# # 1 2
# # 2 3
# # 2 5
# # 2 4
# # 4 4
# # 4 5
# # 4 5
# # 5 6
# # 5 6
# # 5 8
# # 9 10

# # 7 8
# # 1 2
# # 3 4
# # 4 5
# # 4 5
# # 5 6
# # 5 6
# # 5 8
# # 9 10