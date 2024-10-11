
#To determine if a singly linked list is a palindrome, we can use a two-pointer technique (slow and fast pointers) to find the middle of the list, reverse the second half of the list, and then compare the two halves. Here’s how we can implement this approach:

# Approach:
#
# 	1.	Find the Middle of the Linked List:
# 	•	Use the slow and fast pointers to reach the middle of the linked list.
#   	The fast pointer moves two steps at a time, while the slow pointer moves one step.
#      	When the fast pointer reaches the end, the slow pointer will be at the middle.
# 	2.	Reverse the Second Half:
# 	•	Reverse the second half of the linked list starting from the slow pointer.
# 	3.	Compare the Two Halves:
# 	•	Compare the nodes from the start of the list with the nodes from the reversed second half.
#   	If all values match, the list is a palindrome; otherwise, it is not.
# 	4.	Restore the List (Optional):
# 	•	Optionally, reverse the second half back to its original state if you need to maintain the original structure of the list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        second_half = self.reverseList(slow)

        # Step 3: Compare the first and the second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
# Explanation:
#
# 	1.	isPalindrome Method:
# 	•	The method first checks if the list is either empty or has only one node, returning True if so.
# 	•	It uses the slow and fast pointer technique to find the middle of the linked list.
# 	•	The second half of the linked list, starting from the middle, is reversed using the helper method reverseList.
# 	•	It compares nodes from the first half and the reversed second half. If all values match, the list is a palindrome; otherwise, it returns False.
# 	2.	reverseList Method:
# 	•	This helper method reverses a linked list starting from a given node (head). It returns the new head of the reversed list.


# Complexity:
#
# 	•	Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list multiple times (to find the middle, reverse the second half, and compare the halves).
# 	•	Space Complexity: O(1), as it uses a constant amount of additional space (a few pointers).

# Creating the linked list [1, 2, 2, 1]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
print(solution.isPalindrome(node1))  # Output: True

# Creating the linked list [1, 2]
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

print(solution.isPalindrome(node1))  # Output: False
