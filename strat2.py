import heapq

def max_houses(n, m, houses):
    houses.sort(key=lambda x: x[0])
    available_houses = []
    houses_painted = []
    houseNo = 1

    for day in range(1, n+1):
        while houses and houses[0][0] <= day:
            heapq.heappush(available_houses, ((-houses[0][1], houses[0][0]), houseNo))
            houses.pop(0)
            houseNo += 1
        while available_houses and -available_houses[0][0][0] < day:
            heapq.heappop(available_houses)
        if available_houses:
            days, painted_house = heapq.heappop(available_houses)
            if painted_house not in houses_painted:
                houses_painted.append(painted_house)
        if not houses and not available_houses:
            break
    
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
