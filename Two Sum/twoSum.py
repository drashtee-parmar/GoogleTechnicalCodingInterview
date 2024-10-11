# --------------------------- Approaches ----------------
# This approach works when the array is sorted or can be sorted. Here’s how it works:
#
# Two-Pointer Approach
#
# 	1.	Sort the Array (While Keeping Track of Original Indices):
# 	•	We first create a list of tuples where each tuple contains the number and its original index from the input array.
# 	•	We then sort this list based on the numbers.
# 	2.	Use Two Pointers:
# 	•	We use two pointers, one starting at the beginning (left) and one at the end (right) of the sorted list.
# 	•	We calculate the sum of the numbers at these two pointers.
# 	•	If the sum equals the target, we return the indices of these two numbers.
# 	•	If the sum is less than the target, we move the left pointer to the right to increase the sum.
# 	•	If the sum is greater than the target, we move the right pointer to the left to decrease the sum.

class Solution:
    def twoSum(self, nums, target):
        # Create a list of tuples (number, index) using a simple for loop
        nums_with_index = []
        for i in range(len(nums)):
            nums_with_index.append((nums[i], i))

        # Sort the list of tuples based on the numbers
        nums_with_index.sort()

        # Initialize two pointers
        left, right = 0, len(nums) - 1

        # Iterate while the left pointer is less than the right pointer
        while left < right:
            left_num, left_index = nums_with_index[left]
            right_num, right_index = nums_with_index[right]

            # Calculate the sum of the numbers at the left and right pointers
            current_sum = left_num + right_num

            # If we find the target sum, return the indices
            if current_sum == target:
                return [left_index, right_index]
            # If the sum is less than the target, move the left pointer to the right
            elif current_sum < target:
                left += 1
            # If the sum is greater than the target, move the right pointer to the left
            else:
                right -= 1
# ------------------ Explaination ----------------
# 1.	Creating the List of Tuples:
# 	•	We use a simple for loop to iterate through the nums array and create a list of tuples where each tuple contains the number and its index.
# 	2.	Sorting the Array:
# 	•	We then sort the list based on the numbers, keeping track of the original indices.
# 	3.	Using Two Pointers:
# 	•	The left pointer starts at the beginning of the sorted list, and the right pointer starts at the end.
# 	•	We calculate the sum of the numbers at the two pointers (left_num and right_num).
# 	•	If the sum matches the target, we return the indices of these two numbers.
# 	•	If the sum is less than the target, we move the left pointer to the right to increase the sum.
# 	•	If the sum is greater than the target, we move the right pointer to the left to decrease the sum.

# --------------------- Complexity --------------------
# Complexity:
#
# 	•	Time Complexity: O(n \log n), due to sorting the array.
# 	•	Space Complexity: O(n), for storing the sorted list with indices.

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
