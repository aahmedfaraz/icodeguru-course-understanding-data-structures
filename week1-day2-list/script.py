# List

# Index    0   1   2   3   4   5
numbers = [10, 20, 30, 40, 30, 50]

# Access
print(numbers[2]) # O(1)

# Insert
numbers.append(60) # O(1) amortized
numbers.insert(0, 5) # O(n)
numbers.insert(2, 15) # O(n)
print(numbers)

# Remove
numbers.pop() # O(1)
print(numbers)
numbers.pop(0) # O(n)
print(numbers)
numbers.remove(30) # O(n)
print(numbers)

# Update
numbers[4] = 35 # O(1)
print(numbers)

# Traverse
for num in numbers: # O(n)
  print(num, '->', num * num)

# OUTPUT
# 30
# [5, 10, 15, 20, 30, 40, 30, 50, 60]
# [5, 10, 15, 20, 30, 40, 30, 50]
# [10, 15, 20, 30, 40, 30, 50]
# [10, 15, 20, 40, 30, 50]
# [10, 15, 20, 40, 35, 50]
# 10 -> 100
# 15 -> 225
# 20 -> 400
# 40 -> 1600
# 35 -> 1225
# 50 -> 2500