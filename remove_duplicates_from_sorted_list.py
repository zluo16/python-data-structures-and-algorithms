from typing import Optional

from mastering_the_coding_interview_data_structures_and_algos.linked_lists.linked_list_class import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            if prev:
                if prev.val == curr.val:
                    prev.next = curr.next
                else:
                    prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return head
