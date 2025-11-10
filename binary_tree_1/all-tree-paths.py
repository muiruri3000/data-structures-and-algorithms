# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
def all_tree_paths(root):
  paths = _all_tree_paths(root)
  for path in paths:
    path.reverse()
  return paths

  
def _all_tree_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]

  all_paths = []

  left_path = _all_tree_paths(root.left)
  for path in left_path:
    path.append(root.val)
    all_paths.append(path)
  
  right_path = _all_tree_paths(root.right)
  for path in right_path:
    path.append(root.val)
    all_paths.append(path)
    
  return all_paths





































  
