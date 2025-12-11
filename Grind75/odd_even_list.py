def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Create two chains parallely, one is odd and another is even
    # Finally at the end, conenct odd chain to even chain
    # Use two pointers intiallised to head and next
    # Store next to join at the end
    # Then update connection for bothe pointers
    # Now move both pointers to their next
    # At each iteration, there will be a conenction from first to second initially
    # Do until fast2.next is None, there is no movement possible for fast 2
    # Now finally make the stored as next of fast1
    # Always fast2 will only exhaust first (Odd length)
    # Base case, if head empty return None
    # TC: O(N), SC: O(1)

    if not head:
        return None
    fast1 = head
    fast2 = head2 = head.next
    while fast2 and fast2.next:
        fast1.next = fast2.next
        fast2.next = fast2.next.next
        fast1 = fast1.next
        fast2 = fast2.next
    fast1.next = head2
    return head
