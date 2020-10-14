# Big O Notation

# O(1) = Constant
def print_one_item(items):
  print(items[0])

# O(n) = Linear
def print_every_item(items):
  for item in items:
    print(item)

# O(n^2) = Quadratic
def print_pairs(items):
  for item_one in items:
    for item_two in items:
      print(item_one, item_two)

# O(log n)= Logarithmic
def foo(n):
  i = 1
  while i < n:
    print(i)
    i *= 2

# Big O represents worst case scenario

# Linked Lists - elements are not physically located right next to each other
# Singly linked list - each element only knows about itself and the next linked
# node in the list

# removing an element from the end of a SLL is linear time
# have to traverse through the beginning of the SLL even if element is near tail

# Binary Search Trees - can reference up to two other nodes (left/right) 

# Left node value is less than its parent
# Right node value is more than its parent

# a search is completed when the target of the search is found
# a traversal is completed when every node has been explored

# Depth First Traversal - DFT, continues traveling forward on each branch until a
# dead end is reached. Uses a stack approach

# Breadth First Traversal - BFT, explores layer by layer. Uses a queue approach

### Review Videos for II, III, IV ###