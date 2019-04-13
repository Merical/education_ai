class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        2 pass solution

        :param head:
        :param n:
        :return:
        '''
        dummy: ListNode = ListNode(0)
        length: int = 0
        dummy.next = head
        first: ListNode = head
        while first != None:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    def removeNthFromEndOnePass(self, head: ListNode, n: int) -> ListNode:
        '''
        1 pass solution

        :param head:
        :param n:
        :return:
        '''
        dummy: ListNode = ListNode(0)
        dummy.next = head
        first: ListNode = dummy
        second: ListNode = dummy
        i = 0
        while i < n:
            first = first.next
            i += 1
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next



solution = Solution()
head: ListNode = ListNode(0)
temp: ListNode = head
for i in [1]:
    temp.next = ListNode(i)
    temp = temp.next
print(solution.removeNthFromEnd(head.next, 2))
print(solution.removeNthFromEndOnePass(head.next, 2))
