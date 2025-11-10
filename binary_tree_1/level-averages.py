# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from statistics import mean
def level_averages(root):
  levels = []
  _level_averages(root, levels, 0)
  avgs = []
  
  for level in levels:
    avgs.append(mean(level))
  return avgs
  
def _level_averages(root, levels, level_num):
  if root is None:
    return 0
  if len(levels) == level_num:
    levels.append([root.val])
  else:
    levels[level_num].append(root.val)
  _level_averages(root.left, levels, level_num + 1)
  _level_averages(root.right, levels, level_num + 1)

