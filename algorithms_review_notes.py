# Video I
# Even though Big O is measured in worse case scenario
# we also want to consider average case scenarios

# n is the input size

# Constant - O(1)
def print_num(n):
  print(n)

def print_num_1000(n):
  for _ in range(1000):
    print(n)


# Linear - O(n)
def print_num_n_times(n):
  for _ in range(n):
    print(n)

def print_num_n_times_modified(n):
  # linear
  for _ in range(n):
    print(n)
    # constant
    for _ in range(1000):
      print(n)

# Polynomial - O(n^2)
animals = ['wolf', 'fox', 'lion', 'tiger', 'horse', 'cat']

def print_animal_pairs():
  # linear
  for animal_1 in animals:
    # linear
    for animal_2 in animals:
      print(f"{animal_1} and {animal_2}")

# print_animal_pairs()

# Logarithmic - O(log n) = reduce data in half (don't have to search all data)
def free_animals(animals):
  while len(animals) > 0:
    # removing half numbers in each iteration
    animals = animals[0: len(animals) // 2]
    print(animals)

free_animals(animals)


import random
import time

my_range = 100000000
my_size = 15

random_nums = random.sample(range(my_range), my_size)
# print(random_nums)

# O(n) - Linear Time
num_to_find = 1256
def linear_search(arr, target):
  for num in arr:
    if num == target:
      return True
  return False

print(linear_search(random_nums, num_to_find))

random_nums.sort()
print(random_nums)

# Logarithmic - O(log n)
def binary_search(arr, target):
  start = 0
  end = (len(arr) - 1)
  found = False

  while end <= start and not found:
    middle_index = (start + end) // 2

    if arr[middle_index] == target:
      found = True

    else:
      if target < arr[middle_index]:
        end = middle_index - 1
      if target > arr[middle_index]:
        start = middle_index + 1

  return found

# print(binary_search(random_nums, 12))

print("Linear")
start = time.time()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end - start}")