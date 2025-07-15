# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        numbers = []
        current = head
        while current is not None:
            numbers.append(current.val)
            current = current.next
        exp = len(numbers) - 1
        total = 0
        for binary in numbers:
            total += (2**exp) * binary
            exp -= 1
        return total
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
