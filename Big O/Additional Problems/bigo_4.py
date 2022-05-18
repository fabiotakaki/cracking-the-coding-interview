# The following code performs integer division. What is ts runtime (assume a and b are both positive)?
# Answer: O(a/b)
def div(a:int, b:int) -> int:
    count = 0
    sum = b
    while(sum <= a):
        sum += b
        count += 1
    return count