def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Use two adjacent pointers curr and prev
    # prev initially None as end has to be None
    prev = None
    curr = head
    while curr != None:
        # As current next is going to be set as prev, 
        # store it for next iteration
        store = curr.next  
        curr.next = prev    # Reverse
        # Update prev and curr for next iteration
        prev = curr 
        curr = store
    # Curr becomes None, so prev points to last element
    return prev

    # TC - O(N), SC - O(1)

    # Recursive Version
    def helper(prev, curr):
        if curr == None:
            return prev
        store = curr.next
        curr.next = prev
        return helper(curr, store)
    return helper(None, head)

    # TC - O(N), SC - O(N) [Call Stack ]