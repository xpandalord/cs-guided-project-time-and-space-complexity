"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.
​
Example:
​
Input: [1,3,3,2,1]
Output: True
​
Example:
​
Input: [0,1,2,3]
Output: False
​
*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""
# O(1) + O(n) + O(1) + O(1) = O(n)
def contains_duplicate(nums):
    # Your code here
    # return len(nums) != len(set(nums))
​
    # s = set() # O(1)
    # # O(n)
    # for n in nums:
    #     s.add(n) # O(1)
​
    # # what's the runtime of `len` 
    # # `len` is an O(1) function 
    # return len(nums) != len(s)    
​
    # O(n log n) + O(n) = O(n log n)
    # if we sort our nums 
    # nums.sort() # O(n^2) > O(n log n) > O(n)
​
    # O(n)
    # for i in range(1, len(nums)):
    #     if nums[i-1] == nums[i]: # O(1)
    #         return True
    # return False 
​
    # O(n) + O(n) = O(n + n) = O(2 * n) = O(n)
    nums_count = {}
​
    # O(n)
    for n in nums:
        if n in nums_counts: # O(1)
            nums_count[n] += 1
        else:
            nums_count[n] = 1
​
    # O(n)
    for n in nums_count:
        if nums_counts[n] > 1: # O(1)
            return True
​
    return False