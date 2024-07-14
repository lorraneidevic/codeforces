from collections import deque


def bfs(x, y) -> int:
    search_queue = deque()
    search_queue.append((x, y))
    total = lakes[x][y]
    lakes[x][y] = 0

    while search_queue:
        x, y = search_queue.pop()

        for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
            if 0 <= nx < n and 0 <= ny < m and lakes[nx][ny] > 0:
                total += lakes[nx][ny]
                lakes[nx][ny] = 0
                search_queue.append((nx, ny))

    return total


t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]

    lakes = [[int(x) for x in input().split()] for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    sum_lakes = [0]
    for x in range(n):
        for y in range(m):
            if lakes[x][y] > 0:
                sum_lakes.append(bfs(x, y))

    print(max(sum_lakes))
