# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Create a dummy node to easily return the head of the merged list
        dummy = ListNode()
        tail = dummy
        
        # Traverse both lists while they have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move the tail pointer forward
            tail = tail.next
            
        # At least one of the lists is empty now, append the remaining nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # The merged list starts at dummy.next
        return dummy.next