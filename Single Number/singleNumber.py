# To solve this problem with linear runtime complexity and constant space, we can use the bit manipulation approach, specifically the XOR operation.
# This approach is both efficient and straightforward.
#
# XOR Property
#
# The XOR operation (^) has several useful properties that make it ideal for solving this problem:
#
# 	1.	A number XORed with itself is 0:  a \oplus a = 0 .
# 	2.	A number XORed with 0 is the number itself:  a \oplus 0 = a .
# 	3.	XOR is commutative and associative, meaning the order of operations does not matter.
#
# Given these properties, if every element in the array appears exactly twice except for one element,
# XORing all the numbers together will cancel out the numbers that appear in pairs, leaving only the single element.
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
# --------------------------- Explaination ------------------------
# 	1.	Initialize result:
# 	•	Start with result = 0.
# 	2.	XOR All Elements in the Array:
# 	•	Iterate through each element in nums.
# 	•	XOR the current element with result.
# 	•	Since all the elements that appear twice will cancel each other out, only the single element will remain.
# 	3.	Return the Single Element:
# 	•	After the loop, result will hold the value of the element that appears only once.


# --------------------------- Complexity ------------------------
#
# 	•	Time Complexity: O(n), where n is the length of the array. We iterate through the array once,
# 	performing a constant-time operation (XOR) for each element.
# 	•	Space Complexity: O(1), since we only use a single variable (result) for storage, regardless of the size of the input.

solution = Solution()

# Example 1
print(solution.singleNumber([2, 2, 1]))  # Output: 1

# Example 2
print(solution.singleNumber([4, 1, 2, 1, 2]))  # Output: 4

# Example 3
print(solution.singleNumber([1]))  # Output: 1
