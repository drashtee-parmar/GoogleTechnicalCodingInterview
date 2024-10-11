def addBinary(a, b):
    i = len(a) - 1
    j = len(b) - 1


    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0

        total = x + y + carry
        result.append(str(total % 2))
        carry = total // 2

        i -= 1
        j -= 1

    return ''.join(result[::-1])

# Explanation:
#
# 	1.	Iterate from the End:
# 	•	We iterate from the end of each string (i and j pointers). If one pointer goes out of bounds, the value defaults to 0.
# 	2.	Calculate the Sum and Update Carry:
# 	•	Calculate total as the sum of the digits (x and y) and the carry.
# 	•	total % 2 gives the binary digit to append to the result.
# 	•	total // 2 updates the carry for the next iteration.
# 	3.	Build the Result:
# 	•	We append each calculated binary digit to the result list and reverse it at the end to construct the binary string in the correct order.
#
# Complexity:
#
# 	•	Time Complexity: O(n), where n is the maximum length of the two input strings.
# 	•	Space Complexity: O(n), for storing the result.

print(addBinary("11", "1"))   # Output: "11"
print(addBinary("1010", "1011")) # Output: "1101"
