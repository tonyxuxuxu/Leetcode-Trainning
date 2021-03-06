"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        is_repeat = False

        while curr.next:
            while curr.next.next and curr.next.val == curr.next.next.val:
                is_repeat = True
                curr.next = curr.next.next
            if is_repeat:
                curr.next = curr.next.next
                is_repeat = False
            else:
                curr = curr.next
        return dummy.next