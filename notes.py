# 10/13/2020
# Can you reverse a linked list

def reverse_list(head):
	prev = None
	cur = head
	while cur is not None:
		old_next = cur.next
		cur.next = prev  # Reverse the pointer
		prev = cur
		cur = old_next
	return prev

# Is it a valid BST?

class Node:
	def __init(self, data):
		self.data = data
		self.left = None
		self.right = None

def checkBST(root):
	# check if value of node is in acceptable range (0 < val < 10**4)
	# if so, recurse on left/right
	# otherwise return false

	# do a traversal check as we go
	# come up with a path through the tree
	# print/put in array node values as we go
	# resulting array should be in order

	# recursive apprach
	# if there's a left child, recurse left
	# then add self to array (or if ther's no left child)
	# then if there's right child, recurse right
	# return array

	# then check that the array is in order

	# when we return value from a left recursion, could we check then 	that all values < current_node?
		# This won't check all subtrees against root node
  pass