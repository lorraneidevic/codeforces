for _ in range(int(input())):
    response = 0

    for i in range(10):
        row = input()
        for j in range(10):
            if row[j] == 'X':
                response += min(i+1, j+1, 10-i, 10-j)

    print(response)