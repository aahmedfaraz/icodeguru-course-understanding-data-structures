# Time and Space complexity

# Constant Space Complexity O(1)
n = 1000

# Quadratic Time Complexity O(n^2)
count = 0
for i in range(5):          # O(n)
  for j in range(5):        # O(n)
    count += 1            # O(1)
# Total: O(n) * O(n) * O(1) = O(n^2)
print("Quadratic Count:", count)

# Cubic Time Complexity O(n^3)
count = 0
for i in range(5):          # O(n)
  for j in range(5):        # O(n)
    for k in range(5):      # O(n)
      count += 1            # O(1)
# Total: O(n) * O(n) * O(n) * O(1) = O(n^3)
print("Cubic Count:", count)

# OUTPUT - When input n = 5
# Quadratic Count: 25
# Cubic Count: 125