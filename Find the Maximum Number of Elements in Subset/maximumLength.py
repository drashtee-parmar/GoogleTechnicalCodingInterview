
# The problem requires finding the maximum length of a subset of nums that satisfies a specific pattern: [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x], where k is any non-negative power of 2. This pattern forms a sequence that increases and then mirrors itself to decrease symmetrically.
#
# To solve this problem efficiently, we need to leverage the fact that every element in this pattern must be either equal to or half of the previous one. We can use a frequency count and sorting approach to find the longest subset that follows these rules.
#
# Solution Explanation
#
# 	1.	Count the Frequency:
# 	•	Use a dictionary to count the occurrences of each element in nums. This allows us to keep track of how many of each number are available for forming the sequence.
# 	2.	Sort the Unique Elements:
# 	•	Sort the unique elements of nums in ascending order. This helps us to build the sequence in increasing order and then mirror it.
# 	3.	Form the Subset:
# 	•	Iterate through the sorted elements and try to form the sequence [x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x].
# 	•	At each element, check if its double is available in the frequency dictionary and can be used to extend the sequence.
# 	4.	Compute the Maximum Length:
# 	•	Keep track of the maximum length of any valid subset formed following these rules.

# NOt workig properly

from typing import List
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Count the frequency of each number in nums
        count = Counter(nums)

        # Sort the unique numbers
        unique_nums = sorted(count.keys())
        max_length = 1  # The minimum possible length is 1

        # Iterate through each unique number
        for num in unique_nums:
            if count[num] > 0:  # Only proceed if we have this number available
                current_length = 1
                multiplier = 2
                while num * multiplier in count and count[num * multiplier] > 0:
                    current_length += 1
                    multiplier *= 2

                # Update max_length with the maximum length of the pattern found
                max_length = max(max_length, current_length)

        return max_length
