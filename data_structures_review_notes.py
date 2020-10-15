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

# Video II
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

class Stack:
  def __init__(self):
    self.size = 0
    self.stack = LinkedList()

  def __len__(self):
    return self.size

  def push(self, value):
    self.size += 1
    self.stack.add_to_head(value)

  def pop(self):
    if self.size == 0:
      return None
    self.size -= 1
    node = self.stack.remove_head()
    return node

class Queue:
  def __init__(self):
    self.size = 0
    self.queue = LinkedList()

  def __len__(self):
    return self.size

  def enqueue(self, value):
    # add to tail
    self.size += 1
    self.queue.add_to_tail(value)

  def dequeue(self):
    # remove from head
    if self.size == 0:
      return None

    self.size -= 1
    value = self.queue.remove_head()
    return value

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_head(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next_node = self.head
      self.head = new_node

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None

    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value

    head_value = self.head.value
    self.head = self.head.next_node
    return head_value

  def remove_tail(self):
    if self.head is None:
      return None

    current_node = self.head

    while current_node is not None:
      if current_node.next_node is not None:
        current_node = current_node.next_node
      else:
        current_node = self.tail.value
        self.tail = None
        return current_node


  def contains(self, value):
    if self.head is None:
      return False

    current_node = self.head

    while current_node is not None:
      if current_node.value == value:
        return True

      current_node = current_node.next_node

    return False

  

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Needs a cache to store numbers
        # for num in nums:
        # add num to cache
        # If cache already contains the current number,
        # return True 
        # else add number to cache and move forward
        # return False
        
        cache = []
        
        for num in nums:
            if num not in cache:
                cache.append(num)
            else:
              return True
        return False


new_stack = Stack()
print(len(new_stack))
new_stack.push(2)
new_stack.push(3)
new_stack.push(5)
print(new_stack.stack)
print(len(new_stack))
print(f'Removed value is {new_stack.pop()}')