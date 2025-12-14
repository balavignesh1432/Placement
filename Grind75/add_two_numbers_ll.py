def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Add digit1 and digit2 and carry, and get the digit and carry
    # Initially create a dummy node
    # Create Node with digit, and link to prev, increment all 3 pointers
    # Do until both pointers are not None,
    # If only one exhausts before, for remaining do the same as above adding carry and only the val
    # Edge Case: If at the end only carry exists, create a node and link it
    # Return dummy next as it is the head
    # TC: O(max(m,n)), SC: O(max(m,n))
    carry = 0
    dummy = ListNode()
    temp = dummy
    while l1 and l2:
        val = l1.val + l2.val + carry
        digit = val % 10
        carry = val // 10
        temp.next = ListNode(digit)
        l1 = l1.next
        l2 = l2.next
        temp = temp.next
    
    while l1:
        val = l1.val + carry
        digit = val % 10
        carry = val // 10
        temp.next = ListNode(digit)
        l1 = l1.next
        temp = temp.next
    
    while l2:
        val = l2.val + carry
        digit = val % 10
        carry = val // 10
        temp.next = ListNode(digit)
        l2 = l2.next
        temp = temp.next
        
    if carry:
        temp.next = ListNode(carry) 
    return dummy.next

    # Cleaner Code:
    # TC: O(max(m,n)), SC: O(max(m,n))
    carry = 0
    dummy = ListNode()
    temp = dummy
    while l1 or l2 or carry:
        digit1 = 0 if not l1 else l1.val 
        digit2 = 0 if not l2 else l2.val 
        val = digit1 + digit2 + carry
        digit = val % 10
        carry = val // 10
        temp.next = ListNode(digit)
        temp = temp.next
        l1 = None if not l1 else l1.next
        l2 = None if not l2 else l2.next
    return dummy.next