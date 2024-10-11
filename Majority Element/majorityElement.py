# ---------------- What approach to use -------------------
# To solve the problem of finding the majority element, which appears more than ⌊n / 2⌋ times in the array, we can use the Boyer-Moore Voting Algorithm. This algorithm works in linear time (O(n)) and uses constant space (O(1)), making it an efficient solution for this problem.
#
# Boyer-Moore Voting Algorithm
#
# The idea is to keep a candidate for the majority element and a count that tracks the net balance of this candidate. Here’s how it works:
#
# 	1.	Initialization: Set the candidate to None and count to 0.
# 	2.	Iterate through the array:
# 	•	If count is 0, set the current number as the candidate.
# 	•	If the current number is the same as the candidate, increment count.
# 	•	If the current number is different from the candidate, decrement count.
# 	3.	Return the candidate after the loop. Since we are guaranteed that a majority element exists, the candidate at the end of the loop will be the majority element.
#

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
# --------------------- Explaination -----------------------
# 	1.	Initialization:
# 	•	candidate is set to None initially, and count is set to 0.
# 	2.	Iterating Through the Array:
# 	•	If count is 0, we set the current element as the new candidate.
# 	•	If the current element matches the candidate, we increment count.
# 	•	If it doesn’t match, we decrement count.
# 	3.	Return the Candidate:
# 	•	The candidate left at the end of the iteration is guaranteed to be the majority element because it appears more than ⌊n / 2⌋ times.

# --------------------- Complexity -----------------------
# 	Time Complexity: O(n), where n is the length of the array. We only traverse the array once.
# 	Space Complexity: O(1), as we only use a few variables (candidate and count), regardless of the input size.

# --------------------- Testing -----------------------
solution = Solution()

# Example 1
print(solution.majorityElement([3, 2, 3]))  # Output: 3

# Example 2
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2

# Example 3
print(solution.majorityElement([1]))  # Output: 1
