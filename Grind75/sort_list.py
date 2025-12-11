def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Merge Sort Recursion:
    # Divide into half
    # Call for left and right
    # Merge them and return head
    # When dividing, use dummy node, as start, and slow and fast pointers
    # Until fast.next is none, move
    # slow.next is the middle, which should be the head of list2
    # Make slow.next none to mark end of list1
    # Merge same as merging two sorted list using dummy node
    # TC: O(N log N), SC: O(log N)
    def divide(root):
        dummy = ListNode()
        dummy.next = root
        head1 = root
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return [head1, head2]
        
    def merge(head1, head2):
        dummy = ListNode()
        head = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2
        return dummy.next    
        
    def helper(root):
        if not root:
            return None
        if not root.next:
            return root
        head1, head2 = divide(root)
        left = helper(head1)
        right = helper(head2)
        return merge(left, right)
    return helper(head)


    # Space Optimization: Avoid Recursion Call Stack
    # Use iteration with Bottom UP merge, and size which multiplies by 2 each time
    # loop runs for log N times, inside sort runs for N
    # First merge one length lists
    # Then two length lists
    # Until size becomes length, count length in the beginning
    # While merging two lists, after merge return head and tail,
    # So as to start for the next iteration, as after merge this head has to be next of the previous
    # Initually prev will dummy Node
    # Split is based on head and size
    # TC: O(N log N), SC: O(1)
    if not head or not head.next:
        return head

    length = 0
    curr = head
    while curr:             # Count length of list
        length += 1     
        curr = curr.next
    dummy = ListNode(0)
    dummy.next = head

    size = 1
    while size < length:
        prev = dummy
        curr = dummy.next
        while curr:
            left = curr
            right = split(left, size)   # cuts after size nodes, returns next start

            curr = split(right, size)   # 3. Next starting position after right list

            merged_head, merged_tail = merge(left, right)   # 4. Merge left + right and attach
            prev.next = merged_head
            prev = merged_tail
        size *= 2
    return dummy.next

    # Splits list into two parts:
    # Returns the head of the second part after skipping 'size' nodes
    def split(head, size):
        if not head:
            return None
        for _ in range(size - 1):
            if not head.next:
                return None
            head = head.next
        second = head.next
        head.next = None
        return second

    # Merge two sorted lists, but also return the tail
    def merge(l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2

        # Advance tail to the end
        while tail.next:
            tail = tail.next
        return dummy.next, tail