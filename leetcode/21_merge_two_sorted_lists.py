# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        merge the ListNode by compare each node val

        :param l1:
        :param l2:
        :return:
        '''
        dummy: ListNode = ListNode(0)
        # dummy.next = l1 if l1.val < l2.val else l2
        temp = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
        if l1 != None:
            temp.next = l1
        elif l2 != None:
            temp.next = l2
        return dummy.next

    def mergeTwoListsRecursion(self, l1: ListNode, l2:ListNode) -> ListNode:
        '''
        merge the ListNode by recursion

        :param l1:
        :param l2:
        :return:
        '''
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoListsRecursion(l1.next, l2)
        return l1 or l2


solution = Solution()
l1: ListNode = ListNode(0)
temp1: ListNode = l1
for i in [1, 2, 4]:
    temp1.next = ListNode(i)
    temp1 = temp1.next

l2: ListNode = ListNode(0)
temp2: ListNode = l2
for i in [1, 2, 4]:
    temp2.next = ListNode(i)
    temp2 = temp2.next

print(solution.mergeTwoLists(l1, l2))