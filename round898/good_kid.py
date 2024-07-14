input_size = int(input())

for _ in range(input_size):
    _ = input()
    input_string = input()
    result = 1
    a = [int(c) for c in input_string.split(" ")]

    sorted_a = sorted(a)

    sorted_a[0] = sorted_a[0]+1

    for x in sorted_a:
        result = result * x

    print (result)