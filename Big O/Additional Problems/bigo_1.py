# The following code computes the product of a and b. What is its runtime?
# Answer: O(b)

def product(a:int, b:int) -> int:
    sum = 0
    for i in range(b):
        sum += a
    return sum