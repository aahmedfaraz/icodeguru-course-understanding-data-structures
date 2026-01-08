# Time and Space complexity

# Constant Space Complexity O(1)
n = 1000

# Quadratic Time Complexity O(n^2)
count = 0
for i in range(5):          # O(n)
  for j in range(5):        # O(n)
    count += 1            # O(1)
# Total: O(n) * O(n) * O(1) = O(n^2)
print("Quadratic Count - when n=5:", count)

# Cubic Time Complexity O(n^3)
count = 0
for i in range(5):          # O(n)
  for j in range(5):        # O(n)
    for k in range(5):      # O(n)
      count += 1            # O(1)
# Total: O(n) * O(n) * O(n) * O(1) = O(n^3)
print("Cubic Count - when n=5:", count)

# Logarithmic Time Complexity O(log n)
import math
n = 16
count = 0
while n > 1:               # O(log n)
  n = n // 2               # O(1)
  count += 1               # O(1)
# Total: O(log n) * O(1) * O(1) = O(log n)
print("Logarithmic Count - when n=16:", count)

# Exponential Time Complexity O(2^n)
# fibonacci function
count = 0

def fibonacci(n):
    global count
    count += 1               # O(1) → counting each function call
    if n <= 1:               # O(1) → base case check
        return n
    # Two recursive calls → exponential growth
    return fibonacci(n - 1) + fibonacci(n - 2)
    # Overall time complexity: O(2^n)

fibonacci(5)
print("Fibonacci(5) calls:", count)

count = 0
fibonacci(10)
print("Fibonacci(10) calls:", count)



# Factorial Time Complexity O(n!)
count = 0
def factorial(n):
    global count
    count += 1               # O(1) → counting each function call
    if n == 0 or n == 1:     # O(1) → base case check
        return 1
    result = 0
    for i in range(n):       # O(n) → loop for each recursive call
        result += factorial(n - 1)
    return result
    # Overall time complexity: O(n!)
factorial(5)
print("Factorial(5) calls:", count)
count = 0
factorial(10)
print("Factorial(10) calls:", count)

# OUTPUT
# Quadratic Count - when n=5: 25
# Cubic Count - when n=5: 125
# Logarithmic Count - when n=16: 4
# Fibonacci(5) calls: 15
# Fibonacci(10) calls: 177
# Factorial(5) calls: 206
# Factorial(10) calls: 6235301