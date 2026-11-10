# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, list1: ListNode | None, list2: ListNode | None)-> ListNode | None:
        result = ListNode()
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            result  = list1
            result.next = self.solve(list1.next, list2)
        else:
            result = list2
            result.next = self.solve(list1, list2.next)

        return result
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        return self.solve(list1, list2)
        


        