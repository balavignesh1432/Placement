def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # To do it in place, reverse k length, need its head and tail to connect to existing chain structure
    # Reverse a LL, But also returns Tail
    # TC: O(N), SC: O(1)
    def reverse(node):
        tail = node
        prev = None
        while node:
            store, node.next = node.next, prev
            prev, node = node, store
        return [prev, tail]
    
    # Dummy head node
    dummy = ListNode()
    prev = dummy
    prev.next = head
    
    # Until prev is last node
    while prev.next:
        # Take next of prev
        node = prev.next
        for _ in range(k - 1):      # Get kth node
            node = node.next
            if not node:            # If exhausted before k, return as already done
                return dummy.next
        store, node.next = node.next, None  # Store next of k to connect reversed tail
        head, tail = reverse(prev.next)     # Reverse with prev next which points to start
        prev.next = head                    # Update links 
        tail.next = store
        prev = tail                         # Update prev for next chain
    return dummy.next