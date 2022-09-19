from typing import Optional


class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:

    def __init__(self, head: Optional[ListNode] = None, length: Optional[int] = 0):
        self.head = head
        self.tail = self.head
        self.length = length

    def append(self, tail: ListNode):
        tail.prev = tail
        self.tail.next = tail
        self.tail = tail
        self.length += 1
        return self

    def prepend(self, head: ListNode):
        self.head.prev = head
        head.next = self.head
        self.head = head
        self.length += 1
        return self

    def insert(self, index: int, list_node: ListNode):
        if index > self.length - 1:
            return self.append(list_node)

        leader = self.traverse_to_index(index - 1)
        follower = leader.next
        list_node.prev = leader
        list_node.next = follower
        follower.prev = list_node
        leader.next = list_node
        self.length += 1

        return self

    def remove(self, index: int):
        if index < 0:
            return self

        leader = self.traverse_to_index(index - 1)

        new_next = leader.next.next
        leader.next = new_next

        return self

    def traverse_to_index(self, index: int):
        if index > self.length - 1:
            return self.tail

        leader = self.head
        i = 0
        while i is not index:
            leader = leader.next
            i += 1

        return leader

    def print_list(self):
        leader = self.head
        while leader:
            print(leader.val)
            leader = leader.next
