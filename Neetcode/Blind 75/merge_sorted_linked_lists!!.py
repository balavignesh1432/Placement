def mergeTwoLists(list1, list2):
    # Start by creating a dummy node
    head = temp = ListNode()
    # Iterate until any one list is exhausted
    while list1 and list2: 
        if list1.val <= list2.val:
            temp.next = list1   # Update the temp chain 
            list1 = list1.next  # Update the list pointer
        else:
            temp.next = list2   # Update the temp chain 
            list2 = list2.next  # Update the list pointer
        temp = temp.next    # Update the temp node to its chain
    temp.next = list1 if list1 else list2   # Update temp chain if one is exhausted early
    return head.next    # Return next of initial dummy created

    # TC - O(M + N), SC - O(1)


    # Recursion - Intuition Just think two single length list:
    # At each step there are two pointers
    # Just have to decide which pointer to move next
    # each pointer next move is another recursion call
    # And have to decide where should next point while moving,
    # which will be returned from the recursion call
    # Base Case: If one list pointer comes to end, Both can not come to end at a time
    # Return the pointer of the other list. (Even if other is also empty due to input edge)
    # Small subproblem: When just two single nodes, you compare and move one, 
    # For its next the other will be returned (Base Case)
    # So now length two merged list is returned with head, 
    # which will be the next of previous call
    
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
    
    # TC - O(M + N), SC - O(M + N)