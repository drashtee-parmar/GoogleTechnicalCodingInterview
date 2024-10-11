class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)

        # Loop until one of the strings is exhausted
        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append the remaining characters from word1 or word2
        if i < len1:
            merged.append(word1[i:])
        if j < len2:
            merged.append(word2[j:])

        # Join the list into a string and return
        return ''.join(merged)

# --------------------------------------------- Explaination -----------------------------------------------
# 1.	Initialization:
# 	•	We create an empty list merged to hold the characters of the merged string.
# 	•	We initialize two pointers i and j to keep track of our current position in word1 and word2, respectively.
# 	•	We also calculate the lengths of word1 (len1) and word2 (len2) for easier comparison.
# 	2.	Merging Characters Alternately:
# 	•	We use a while loop to iterate until one of the strings is exhausted.
# 	•	In each iteration, we append the character from word1 at position i and from word2 at position j to the merged list.
# 	•	We then increment both pointers (i and j) to move to the next character.
# 	3.	Appending Remaining Characters:
# 	•	After the loop, if there are any remaining characters in word1 (i.e., i < len1), we append them directly to merged.
# 	•	Similarly, if there are remaining characters in word2 (i.e., j < len2), we append them.
# 	4.	Returning the Result:
# 	•	We use ''.join(merged) to combine all elements in the merged list into a single string and return it.

# --------------------------------------------- complexity -----------------------------------------------
# Time Complexity: O(n + m), where n is the length of word1 and m is the length of word2.
# We iterate through each character in both strings once.

# Space Complexity: O(n + m), as we store the merged result in a list that has a length equal to the sum of the lengths of word1 and word2.

# --------------------------------------------- Testing ----------------------------------------------------------------
solution = Solution()

# Example 1
print(solution.mergeAlternately("abc", "pqr"))  # Output: "apbqcr"

# Example 2
print(solution.mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"

# Example 3
print(solution.mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
