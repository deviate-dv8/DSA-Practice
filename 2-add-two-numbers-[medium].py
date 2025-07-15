# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        l1List = []
        l2List = []
        current = l1
        while current is not None:
            l1List.insert(0, current.val)
            current = current.next
        current = l2
        while current is not None:
            l2List.insert(0, current.val)
            current = current.next
        sumNode = int("".join(map(str, l1List))) + int("".join(map(str, l2List)))
        sumList = reversed(list(map(int, str(sumNode))))
        current = dummy
        for i in sumList:
            current.next = ListNode(i)
            current = current.next

        return dummy.next

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
