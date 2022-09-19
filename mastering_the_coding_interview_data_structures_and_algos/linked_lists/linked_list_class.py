import math
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head: Optional[ListNode] = None, length: Optional[int] = 0):
        self.head = head
        self.tail = self.head
        self.length = length

    def append(self, tail: ListNode):
        self.tail.next = tail
        self.tail = tail
        self.length += 1
        return self

    def prepend(self, head: ListNode):
        head.next = self.head
        self.head = head
        self.length += 1
        return self

    def insert(self, index: int, list_node: ListNode):
        if index >= self.length - 1:
            return self.append(list_node)

        if index == 0:
            return self.prepend(list_node)

        leader = self.traverse_to_index(index - 1)

        list_node.next = leader.next
        leader.next = list_node
        self.length += 1

        return self

    def remove(self, index: int):
        if index == 0:
            return self.unshift()

        if index >= self.length - 1:
            return self.pop()

        leader = self.traverse_to_index(index - 1)

        new_next = leader.next.next if leader.next is not None else None
        removed_node = leader.next
        leader.next = new_next

        return removed_node

    def unshift(self):
        leader = self.head
        next_node = leader.next
        leader.next = None
        self.head = next_node
        self.length -= 1
        return leader

    def pop(self):
        leader = self.traverse_to_index(self.length - 2)
        popped_node = leader.next
        leader.next = None
        self.length -= 1
        return popped_node

    def traverse_to_index(self, index: int):
        if index > self.length - 1:
            return self.tail

        leader = self.head
        i = 0
        while i is not index:
            leader = leader.next
            i += 1

        return leader

    # 0 -> 1 -> 3 -> 5
    # 5 -> 3 -> 1 -> 0
    def reverse_linked_list(self):
        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first

        return self.head

    def print_list(self):
        leader = self.head
        while leader:
            print(leader.val)
            leader = leader.next


n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(5)
n0 = ListNode()
n4 = ListNode(3)

linked_list = LinkedList(n1, 1)

# print(linked_list)

linked_list.append(n2)

# print(linked_list)

linked_list.append(n3)

# print(linked_list)

linked_list.prepend(n0)

# 0 -> 1 -> 3 -> 5

linked_list.insert(2, n4)


# linked_list.print_list()
#
linked_list.remove(4)

linked_list.print_list()

linked_list.reverse_linked_list()

# linked_list.unshift()

linked_list.print_list()
