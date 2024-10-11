# To solve this problem efficiently with O(n) time complexity, we can use Kadane’s Algorithm. This algorithm allows us to find the maximum sum of a contiguous subarray in a single pass through the array.
#
# Kadane’s Algorithm
#
# The idea behind Kadane’s Algorithm is to keep track of the maximum sum of a subarray ending at each index, and then to keep a global maximum that stores the highest sum encountered so far. Here’s how it works:
#
# 	1.	Initialize two variables:
# 	•	current_sum to keep track of the sum of the current subarray. Initially, it is set to the first element of the array.
# 	•	max_sum to keep track of the maximum sum encountered. It is also initially set to the first element.
# 	2.	Iterate through the array starting from the second element:
# 	•	Update current_sum to be the maximum of:
# 	•	The current element itself (if starting a new subarray is better).
# 	•	The sum of current_sum plus the current element (extending the existing subarray).
# 	•	Update max_sum to be the maximum of max_sum and current_sum.
# 	3.	Return max_sum as the maximum sum of any subarray in the array.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current_sum and max_sum to the first element
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update current_sum
            current_sum = max(num, current_sum + num)
            # Update max_sum
            max_sum = max(max_sum, current_sum)

        return max_sum


# ------------------------------------------ Explanation -------------------------------------
#
# 	1.	Initialization:
# 	•	current_sum and max_sum are initialized to the first element of the array since the smallest possible subarray contains one element.
# 	2.	Iterating Through the Array:
# 	•	For each element, we decide whether to start a new subarray (num) or continue with the existing subarray (current_sum + num).
# 	•	We then update max_sum to keep track of the maximum sum encountered.
# 	3.	Return the Result:
# 	•	After iterating through the entire array, max_sum contains the largest sum of any subarray.

# Complexity
#
# 	•	Time Complexity: O(n), where n is the length of the array. The algorithm makes a single pass through the array, making it very efficient.
# 	•	Space Complexity: O(1), as we only use a few variables (current_sum and max_sum) to keep track of the running totals.

# Follow-up: Divide and Conquer Approach
#
# If you want to try a different approach, you can use a divide and conquer technique. However, it has a higher time complexity of O(n \log n) and is more complex to implement compared to Kadane’s Algorithm. Here’s the basic idea:
#
# 	1.	Divide the array into two halves.
# 	2.	Recursively find the maximum subarray sum in the left half and the right half.
# 	3.	Find the maximum subarray sum that crosses the midpoint (this requires merging the two halves).
# 	4.	Return the maximum of the three.
#
# Kadane’s Algorithm, however, is usually preferred due to its simplicity and efficiency.

# ------------------------------------ Testing -------------------------------
solution = Solution()

# Example 1
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6

# Example 2
print(solution.maxSubArray([1]))  # Output: 1

# Example 3
print(solution.maxSubArray([5, 4, -1, 7, 8]))  # Output: 23
