def little_girl_codeforces():
    size, queries = str(input()).split(" ")
    arr = sorted(str(input()).split(" "))
    for _ in range(int(queries)):
        query = str(input()).split(" ")

  arr_empty = [0] * (
      len(arr) + 1
  )  # remove last one later to remove the need to check for arr size
  accum = 0
  total = 0

  for query in queries:
      l = query[0]
      r = query[1]
      arr_empty[l - 1] += 1
      arr_empty[r] -= 1

  arr_empty.pop()

  for i in range(len(arr_empty)):
      arr_empty[i] += accum
      accum = arr_empty[i]

  arr_empty = sorted(arr_empty, reverse=True)
  for i in range(len(arr_empty)):
      total += arr_empty[i] * arr[i]
      print(arr_empty)
      print(accum)

  print(total)

little_girl_codeforces()
