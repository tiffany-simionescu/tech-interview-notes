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

# class Stack:
#   def __init__(self):
#     self.size = 0
#     self.stack = LinkedList()

#   def __len__(self):
#     return self.size

#   def push(self, value):
#     self.size += 1
#     self.stack.add_to_head(value)

#   def pop(self):
#     if self.size == 0:
#       return None
#     self.size -= 1
#     node = self.stack.remove_head()
#     return node

# class Queue:
#   def __init__(self):
#     self.size = 0
#     self.queue = LinkedList()

#   def __len__(self):
#     return self.size

#   def enqueue(self, value):
#     # add to tail
#     self.size += 1
#     self.queue.add_to_tail(value)

#   def dequeue(self):
#     # remove from head
#     if self.size == 0:
#       return None

#     self.size -= 1
#     value = self.queue.remove_head()
#     return value

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        return None

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            node = self.storage.remove_head()
            return node
        return None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def __str__(self):
        output = ""
        current_node = self.head
        while current_node is not None:
            output += f"{current_node.value}"
            # Update the tracker node to the next node
            current_node = current_node.next_node
        return output

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

  def get_list_size(self):
        i = 0
        current_item = self.head
        if not current_item:
            return i
        while current_item is not None:
            i += 1
            current_count = i
            current_item = current_item.next_node
        return current_count

  

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
print(len(new_stack))
print(f'Removed value is {new_stack.pop()}')


# Video III

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # don't need Nones, just being explicit 
    new_node = ListNode(value, None, None)
    self.length += 1
    # if list is currently empty, add node in that case
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      # the list already has elements in it
      # make new node point to current head
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def remove_from_head(self):
    if self.head is None:
      return None
    head_value = self.head.value
    self.delete(self.head)
    return head_value

  def add_to_tail(self, value):
    new_node = ListNode(value, None, None)
    self.length += 1
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def remove_from_tail(self):
    if self.tail is None:
      return None
    tail_value = self.tail.value
    self.delete(self.tail)
    return tail_value

  def move_to_front(self, node):
    if node is self.head:
      return
    old_value = node.value
    self.delete(node)
    self.add_to_head(old_value)

  def move_to_end(self, node):
    if node is self.tail:
      return
    old_value = node.value
    self.delete(node)
    self.add_to_tail(old_value)

  def delete(self, node):
    # the list is empty - do nothing
    if self.head is None and self.tail is None:
      return
    # the list is only one node
    self.length -= 1
    if self.head == self.tail and node == self.head:
      self.head = None
      self.tail = None
    # the node is the head node 
    if self.head == node:
      self.head = node.next 
      node.delete() 
    # the node is the tail node
    if self.tail == node:
      self.tail = node.prev
      node.delete()
    # the node is just some node in the list
    else:
      node.delete()

  def get_max(self):
    if self.head is None:
      return None
    max_val = self.head.value
    current = self.head
    while current:
      if current.value > max_val:
        max_val = current.value
      current = current.next
    return max_val


# Video III and IV
# BST - Binary Search Tree - value, children, no loops, only two children max

class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # O(log n) Runtime
  def insert(self, value):
    # take the current value of our node (self.value)
    # compare to the new value we want to insert

    if value < self.value:
      # if self.left is already taken by a node
        # make that node call insert
      # set the left to the new node with new value
      if self.left is None:
        self.left = BSTNode(value)
      else:
        self.left.insert(value)

    if value >= self.value:
      # if self.right is already taken by a node
        # make that node call insert
      # set the right child to the new node with new value
      if self.right is None:
        self.right = BSTNode(value)
      else:
        self.right.insert(value)


  def contains(self, target):
    if self.value == target:
      return True
 
    if self.value >= target:
      if self.left is None:
        return False
      return self.left.contains(target)

    if self.value < target:
      if self.right is None:
        return False
      return self.right.contains(target)


  def get_max(self):
    if self.right is None:
      return self.value
    return self.right.get_max()
  
  # DFT
  def for_each(self, fn):
    # This will print in DFT
    # fn(self.value)

    if self.left:
      self.left.for_each(fn)
    # This will print in BFT
    fn(self.value)

    if self.right:
      self.right.for_each(fn)


  def in_order_print(self, node):
    pass

  def bft_print(self, node):
    # create a queue for nodes
    queue = Queue()
    # add the first node to the queue
    queue.enqueue(node)
    # while the queue is not empty
    while queue.size > 0:
      # remove the first node from the queue
      cur_node = queue.dequeue()
      # print the removed node
      print(cur_node.value)
      # add all children into the queue
      if cur_node.left:
        queue.enqueue(cur_node.left)
      if cur_node.right:
        queue.enqueue(cur_node.right)


  def dft_print(self, node):
    # create a stack for nodes
    stack = Stack()
    # add the first node to the stack
    stack.push(node)
    # while the stack is not empty
    while stack.size > 0:
      # get the current node from the top of the stack
      cur_node = stack.pop()
      # print that node
      print(cur_node.value)
      # add all children to the stack (order matters)
      if cur_node.right:
        stack.push(cur_node.right)
      if cur_node.left:
        stack.push(cur_node.left)

root_node = BSTNode(8)
root_node.insert(3)
root_node.insert(10)
root_node.insert(9)
root_node.insert(12)
root_node.bft_print
root_node.dft_print

# print_node = lambda x: print(x)

# root_node.for_each(print_node)