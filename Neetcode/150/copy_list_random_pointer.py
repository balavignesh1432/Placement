def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # Clone each node and return, finally return head
    # So better use recursion, use map to maintain mapping of original to clone
    # List can contain duplicate values, so key should be entire node itself, not just the number
    # For every stage, check if already cloned, if so return that node. (Avoid cloning same node again)
    # Because random could point to any node previously also.
    # Also random could point to itself.
    # So clone the node, and assign to mapping before constructing next and random
    # Since value can be modified after assigning also
    # Finally return the cloned node
    # Base Case: If node becomes None, return None
    # TC: O(N), SC: O(N), N for Map and Call Stack
    clone = {}
    def helper(node):
        if not node:
            return None
        if node in clone:
            return clone[node]
        copy = Node(node.val)
        clone[node] = copy
        copy.next = helper(node.next)
        copy.random = helper(node.random)
        return clone[node]
    return helper(head)