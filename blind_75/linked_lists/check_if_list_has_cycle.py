from typing import Optional

from mastering_the_coding_interview_data_structures_and_algos.linked_lists.linked_list_class import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        node_set = set()

        curr = head

        while curr is not None:
            if curr in node_set:
                return True

            node_set.add(curr)
            curr = curr.next

        return False


a1 = [-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]
a1.sort()
print(a1)
