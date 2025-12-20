def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # Use array and check if reverse are equal
    # TC: O(N), SC: O(N)
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res == res[::-1]
        
    # Reverse Half Method
    # Use fast and slow to find mid point
    # Reverse second half
    # Check both half equality using two pointers, only until both are not None
    # If one reached end, return True (As only one element will be left if odd length)
    # TC: O(N), SC: O(1)
    if not head.next:
        return True
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    prev = None
    while slow:
        store = slow.next
        slow.next = prev
        prev = slow
        slow = store
    while prev and head:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True