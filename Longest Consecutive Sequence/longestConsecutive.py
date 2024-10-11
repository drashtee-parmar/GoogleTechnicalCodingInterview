
# To solve the problem of finding the length of the longest consecutive sequence in an unsorted array with O(n) time complexity, we can use a hash set to achieve this efficiently. The idea is to use the hash set for constant-time lookups to find the start of each sequence and count its length.
#
# Approach
#
# 	1.	Convert the List to a Set:
# 	•	Convert nums to a set (num_set) to allow for O(1) time complexity when checking if an element exists in the set. This helps us efficiently determine the presence of consecutive numbers.
# 	2.	Find the Start of Each Sequence:
# 	•	Iterate through each number in nums. For each number, check if it is the start of a sequence. A number is the start of a sequence if num - 1 is not in the set.
# 	•	If it is the start, we count the length of the sequence by checking consecutive numbers (num + 1, num + 2, etc.) until the sequence breaks.
# 	3.	Update the Longest Sequence Length:
# 	•	Keep track of the maximum sequence length encountered during the iteration.

class Solution:
    def longestConsecutive(self, nums):
        # Convert the list to a set for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        # Iterate through each number in the set
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# --------------------------------- Explanation --------------------------------
#
# 	1.	Convert to Set:
# 	•	We convert nums to a set (num_set) for O(1) lookups.
#   	This allows us to check if a number’s predecessor (num - 1) or successor (num + 1) exists quickly.
# 	2.	Identify the Start of a Sequence:
# 	•	For each number, we check if num - 1 is not in the set. If it’s not, it means num is the start of a sequence.
# 	•	We then count how long this sequence is by checking for the presence of num + 1, num + 2, etc., in the set.
# 	3.	Update the Longest Streak:
# 	•	We track the length of the longest sequence (longest_streak) as we iterate through the set.
# 	4.	Return the Longest Streak:
# 	•	At the end, longest_streak will hold the length of the longest consecutive sequence.


# ------------------------------ Complexity ---------------------------------------
#
# 	•	Time Complexity: O(n)
# 	•	We convert the array to a set in O(n) time.
# 	•	We iterate through the set, and each number is processed at most twice (once when it’s the start of a sequence and possibly again when it extends a sequence), resulting in linear time complexity.
# 	•	Space Complexity: O(n)
# 	•	We use a set to store the elements, which requires O(n) space.

# ---------------------------- Testing --------------------------------
solution = Solution()

# Example 1
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4

# Example 2
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
