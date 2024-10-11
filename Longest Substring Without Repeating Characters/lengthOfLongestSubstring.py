# To find the length of the longest substring without repeating characters, we can use a sliding window approach with a hash map (dictionary) to keep track of the characters and their latest positions. This method allows us to efficiently find the longest substring without repeating characters in O(n) time complexity.
#
# Approach
#
# 	1.	Use a Hash Map:
# 	•	We use a dictionary to store the characters in the current substring and their most recent index in the string.
#   	This helps us quickly determine if a character is repeated within the current window.
# 	2.	Sliding Window Technique:
# 	•	We maintain two pointers, left and right, representing the current window of non-repeating characters.
#   	right expands the window by iterating through the string, while left contracts it when a repeated character is found.
# 	•	If a character is repeated (i.e., it is already in the dictionary and its index is within the current window),
#   	move the left pointer to one position after the previous occurrence of that character.
# 	•	Always update the character’s index in the dictionary to the current position.
# 	•	Calculate the length of the current substring (right - left + 1) and update the maximum length found so far.
# 	3.	Return the Maximum Length:
# 	•	After iterating through the string, the maximum length recorded will be the length of the longest substring without repeating characters.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last index of each character
        char_index = {}
        max_length = 0
        left = 0

        # Iterate through the string
        for right in range(len(s)):
            char = s[right]

            # If the character is in the dictionary and within the current window, move left pointer
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Update the character's latest index
            char_index[char] = right

            # Calculate the length of the current substring and update max_length
            max_length = max(max_length, right - left + 1)

        return max_length

#  ---------------------------- Explaination ----------------------------
# 1.	Dictionary Initialization:
# 	•	char_index is used to store the last seen index of each character.
# 	•	max_length keeps track of the maximum length of substrings found so far.
# 	•	left is the start of the sliding window.
# 	2.	Sliding Window Expansion:
# 	•	As right expands to include new characters, we check if the character is already in char_index and within the current window (left to right).
# 	•	If it is, move left to the right of the previous occurrence of the character (char_index[char] + 1).
# 	3.	Update the Character’s Index:
# 	•	We update the index of the current character in char_index to the current right position.
# 	4.	Calculate the Length:
# 	•	The length of the current substring is right - left + 1. We update max_length if this length is greater than the previous max_length.

# --------------------------- Complexity --------------------
#
# 	•	Time Complexity: O(n), where n is the length of the string.
# 	    Each character is processed at most twice (once when expanding right and at most once when contracting left),
#   	making the algorithm efficient.
# 	•	Space Complexity: O(min(n, m)), where m is the size of the character set (in this case, 128 for ASCII characters).
#   	The dictionary stores up to m characters.


solution = Solution()

# Example 1
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3

# Example 2
print(solution.lengthOfLongestSubstring("bbbbb"))     # Output: 1

# Example 3
print(solution.lengthOfLongestSubstring("pwwkew"))    # Output: 3
