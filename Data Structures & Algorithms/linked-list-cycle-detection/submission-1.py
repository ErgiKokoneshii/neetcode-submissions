# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = []
        while head:
            if head not in visited_nodes:
                visited_nodes.append(head)
            else:
                return True
            head = head.next
        return False