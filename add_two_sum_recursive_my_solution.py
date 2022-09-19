# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ns1 = self.appendToNumStrRecursive('', l1)
        ns2 = self.appendToNumStrRecursive('', l2)

        final_num = int(ns1) + int(ns2)
        final_num_str = str(final_num)

        list_node = None

        for i in range(0, len(final_num_str)):
            ln = ListNode(int(final_num_str[i]), list_node)
            list_node = ln

        return list_node

    def appendToNumStrRecursive(self, string: str, l_node: Optional[ListNode]) -> str:
        s = string
        if l_node.next is not None:
            s = self.appendToNumStrRecursive(s, l_node.next)
        return s + f"{l_node.val}"
