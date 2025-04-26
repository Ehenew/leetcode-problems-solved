import math

n, m, a = map(int, input().split())

flagstones_length = math.ceil(n / a)
flagstones_width = math.ceil(m / a)

total_flagstones = flagstones_length * flagstones_width
print(total_flagstones)
