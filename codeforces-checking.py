check_string = "codeforces"

input_size = int(input())

for x in range(input_size):
    input_char = input()
    if input_char in check_string:
        print("YES")
    else:
        print("NO")
