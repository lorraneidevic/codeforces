from functools import lru_cache

test_cases = int(input())


@lru_cache(maxsize=500)
def yes(n: int, m: int) -> bool:
    if n == m:
        return True
    if n % 3 != 0:
        return False

    return yes(n // 3, m) or yes(n // 3 * 2, m)


for _ in range(test_cases):
    n, m = [int(x) for x in input().split()]

    if yes(n, m):
        print("YES")
    else:
        print("NO")
