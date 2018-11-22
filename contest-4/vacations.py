from math import *
from sys import stdin

# 0 -> rest, 1 -> contest, 2 -> gym
options = [[0], [0, 1], [0, 2], [0, 1, 2]]

def vacations(n, available):
    min_rest = [[1, 0 if 1 in options[available[0]] else inf, 0 if 2 in options[available[0]] else inf]]

    for i in range(1, len(available)):
        day = available[i]
        current = [inf, inf, inf]
        
        for o in options[day]:

            min_day = inf

            # we find the minimum in the previous day
            for j in range(0, 3):
                v = min_rest[-1][j]

                if j != o or o == 0: # we cannot take the same activity, except if it is rest
                    if v < min_day:
                        min_day = v

            current[o] = min_day if (o != 0) else min_day + 1

        min_rest.append(current)
    return min(min_rest[-1])

lines = stdin.read().split("\n")

# make sure there is no empty line at the end
if lines[-1] == '':
    lines.pop()

n = int(lines[0])
available = [int(v) for v in lines[1].split(" ")]

print(vacations(n, available))