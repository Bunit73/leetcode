# https://leetcode.com/submissions/detail/109225225/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        
        stack = []
        
        while(head):
            stack.append(head)
            head = head.next
        
        #New head
        head = stack.pop()
        head.next = None
        final_head = head
        
        while len(stack)>0:
            head.next = stack.pop()
            head = head.next
            head.next = None
            
        return final_head
