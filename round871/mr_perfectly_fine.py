test_cases = int(input())
oo = 200000000

for _ in range(test_cases):
    books_available = int(input())
    total_minutes_1 = oo
    total_minutes_2 = oo
    total_minutes_12 = oo
    for _ in range(books_available):
        minutes, skills = input().split()
        minutes = int(minutes)

        if skills == "01" and minutes < total_minutes_1:
            total_minutes_1 = minutes
        elif skills == "10" and minutes < total_minutes_2:
            total_minutes_2 = minutes
        elif skills == "11" and minutes < total_minutes_12:
            total_minutes_12 = minutes

    if (total_minutes_1 < oo and total_minutes_2 < oo) or total_minutes_12 < oo:
        print(min(total_minutes_1 + total_minutes_2, total_minutes_12))
    else:
        print(-1)
