def recursion(index: int):
    if index < 0:
        return
    if index == 0:
        print(numbers_arr[index], end=" ")
    elif index % 2 == 0:
        print(numbers_arr[index], end=" ")
    recursion(index - 1)


tests = int(input())

numbers = str(input())
numbers_arr: list[str] = numbers.split(" ")

recursion(len(numbers_arr) - 1)
