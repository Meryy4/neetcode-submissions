# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        tail=dummy
        first_list=list1
        second_list=list2
        while(first_list is not None and second_list is not None):
            if first_list.val<second_list.val:
                tail.next=first_list
                first_list=first_list.next
            else:
                tail.next=second_list
                second_list=second_list.next
            tail=tail.next
        if first_list is not None:
            tail.next = first_list
        else:
            tail.next = second_list
        return dummy.next

            
           
            






        