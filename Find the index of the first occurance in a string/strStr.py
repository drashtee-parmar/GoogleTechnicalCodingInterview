# # ---------------- What approach to take? -------------------
# To solve this problem, we need to find the index of the first occurrence of the substring needle in the string haystack. If needle is not found, we return -1. Python provides multiple ways to achieve this efficiently. Below is an implementation that uses Python’s in-built features as well as an explanation of a more efficient algorithm called the Knuth-Morris-Pratt (KMP) algorithm, which is ideal for this kind of task.
#
# Simple Python Implementation
#
# Python has a built-in method, str.find(), which does exactly what we need, but to demonstrate how to solve this problem manually, here’s a straightforward implementation using a sliding window approach:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If the needle is an empty string, return 0
        if not needle:
            return 0

        # Get the lengths of both haystack and needle
        haystack_len = len(haystack)
        needle_len = len(needle)

        # Iterate through haystack with a window the size of the needle
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring matches the needle
            if haystack[i:i + needle_len] == needle:
                return i

        # If no match is found, return -1
        return -1

# --------------------- Explaination -----------------------
# 1.	Check if Needle is Empty:
# 	•	If needle is an empty string, the function returns 0 as per the problem constraints (though typically, needle will not be empty given the constraints).
# 	2.	Length Calculation:
# 	•	Compute the lengths of haystack and needle for later use.
# 	3.	Iterate Through Haystack:
# 	•	Iterate through the haystack string from index 0 to haystack_len - needle_len + 1 to create a sliding window of size equal to the length of needle.
# 	•	For each index i, check if the substring of haystack from i to i + needle_len matches needle.
# 	•	If a match is found, return i as the starting index of the first occurrence.
# 	4.	Return -1 If Not Found:
# 	•	If the loop completes without finding a match, return -1.

# --------------------- Complexity -----------------------
# 	•	Time Complexity: O((n - m + 1) \times m) \approx O(n \times m), where n is the length of haystack and m is the length of needle.
# 	In the worst case, every substring of length m in haystack needs to be checked against needle.
# 	•	Space Complexity: O(1), as no extra space proportional to the input size is used.

# --------------------- Testing -----------------------

solution = Solution()

# Example 1
print(solution.strStr("sadbutsad", "sad"))  # Output: 0

# Example 2
print(solution.strStr("leetcode", "leeto")) # Output: -1

# Example 3
print(solution.strStr("hello", "ll"))       # Output: 2
