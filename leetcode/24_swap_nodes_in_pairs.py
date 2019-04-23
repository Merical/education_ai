# Definition for singly-linked list.
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy: ListNode = ListNode(0)
        output: ListNode = dummy

        while head:
            if not head.next:
                dummy.next = head
                break
            else:
                rest = head.next.next
                head.next.next = None

                temp = head.next
                head.next = None
                temp.next = head
                head = temp
                head.next.next = rest
                dummy.next = head
                head = head.next.next
                dummy = dummy.next.next

        return output.next

    def printListNode(self, node: ListNode):
        count = 0
        while node and count < 10:
            sys.stdout.write(str(node.val))
            node = node.next
            count += 1
        sys.stdout.write('\n')


solution = Solution()
l1: ListNode = ListNode(0)
temp1: ListNode = l1
for i in [1,2,3,4,5]:
    temp1.next = ListNode(i)
    temp1 = temp1.next

output = solution.swapPairs(l1.next)
while output:
    print(output.val)
    output = output.next