# The following code computes a^b. What is its runtime?
# Answer: O(b)

def power(a:int, b:int) -> int:
    if(b < 0):
        return 0
    elif (b == 0):
        return 1
    else:
        return a * power(a, b-1)