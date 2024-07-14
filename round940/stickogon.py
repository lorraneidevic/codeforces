import collections

input_size = int(input())

for _ in range(input_size):
    polygon = 0
    _ = input()
    input_string = input()
    sticks = [int(c) for c in input_string.split(" ")]

    counters = collections.Counter(sticks)

    for counter in counters.keys():
        if counters[counter] > 2:
            max_polygons = counters[counter] // 3
            polygon += max_polygons

    print(polygon)
