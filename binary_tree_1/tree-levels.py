# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
# def tree_levels(root):
#   levels = _tree_levels(root)
#   for level in levels:
#   return levels

  
# def _tree_levels(root):
#   if root is None:
#     return []


#   levels = []
#   level_num = 0
#   stack = [(root,level_num)]
#   while stack:
#     node, level_num = stack.pop()
#     if len(levels) == level_num:
#       levels.append([node.val])
#     else:
#       levels[level_num].append(node.val)
  
#     if node.left is not None:
#       stack.append((node.left, level_num + 1))
#     if node.right is not None:
#       stack.append((node.right, level_num + 1))
#   return levels




def tree_levels(root):
  levels = []
  _tree_levels(root,levels, 0)
  return levels

def _tree_levels(root,levels, level_num):
  if root is None:
    return []
  if len(levels) == level_num:
       levels.append([root.val])
  else:
       levels[level_num].append(root.val)

  _tree_levels(root.left, levels, level_num +1)
  _tree_levels(root.right, levels, level_num +1)
  












    
  
  
