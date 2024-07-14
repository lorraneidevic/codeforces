test_cases = int(input())

for _ in range(test_cases):
    _ = int(input())
    s = str(input()).replace(" ", "")
    longest_blank_space = 0
    sequential_blank_space = 0

    for c in enumerate(s):
        if c == "0":
            sequential_blank_space += 1
        else:
            sequential_blank_space = 0

        if sequential_blank_space > longest_blank_space:
            longest_blank_space = sequential_blank_space

    print(longest_blank_space)
