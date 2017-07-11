# https://leetcode.com/problems/remove-duplicates-from-sorted-list/#/description
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        
        num_hash = {}
        new_ll = []
        
        while head:
            if head.val not in num_hash:
                new_ll.append(head)
                num_hash[head.val] = True
            head = head.next
        
        new_head = new_ll.pop(0)
        new_head.next = None
        head_ptr = new_head
        
        while len(new_ll) > 0:
            new_head.next = new_ll.pop(0)
            new_head = new_head.next
            new_head.next = None
            
        
        return head_ptr
