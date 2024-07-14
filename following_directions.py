def left(position: list) -> list:
    position[0] = position[0] - 1
    return position


def right(position: list) -> list:
    position[0] = position[0] + 1
    return position


def up(position: list) -> list:
    position[1] = position[1] + 1
    return position


def down(position: list) -> list:
    position[1] = position[1] - 1
    return position


test_cases = int(input())

for x in range(test_cases):
    candy_position = [1, 1]
    alperen_initial_position = [0, 0]
    alperen_position = alperen_initial_position

    string_length = input()
    directions = input()
    passed_the_candy = False

    for d in directions:
        if d == "L":
            alperen_position = left(alperen_position)
        elif d == "R":
            alperen_position = right(alperen_position)
        elif d == "U":
            alperen_position = up(alperen_position)
        elif d == "D":
            alperen_position = down(alperen_position)

        if alperen_position == candy_position:
            passed_the_candy = True

    if passed_the_candy:
        print("YES")
    else:
        print("NO")
