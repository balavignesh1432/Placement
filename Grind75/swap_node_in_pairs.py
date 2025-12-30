def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Recursion:
    # At each step, store the third node
    # Reverse the nodes
    # For the new next, call with the third node
    # Return the second node in each call
    # TC: O(N), SC: O(N) for recursion stack
    def helper(curr):
        if not curr or not curr.next:
            return curr
        nex = curr.next
        store = nex.next
        nex.next = curr
        curr.next = helper(store)
        return nex
    return helper(head)

    # Iterative Method Dummy Node
    # Use only one pointer prev
    # With that set first and second
    # Swap the chain, then update prev
    # Do until prev.next or prev.next.next there is one or no node left
    # Initially set prev to dummy node
    # TC: O(N), SC: O(1)
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # swap
        store = second.next
        second.next = first
        first.next = store
        
        # Link previous part to swapped
        prev.next = second
        # Move prev to the end of the swapped pair
        prev = first

    return dummy.next