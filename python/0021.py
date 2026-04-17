# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0, None)
        returnHead = dum
        while dum:
            if list1 and list2:
                if list1.val <= list2.val:
                    dum.next = list1
                    list1 = list1.next
                    dum = dum.next
                else:
                    dum.next = list2
                    list2 = list2.next
                    dum = dum.next
            elif list1:
                dum.next = list1
                return returnHead.next
            elif list2:
                dum.next = list2
                return returnHead.next
            else:
                return None

        
