def is_palindrome(s):
  
   # if len(s) <= 1:
   #  return True
   
   # if s[0] != s[-1]:
   #    return False
    
   # return is_palindrome(s[1:-1])
  i = 0
  j = len(s) - 1

  while i < j:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1
  return True
