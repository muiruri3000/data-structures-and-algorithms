def pair_sum(numbers, target_sum):

  #initialize an empty dictionary 
  previous_nums = {}

  # Generate a the list items with their index positions
  # also generate a partner complement
  for index,num in enumerate(numbers):
    complement = target_sum - num 

    # if complement is present in the dictionary,generate the final tuple
    if complement in previous_nums:
      return (index, previous_nums[complement])

    # in every iteration insert a num and its index.
    previous_nums[num] = index




    
  # brute force
  # time complexity: O(n^2)
  # space complexity: O(n)
  
  # for i in range(0, len(numbers)):
  #   for j in range(i +1, len(numbers)):
  #     if numbers[i] + numbers[j] == target_sum:
  #       return (i,j)


  # hashmaps is faster and better

 
  
