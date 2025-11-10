# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def tree_value_count(root, target):
  if root is None:
    return 0
  count = 0
  queue = deque([root])

  while queue:
    node = queue.popleft()
    if node.val == target:
      count += 1
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)

  return count
# def tree_value_count(root, target):
#   if root is None:
#     return 0
#   root_match = 1 if root.val == target else 0
#   return root_match + tree_value_count(root.left, target) + tree_value_count(root.right, target)





























  

