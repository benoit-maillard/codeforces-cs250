from math import *

def find_max(n, a, b, c):
    o = [0]
    for i in range(1, n + 1):
        max_current = - inf
        for l in (a, b, c):
            if l <= i:
                n_remaining = o[i - l] # number of cuts we can obtain after cutting length l
                max_current = max(max_current, n_remaining)

        o.append(1 + max_current) # cost of current cut is 1

    return o[n]

str_input = input()
values = str_input.split(" ")
values_n = [int(v) for v in values]

n, a, b, c = values_n

print(find_max(n, a, b, c))