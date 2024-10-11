class Solution:
    def romanToInt(self, s: str) -> int:
        # Map of Roman numerals to their integer values
        # 	1.	Mapping Roman Numerals:
        # 	•	We create a dictionary (roman_values) that maps each Roman numeral character to its corresponding integer value.
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate through the string in reverse order
        # 	2.	Iterate Through the String in Reverse:
        # 	•	We iterate through the string from right to left to easily handle subtraction cases.
        # 	•	We initialize total to accumulate the sum and prev_value to keep track of the previous numeral’s value.
        for char in reversed(s):
            value = roman_values[char]
            # If the current value is less than the previous value, subtract it; otherwise, add it
        # 	3.	Determine When to Add or Subtract:
        # 	•	For each character:
        # 	•	Get its integer value from the dictionary (value = roman_values[char]).
        # 	•	If the current value (value) is less than the previous value (prev_value), it indicates a subtraction case (e.g., IV or IX), so we subtract it from total.
        # 	•	Otherwise, we add it to total.
        # 	•	Update prev_value to the current value for the next iteration.
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        # 	4.	Return the Total:
        # 	•	After iterating through all characters, total will hold the integer value equivalent of the Roman numeral.
        return total

# Testing
solution = Solution()

# Example 1
print(solution.romanToInt("III"))    # Output: 3

# Example 2
print(solution.romanToInt("IV"))     # Output: 4

# Example 3
print(solution.romanToInt("IX"))     # Output: 9

# Example 4
print(solution.romanToInt("LVIII"))  # Output: 58

# Example 5
print(solution.romanToInt("MCMXCIV")) # Output: 1994

# Complexity
#
# 	Time Complexity: O(n), where n is the length of the Roman numeral string. We iterate through each character once.
# 	Space Complexity: O(1), since we only use a fixed amount of space for variables regardless of the input size.
