
# To solve this problem, we need to arrange the numbers in such a way that they form the largest possible concatenated number. The trick is to sort the numbers based on custom logic rather than their numeric value. We can achieve this using a custom sorting function that determines the order based on which concatenation results in a larger value.
#
# Approach
#
	# 1.	Convert Numbers to Strings: Convert all integers in nums to strings for easy concatenation.
	# 2.	Sort Using a Custom Key: Use a lambda function as the key for sorting.
#           The lambda function will sort based on which of two concatenated values (x + y or y + x) is larger.
	# 3.	Join the Numbers: Once sorted, join the numbers together to form the final result.
	# 4.	Handle Edge Cases: If the result starts with '0', return "0" as all numbers are zeros.

class Solution(object):
    def largestNumber(self, nums):
        # Convert all numbers to strings
        nums = [str(num) for num in nums]

        # Sort the numbers using the custom key
        nums.sort(key=lambda x: x * 10, reverse=True)

        # Join the sorted numbers
        largest_num = ''.join(nums)

        # If the result starts with '0', the entire number is '0'
        return '0' if largest_num[0] == '0' else largest_num
# ------------------------- Explaination ------------------------
# Explanation
#
# 	1.	Convert Numbers to Strings:
# 	•	Convert each integer in the array to a string so that they can be concatenated and compared.
# 	2.	Custom Sorting Using Nested Loops:
# 	•	We use a nested loop to compare each pair of strings nums[i] and nums[j].
# 	•	For each pair, we concatenate them in both possible orders: nums[i] + nums[j] and nums[j] + nums[i].
# 	•	If nums[j] + nums[i] is greater, we swap them to ensure that the larger concatenation comes first.
# 	•	This results in sorting the array in descending order based on the custom comparison.
# 	3.	Join the Sorted Numbers:
# 	•	After sorting, we join the elements of nums into a single string to form the largest number.
# 	4.	Handle Edge Case:
# 	•	If the resulting string starts with '0', it means all elements in nums were zero, so we return "0".


# -------------------------- Complexity ------------------------
# 	•	Time Complexity: O(n^2) due to the nested loop used for sorting.
#   	Although not as efficient as using Python’s built-in sort method, this approach is simple and straightforward.
# 	•	Space Complexity: O(n), since we convert the integers to strings and store them in a list.

# ------------------- Testing --------------------
solution = Solution()

# Example 1
print(solution.largestNumber([10, 2]))  # Output: "210"

# Example 2
print(solution.largestNumber([3, 30, 34, 5, 9]))  # Output: "9534330"

# Example 3
print(solution.largestNumber([0, 0]))  # Output: "0"
