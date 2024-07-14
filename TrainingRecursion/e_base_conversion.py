def base_conversion(n: int):
    if n <= 0:
        return
    digit = n % 2
    response.append(str(digit))
    base_conversion(n // 2)

    return


t = int(input())

for _ in range(t):
    n = int(input())
    response = list()
    base_conversion(n)
    response = reversed(response)
    print("".join(response))