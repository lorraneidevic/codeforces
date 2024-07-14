def print_recursion(n: int):
    if n <= 0:
        return
    print("I love Recursion")
    print_recursion(n - 1)


input = int(input())
print_recursion(input)
