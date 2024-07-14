def print_digits_using_recursion(digits: list, r: list):
    if len(digits) <= 0:
        return r
    r.append(digits[0])
    digits.pop(0)
    print_digits_using_recursion(digits, r)
    return r


tests = int(input())
for test in range(tests):
    n = str(input())
    digits = [digit for digit in n]
    response = print_digits_using_recursion(digits, list())

    print(" ".join(response))
