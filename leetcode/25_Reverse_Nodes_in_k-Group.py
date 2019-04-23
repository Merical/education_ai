# Definition for singly-linked list.
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy: ListNode = ListNode(0)
        output: ListNode = dummy

        while head:
            if not head:
                dummy.next = head
                break
            else:
                nodeList = []
                for i in range(k):
                    if head:
                        temp = head
                        head = head.next
                        temp.next = None
                        nodeList.append(temp)
                    else:
                        break

                if len(nodeList) == k:
                    for i in range(len(nodeList)):
                        dummy.next = nodeList.pop()
                        dummy = dummy.next
                else:
                    for node in nodeList:
                        dummy.next = node
                        dummy = dummy.next

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
for i in [1, 2, 3, 4, 5]:
    temp1.next = ListNode(i)
    temp1 = temp1.next

output = solution.reverseKGroup(l1.next, k=3)
while output:
    print(output.val)
    output = output.next