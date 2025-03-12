# https://leetcode.com/problems/add-two-numbers/description/ 

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# example:
# Input: l1 = [2,4,3] represents 342, l2 = [5,6,4] represents 465   
# Output: [7,0,8] represents 807

# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.  

# Definition for singly-linked list.
# Definition of a singly linked list node
class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x  # The value stored in this node
        self.next = None  # Reference to the next node, initially None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to serve as the head of the result list
        dummy = ListNode(0) # creates new instance of ListNode with its value (val) set to 0
        curr = dummy  # Current pointer to build the result list
        carry = 0  # Tracks the carry over when sum >= 10
        
        # Continue while there are digits left in either list or there's a carry
        while l1 or l2 or carry:
            # Get values from the lists, use 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Integer division to get carry (0 or 1)
            digit = total % 10  # Get the ones digit for current position
            
            # Create new node with calculated digit and link it
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result list, excluding the dummy head
        return dummy.next

# test
if __name__ == "__main__": # if the file is run directly, not imported
    # Create linked list l1: 2 -> 4 -> 3
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # Create linked list l2: 5 -> 6 -> 4    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Create solution instance
    solution = Solution()   
    result = solution.addTwoNumbers(l1, l2)
    
    # Print the result
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

