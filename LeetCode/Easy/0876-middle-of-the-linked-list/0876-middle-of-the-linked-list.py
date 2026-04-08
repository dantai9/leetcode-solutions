# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenght = 0
        current = head
        while current:
            lenght += 1
            current = current.next
        current = head
        for i in range (lenght // 2):
            current = current.next
        return current
        