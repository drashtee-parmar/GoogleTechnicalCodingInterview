#
#To reverse a signed 32-bit integer while ensuring the reversed integer stays within the 32-bit range, we need to handle a few specific cases carefully. Let’s go through a step-by-step approach to implement this.

# Approach
#
# 	1.	Handle the Sign:
# 	•	If the input x is negative, we store the sign separately and work with the absolute value.
#   	At the end, we reapply the sign to the reversed number.
# 	2.	Reverse the Digits:
# 	•	Convert the integer to a string and reverse the characters.
#   	Alternatively, extract each digit using modulo (%) and integer division (//) to build the reversed number.
# 	3.	Check the 32-bit Boundaries:
# 	•	A 32-bit signed integer has a range of [-2^{31}, 2^{31} - 1], or [-2147483648, 2147483647].
#   	If the reversed number exceeds this range, return 0.
# 	4.	Return the Result:
# 	•	Return the reversed integer with the appropriate sign.

import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit integer range limits using sys.maxsize
        INT_MIN = -(2 ** 31)
        INT_MAX = (2 ** 31) - 1

        # Initialize the result and get the sign of x
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before adding the digit to the result
            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result

# ------------------------ Explaination ---------------------------
# Explanation
#
# 	1.	Calculate INT_MIN and INT_MAX:
# 	•	We calculate INT_MIN as -(2^{31}), which gives -2147483648.
# 	•	We calculate INT_MAX as (2^{31}) - 1, which gives 2147483647.
# 	2.	Handling the Reversal:
# 	•	We extract each digit using x % 10 and reduce x using integer division (x //= 10).
# 	•	We then append the digit to result by multiplying result by 10 and adding the digit.
# 	3.	Overflow Check:
# 	•	Before updating result, we check for potential overflow using:
        # if result > (INT_MAX - digit) // 10:
        #     return 0
# 	•	This ensures that the multiplication and addition operations will not exceed the 32-bit boundary.
#
# 	4.	Return the Result:
# 	•	Finally, we multiply result by sign to restore the original sign.

# ------------------------ Complexity --------------------
# 	•	Time Complexity: O(\log_{10}(x)) — The number of digits in x determines the number of iterations, which is approximately \log_{10}(x).
# 	•	Space Complexity: O(1) — The implementation uses a constant amount of space.


# reverse.
# print(solution.lengthOfLongestSubstring("abcabcbb"))  # Output: 3

# Test the function with the value 123
solution = Solution()
print(solution.reverse(123))        # Output: 321
print(solution.reverse(-123))       # Output: -321
print(solution.reverse(120))        # Output: 21
print(solution.reverse(1534236469)) # Output: 0 (correctly handled overflow)
