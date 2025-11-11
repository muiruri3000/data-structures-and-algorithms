def uncompress(s):
  result = []
  numbers = '0123456789'

  j = 0
  i = 0
  while j < len(s):
    if s[j] in numbers:
      j+=1
    else:
      num = int(s[i:j])
      result.append(num * s[j])
      j+=1
      i = j
  return ''.join(result)

print(uncompress('3j4u2p'))
      
      
