# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
# #     self.right = None
# from collections import deque
# def tree_includes(root, target):
#   if not root:
#     return False
    
#   queue = deque([root])

#   while queue:
#     current = queue.popleft()
#     if target == current.val:
#       return True

#     if current.left:
#       queue.append(current.left)
#     if current.right:
#       queue.append(current.right)
      
#   return False

def tree_includes(root,target):
  if not root:
    return False
  if root.val == target:
    return True
  return (
    tree_includes(root.left,target) or tree_includes(root.right,target)
  )





























  
