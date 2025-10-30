def intersection(a, b):
  set_elements = set(a)
  # resultss = []
  # for elem in b:
  #   if elem in set_elements:
  #     resultss.append(elem)
  # return resultss

  
  return [elem for elem in b if elem in set_elements]
