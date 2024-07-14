num_test_cases = int(input())

for _ in range(num_test_cases):
    n, k = map(int, input().split())
    array = [0] * n
    power = 1
    max_power_index = 0

    for i in range(31):  # Check for powers of 2 up to 2^30
        if power > k:
            break
        max_power_index = i
        power *= 2

    array[0] = (2 ** max_power_index) - 1
    remaining_sum = k - array[0]
    array[n - 1] += remaining_sum

    for element in array:
        print(element, end=" ")
