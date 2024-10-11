
#To solve the problem of finding all unique triplets in the array that sum up to zero, we can use the two-pointer approach after sorting the array. This approach works efficiently with a time complexity of O(n^2), which is optimal for this problem. Here’s how we can implement it:

# Explanation
#
# 	1.	Sort the Array:
# 	•	Sorting the array allows us to use the two-pointer technique efficiently. It also helps in avoiding duplicate triplets easily.
# 	2.	Iterate Through the Array:
# 	•	For each element in the array (nums[i]), we treat it as a potential first element of the triplet. The goal is to find two other elements (nums[left] and nums[right]) such that their sum is -nums[i].
# 	3.	Two-Pointer Technique:
# 	•	Initialize two pointers: left (pointing just after i) and right (pointing to the end of the array).
# 	•	Calculate the sum of nums[i], nums[left], and nums[right].
# 	•	If the sum is zero, we’ve found a triplet. Move both pointers inward while skipping duplicates to avoid repeating the same triplet.
# 	•	If the sum is less than zero, move the left pointer to the right to increase the sum.
# 	•	If the sum is greater than zero, move the right pointer to the left to decrease the sum.
# 	4.	Avoid Duplicates:
# 	•	If nums[i] is the same as nums[i-1], skip this iteration to prevent duplicate triplets in the result.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array
        nums.sort()
        n = len(nums)
        result = []
        # Iterate through the array
        for i in range(n):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach for the remaining part of the array
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

#     ---------------------------- Complexity ----------------------------
# Time Complexity: O(n^2)
# 	•	Sorting the array takes O(n \log n).
# 	•	The two-pointer technique iterates through the array in O(n^2) time, making this the dominant term.
# Space Complexity: O(1) for the algorithm itself, excluding the space required for the output list.
# However, sorting the array in-place may require O(\log n) space for the sorting algorithm.

# -------------------------------- Testing -------------------------------
solution = Solution()

# Example 1
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]

# Example 2
print(solution.threeSum([0, 1, 1]))
# Output: []

# Example 3
print(solution.threeSum([0, 0, 0]))
# Output: [[0, 0, 0]]
