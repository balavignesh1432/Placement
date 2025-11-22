
class Solution:
    def merge2List(self, left, right):  # For merging any two sorted list
        head = ListNode()
        merged = head
        while left and right:
            if left.val <= right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        if left:
            head.next = left
        if right:
            head.next = right
        return merged.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute: Store all nodes in array
        # Sort, and create list, and return head
        # TC: O(N log N), SC: O(N)
        lst = []
        for l in lists:
            node = l
            while node:
                lst.append(node.val)
                node = node.next
        lst.sort()
        head = ListNode()
        temp = head
        for val in lst:
            temp.next = ListNode(val)
            temp = temp.next
        return head.next
        
        # Merging each list one by one, using just pointers (Merge 2 list at a time)
        # Then merged already merged list and current list
        # There are k lists, loop running k times for getting each list
        # At the worst case, total n nodes, merging takes n
        # So TC: O(N * K), SC: O(1)
        res = None
        if not len(lists):
            return None
        res = lists[0]
        for i in range(1, len(lists)):  # K times
            left = res
            right = lists[i]
            res = self.merge2List(left, right)      # Runs worst N
        return res

        # Since merging can be done in any order, and need not be sequential
        # We take adjacent 2 list and merge, and then next 2 and so on 
        # So height will be log k, and each case time will be N
        # So: TC : O(N * log K), SC: O(K), since only k roots are stored
        if not len(lists):
            return None
        while len(lists) > 1:   # Until single merged List
            mergedList = []     # Create new list and add to it after merging
            for i in range(0, len(lists), 2):   # Runs for k/2, then k/4, so totally log K
                if i < len(lists) - 1:
                    mergedList.append(self.merge2List(lists[i], lists[i+1]))  # Needs N for total
                else:   # If odd length, just add the last list to merged
                    mergedList.append(lists[i]) 
            lists = mergedList  # Make lists as new list, no need to copy as new list is created in loop
        return lists[0]