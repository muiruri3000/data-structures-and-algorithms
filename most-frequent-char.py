def most_frequent_char(s):
  count = counter(s)
  best = None

  for char in s:
    if best is None or count[char] > count[best]:
      best = char
  return best


def counter(s):
  count = {}
  for char in s:
    if char not in count:
      count[char] = 0
    count[char] += 1
  return count

print(most_frequent_char('deafjam'))
