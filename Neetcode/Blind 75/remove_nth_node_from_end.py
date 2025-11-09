def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Two pointers: TC - O(N), SC = O(1)
    # Moving only the fast n times, 1 step
    # Then moving both slow and fast until fast ends
    # Then removing slow, until fast reaches end
    # Slow is the node that has to be removed
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    prev = ListNode()
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    if slow == head:
        return slow.next
    prev.next = slow.next
    return head
    
    # Recursion - TC O(N), SC = O(1)
    # Just recurse until end, come back while decrementing n as counter
    # If node has to be removed, return next of it, otherwise return itself
    def helper(node):
        if not node:    # If end, return None, which will be assigned to next of last node
            return None
        node.next = helper(node.next)   # Assign next of node after removal 
        nonlocal n  # Needed if modifying outside scope non mutable variables or declare [n] as list is mutabl
        n -= 1  # After reaching end, keep decrementing
        if n == 0:  # Return next of this node to parent, which should be assigned as its parents next
            return node.next
        return node # For other nodes, return itself to its parent
    return helper(head) # Return the modified linked list head

    # Brute Force: Find index of node to be removed by finding length
    # Then iterate to remove that node
    # TC: O(N), SC: O(1)
    N = 0
    cur = head
    while cur:
        N += 1
        cur = cur.next
    removeIndex = N - n
    if removeIndex == 0:
        return head.next
    cur = head
    for i in range(N - 1):
        if (i + 1) == removeIndex:
            cur.next = cur.next.next
            break
        cur = cur.next
    return head