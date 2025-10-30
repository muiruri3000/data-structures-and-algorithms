from collections import Counter
def intersection_with_dupes(a, b):
  counter_a = Counter(a)
  counter_b = Counter(b)
  result = []


  for ele in counter_a:
    for i in range(0, min(counter_a[ele], counter_b[ele])):
      result.append(ele)
  return result

print(intersection_with_dupes(
 ["q", "b", "m", "s", "s", "s"], 
  ["s", "m", "s"]
))
