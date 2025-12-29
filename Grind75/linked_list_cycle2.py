def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Brute Force: Using Set to find if visited
    # If visited already, then that is the start of the cycle
    # If end reached, then no cycle
    # TC: O(N), SC: O(N)
    visited = set()    
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next
    return None

    # Two pointers:
    # Get the point where it meets
    # Let A be dist from head to start of chain, B be dist from start to meet
    # Let C be dist from meet to start of chain
    # The slow pointer travelled, A + B,
    # Fast pointer travelled, A + B + C + B
    # But dist of fast should be doublt of slow,
    # A + B + C + B = 2 (A + B)
    # A = C
    # So moving head and meet 1 at a time until they meet is the start point
    # TC: O(N), SC: O(1)
    slow = fast = head 
    meet = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            meet = fast
            break
    while meet and meet != head:
        meet = meet.next
        head = head.next
    return meet