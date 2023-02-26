# import random
# import sys

# n = int(sys.argv[1])
# days = []
# with open(f"input_{n}.txt", "w") as f:
#     m = random.randint(1, 3*n) % 100000
#     f.write(f"{n} {m}\n")
#     for i in range(m):
#         start_day = random.randint(1, n)
#         end_day = random.randint(start_day, n)
#         days.append((start_day, end_day))
#     days.sort(key=lambda h: (h[0], h[1]))
#     for i in range(m):
#         f.write(f"{days[i][0]} {days[i][1]}\n")

