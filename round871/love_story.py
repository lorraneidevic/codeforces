test_cases = int(input())

codeforces = "codeforces"

for x in range(test_cases):
    string = str(input())
    total = 0
    for si, ci in zip(string, codeforces):
        total += si != ci

    print(total)
