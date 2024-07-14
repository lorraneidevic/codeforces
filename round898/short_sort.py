input_size = int(input())

target_string = "abc"

for x in range(input_size):
    input_string = input()
    cases = []

    if input_string == target_string:
        print("YES")
        continue

    has_same_position: bool = False

    for index, c in enumerate(input_string):
        if c == target_string[index]:
            has_same_position = True

    if has_same_position:
        print("YES")
    else:
        print("NO")
