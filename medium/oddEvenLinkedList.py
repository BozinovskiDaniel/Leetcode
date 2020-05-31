# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Error checking
        if head is None:
            return None
        elif head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even  # Keep a pointer to evenhead

        while even is not None and even.next is not None:

            # Move odd
            odd.next = even.next
            odd = odd.next

            # Move even
            even.next = odd.next
            even = even.next

        # Join two lists
        odd.next = evenHead

        return head
