def max_houses(n, m, houses):
    # sort houses based on end day in ascending order
    houses.sort(key=lambda x: x[1])
    curr_day = 1
    houses_painted = []
    
    # iterate through each day from day 1 to n
    while curr_day <= n and houses:
        i = 0
        # find the first house that can be painted on the current day
        while i < len(houses) and houses[i][0] > curr_day:
            i += 1
        
        if i < len(houses):
            
            # remove the painted house from the list
            houses_painted.append(houses.pop(i)[2])
        
        # increment the current day
        curr_day += 1
    return houses_painted

# read input
n, m = map(int, input().split())
houses = [tuple(map(int, input().split())) for i in range(m)]


# read input from file
# with open("input_5000.txt", "r") as f:
# 	n, m = map(int, f.readline().split())
# 	houses = [tuple(map(int, line.split())) for line in f]
        
new_tuple = []
for i, house in enumerate(houses):
    new_tuple.append((house[0], house[1], i+1))

# call the function and print the output
painted = max_houses(n, m, new_tuple)
print(' '.join(map(str, painted)))
# print(len(painted))