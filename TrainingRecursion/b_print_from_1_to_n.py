def print_recursion(n: int, count: int = 1):
    if n <= 0:
        return
    print(count)
    print_recursion(n - 1, count + 1)


input = int(input())
print_recursion(input)
