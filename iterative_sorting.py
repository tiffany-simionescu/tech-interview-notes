# Linear Search - O(n) (sequential) searching one by one starting at first index
def linear_search(arr, target):
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
  return -1 # not found

# Binary Search - O(log n) start with the middle index to eleminate half of list
def binary_search(arr, target):
  low = 0
  high = len(arr) - 1
  while low <= high:
    middle = (low + high) // 2
    if target < arr[middle]:
      high = middle - 1
    elif target > arr[middle]:
      low = middle + 1
    else:
      return middle
  return -1

my_arr = [1, 2, 3, 6, 8, 10, 20, 23, 25]
print(binary_search(my_arr, 20))

# iteratative algorithm - repeat one or many steps until a process is done

# Insertion Sort - O(n^2) Quadratic
  # one item is always sorted, so first element is already sorted
  # left side is sorted, and you need to move one element from the right into the sorted left
  # switch elements till in correct position and move position of sorted elements
def insertion_sort(list_to_sort):
  # the first element is already in the "sorted side"
  # for all other items, we should do things
  # starting at the second item, iterate until end of array
  for i in range(1, len(list_to_sort)):
    # the current number at the index, represents the value currently being sorted
    current_num = list_to_sort[i]
    # move the current number back through the array ( to the sorted side )
    j = i
    # keep moving until: it's greater than the number before it OR we reach the start of the array
    while j > 0 and current_num < list_to_sort[j-1]:
      # replace the current value and the one to left of it
      list_to_sort[j] = list_to_sort[j-1]
      j -= 1
    # set the value at the current index to the current number
    # at this moment, J represents the new location for the current number
    list_to_sort[j] = current_num
  
  return list_to_sort

print(insertion_sort([8, 4, 2, 5, 1, 3]))

# Selection Sort - 
  # find the number smaller than the cur_index and swap
  # move cur-index by one and repeat the above
  # if the cur-index is the smallest do nothing and move to next index

# Bubble Sort - 
  # check two cards 
  # if 2nd element is smaller, swap
  # move one index
  # repeat the above until you don't have to swap anymore


