test_cases = int(input())

for x in range(test_cases):
    string_length = int(input())
    final_string = input()
    match = 0

    i = 0
    j = string_length - 1

    while i < j:
        if final_string[i] != final_string[j]:
            match += 1
        else:
            break
        i += 1
        j -= 1

    print(string_length - (match * 2))
