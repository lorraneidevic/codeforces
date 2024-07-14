# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(message, K):
    if not message or len(message) == 0:
        return "..."
    if len(message) <= K:
        return message

    words = message.split()

    if len(words[0]) > K:
        return "..."

    cut_word = message[:K].rsplit(' ', 1)[0]

    if len(cut_word + " ...") <= K:
        return cut_word + " ..."
    else:
        return cut_word[:K].rsplit(' ', 1)[0] + " ..."


print(solution("", 15))  # expected ...
print(solution("...", 15))  # expected ...
print(solution(None, 15))  # expected ...
print(solution("And", 3))  # expected And
print(solution("And", 500))  # expected And
print(solution("super", 3))  # expected ...
print(solution("And now here is my secret", 15))  # expected And now ...
print(solution("And now her is my secret", 150))  # expected And now her...
print(solution("There is an animal with four legs", 15))  # expected And now ...
