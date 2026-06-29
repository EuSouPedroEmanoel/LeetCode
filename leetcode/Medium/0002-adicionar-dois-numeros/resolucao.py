from typing import Optional

# Se for testar no Leetcode, por favor comente toda a classe ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def from_list(elements: list[int]) -> Optional[ListNode]:
        if not elements:
            return None

        head = ListNode(elements[0])
        current = head

        for i in elements[1:]:
            current.next = ListNode(i)
            current = current.next

        return head

    @staticmethod
    def to_list(head: Optional['ListNode']) -> list:
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result


    def addTwoNumbers(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        l1_size = len(Solution.to_list(l1))
        l2_size = len(Solution.to_list(l2))

        size = l1_size if l1_size > l2_size else l2_size
        result_list: list[int] = []
        temp = 0

        current_l1 = l1
        current_l2 = l2

        for i in range(size):

            l1_temp = 0
            l2_temp = 0

            if temp > 0:
                l1_temp += temp
                temp = 0
            if current_l1:
                if current_l1.val is not None:
                    l1_temp += current_l1.val

            if current_l2:
                if current_l2.val is not None:
                    l2_temp += current_l2.val

            sttm = l1_temp + l2_temp

            if sttm >= 10:
                sttm = sttm -10
                temp += 1

            result_list.append(sttm)
            if current_l1:
                current_l1 = current_l1.next
            if current_l2:
                current_l2 = current_l2.next
        if temp != 0:
            result_list.append(1)
        return Solution.from_list(result_list)


