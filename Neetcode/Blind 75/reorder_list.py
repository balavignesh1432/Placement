def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute Force: Add list nodes to list, reorder list (Another list)
        # Then make linked list connections according to reorder list
        # TC: O(N), SC: O(N)
        array = []
        while head: # Add nodes to list
            array.append(head)
            head = head.next
        reorderArray = []
        # Reorder pointers from ends
        i = 0   
        j = len(array) - 1
        while i <= j:   # Reorder list
            reorderArray.append(array[i])
            if i != j:  # To avoid adding same twice
                reorderArray.append(array[j])
            i += 1
            j -= 1
        for i in range(len(reorderArray) - 1):
            reorderArray[i].next = reorderArray[i + 1]  # Make LL links according to modified order
        reorderArray[-1].next = None    # Make last element point to None
        return head 

        
        # Intuition: Merging 1st half and reversed 2nd half results in reordered list
        # Since reversing can be done in place, and does not need recursion for extra space
        # Find mid point, using fast and slow pointers
        # Mark end of first half, and reverse second half
        # Since odd length, results in one larger than other, handle that case when merging
        # This method can be used when needed to iterate back in linked list.
        # Since only one half of LL needs to be reversed, 
        # no extra space is needed for solving, first half remains intact
        # TC: O(N), SC: O(1)
        if not head.next:
            return head
        slow = fast = head
        prev = None
        while fast and fast.next:   # Find Mid point using fast and slow pointers
            prev = slow             # To make the last node of 1st half to point to None
            slow = slow.next
            fast = fast.next.next
        prev.next = None            # Mark end of first half
        prev = None                 # For reversing 2nd half
        
        # Reversing 2nd half
        while slow:                 # Slow points the start of 2nd half
            store = slow.next
            slow.next = prev
            prev = slow
            slow = store
        list2 = prev                # Prev points to the last node of 2nd half which is new head
        list1 = head                # Head is needed to return
        
        # Merge 1st half and reversed 2nd half
        while list1:    # 1st half is short when odd length
            store1 = list1.next
            store2 = list2.next
            list1.next = list2
            list1 = store1
            if list1 != None:       # If first half is over, don't modify 2nd half, leave the rest of chain
                list2.next = list1
                list2 = store2
        return head