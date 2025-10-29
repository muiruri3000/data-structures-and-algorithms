def pair_product(numbers, target_product):

  number_product = {}

  for index, num in enumerate(numbers):
    complement = target_product / num

    if complement in number_product:
      return (index, number_product[complement])

    number_product[num] = index
    

    
  # bruteforce
  # for i in range(0, len(numbers)):
  #   for j in range(i+1, len(numbers)):
  #     if numbers[i] * numbers[j] == target_product:
  #       return (i,j)

print(pair_product([3, 2, 5, 4, 1], 8))
      
