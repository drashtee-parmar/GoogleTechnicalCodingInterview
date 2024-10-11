# # ---------------- What approach to take? -------------------
# To determine if an integer n is a power of two without using loops or recursion, we can leverage a bit manipulation approach. This is efficient and elegant, using properties of binary numbers.
#
# Bit Manipulation Approach
#
# A number is a power of two if it has exactly one bit set in its binary representation. For example:
#
# 	•	1 (which is 2^0) is 0001 in binary.
# 	•	2 (which is 2^1) is 0010 in binary.
# 	•	4 (which is 2^2) is 0100 in binary.
#
# Key Observation
#
# If n is a power of two, then n & (n - 1) should be 0:
#
# 	•	This works because n - 1 flips all bits after the rightmost set bit in n, turning it into a sequence of 1s.
# 	•	For instance:
# 	•	If n = 4 (which is 0100), then n - 1 is 0011.
# 	•	The operation 0100 & 0011 results in 0000.
#
# Additionally, this condition only holds if n > 0.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
# --------------------- Explaination -----------------------
# 1.	Check if n is Positive:
# 	•	If n is not positive (i.e., n <= 0), return False since powers of two are positive numbers.
# 	2.	Bitwise Check:
# 	•	(n & (n - 1)) == 0 checks if n has exactly one bit set.
# 	•	If this condition is True, then n is a power of two.

# --------------------- Complexity -----------------------
# Complexity
#
# 	•	Time Complexity: O(1), as the operation is performed in constant time regardless of the value of n.
# 	•	Space Complexity: O(1), since no additional space proportional to the input size is used.

solution = Solution()

# Example 1
print(solution.isPowerOfTwo(1))  # Output: True

# Example 2
print(solution.isPowerOfTwo(16)) # Output: True

# Example 3
print(solution.isPowerOfTwo(3))  # Output: False

# Example 4
print(solution.isPowerOfTwo(0))  # Output: False

# Example 5
print(solution.isPowerOfTwo(-2)) # Output: False
