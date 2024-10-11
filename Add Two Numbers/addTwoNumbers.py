
#To solve this problem, we’ll traverse the linked lists, add corresponding digits along with any carry, and build a new linked list for the result. Since the digits are stored in reverse order, we can directly add them starting from the head of the lists.

# Approach:
#
# 	1.	Initialize a dummy node to start the result linked list and a current pointer to build the list.
# 	2.	Initialize a carry variable to store any carry-over during addition.
# 	3.	Traverse both linked lists simultaneously:
# 	•	Add the values from both lists and the carry.
# 	•	Compute the new digit (sum % 10) and update the carry (sum // 10).
# 	•	Move the current pointer to the new node containing the computed digit.
# 	•	Move the pointers of l1 and l2 to the next node if they exist.
# 	4.	After the loop, if there’s a remaining carry, add it as a new node.
# 	5.	Return the result starting from the node next to the dummy node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # Dummy node to form the base of the resulting linked list
        result = []
        carry = 0
        i, j = 0, 0

        # Iterate through both lists until all values and carry are processed
        while i < len(l1) or j < len(l2) or carry:
            # Get the value from l1 if available
            if i < len(l1):
                val1 = l1[i]
            else:
                val1 = 0

            # Get the value from l2 if available
            if j < len(l2):
                val2 = l2[j]
            else:
                val2 = 0

            # Calculate the sum and update the carry
            total = val1 + val2 + carry
            carry = total // 10

            # Append the current digit to the result list
            result.append(total % 10)

            # Move to the next index in l1 and l2 if possible
            i += 1
            j += 1

        return result

#     Explanation:

	# 1.	Get Values from Lists:
	# •	The if statements are split into two separate parts for getting val1 from l1 and val2 from l2.
	# •	If the current index i is within the bounds of l1, val1 is set to l1[i]. Otherwise, val1 is set to 0.
	# •	Similarly, if j is within the bounds of l2, val2 is set to l2[j]. Otherwise, val2 is set to 0.
	# 2.	Update total and carry:
	# •	We compute the total as val1 + val2 + carry.
	# •	The carry for the next iteration is updated as total // 10.
	# •	We append the digit (total % 10) to the result list.
	# 3.	Advance Indices:
	# •	The indices i and j are incremented to move to the next element in each list.

# Complexity:
#
# 	•	Time Complexity: O(n), where n is the maximum length of the two lists. We iterate through each list once.
# 	•	Space Complexity: O(n), for storing the resulting list.

solution = Solution()

# Example 1
l1 = [2, 4, 3]
l2 = [5, 6, 4]
result = solution.addTwoNumbers(l1, l2)
print(result)  # Output: [7, 0, 8]

# Example 2
l1 = [0]
l2 = [0]
result = solution.addTwoNumbers(l1, l2)
print(result)  # Output: [0]

# Example 3
l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
result = solution.addTwoNumbers(l1, l2)
print(result)  # Output: [8, 9, 9, 9, 0, 0, 0, 1]
