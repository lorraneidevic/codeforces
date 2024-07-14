def print_recursion(n: int, count: list) -> list:
    if n <= 0:
        return count
    count.append(str(n))
    print_recursion(n - 1, count)
    return count


input = int(input())
response = print_recursion(input, list())

print(" ".join(response))
