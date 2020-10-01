"""
Given a sorted array `nums`, remove the duplicates from the array.
​
Example 1:
​
Given nums = [0, 1, 2, 3, 3, 3, 4]
​
Your function should return [0, 1, 2, 3, 4]
​
Example 2:
​
Given nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
​
Your function should return [0, 1, 2, 3, 4, 5].
​
*Note: For your first-pass, an out-of-place solution is okay. However, after
solving out-of-place, try an in-place solution with a space complexity of O(1).
For that solution, you will need to return the length of the modified `nums`.
The length will tell the user where the end of the array is after removing all
of the duplicates.*
"""
# out-of-place: using extra memory
# in-place: not using extra memory
# runtime: O(n + n) = O(2 * n) = O(n)
# memory: O(n + n) = O(2 * n) = O(n)
# def remove_duplicates(nums):
#     # Your code here
#     s = set() # O(n)
#     output = [] # O(n)
​
#     # O(n)
#     for n in nums:
#         s.add(n)
​
#     # O(n)
#     for n in s:
#         output.append(n)
​
#     return output
​
​
    # return list(set(nums))
​
# memory: O(1)
def remove_duplicates(nums):
    # we'll need to remove duplicates from the input list 
    # check elements two-at-a-time, remove one of them 
    # when we see that the two elements are the same 
    # loop through the nums list
    for i in range(1, len(nums)):
        # replace duplicates with chars 
        if nums[i-1] == nums[i]:
            nums[i-1] = 'a'
    # loop through nums list again
        # remove all chars from the list 
​
​
nums = [0, 1, 1, 2, 2, 2, 3, 4, 4, 5]
remove_duplicates(nums)