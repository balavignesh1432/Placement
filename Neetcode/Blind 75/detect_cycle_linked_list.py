def hasCycle(self, head):
    # Brute Force
    # Using set to mark already visited node
    # TC - O(N), SC = O(N)
    visited = set()
    while head:
        if head not in visited:
            visited.add(head)
        else:
            return True
        head = head.next
    return False

    # Tortoise and Hare Cycle Detection
    # TC = O(N), SC = O(1)
    fast = slow = head
    while slow and fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
        if slow == fast:   
            return True
    return False


    # Recursive Version
    # TC - O(N), SC = O(N) [Call Stack]
    def helper(slow, fast):
        if not slow or not fast:
            return False
        if slow == fast:
            return True
        if fast.next:
            return helper(slow.next, fast.next.next)
        return False
    if head and head.next:
        return helper(head.next, head.next.next)
    return False