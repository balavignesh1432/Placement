from collections import deque
class Codec:

    # Perform DFS: Do Preorder
    # If node is not none, create as str and add to list, then call left and right
    # If None, then add "None" to list, and return
    # Join as string using delimiter ','
    # TC: O(N), SC: O(N)
    def serialize(self, root):
        if not root:
            return ""
        res = []
        def dfs(node):
            if not node:
                res.append("None")
                return
            if node:
                res.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ",".join(res)

    # Get the string, and deparse it using ',' delimiter
    # Use Global variable index to keep track of position for left and right for each node, initially 0
    # Then perform dfs, using index, Check if index has valid node, if so create node as int, 
    # Then increment global index, and call dfs for that index for node's left
    # Then that left will keep creating for itself moving global index for its creation
    # Then after coming back from left, increment global index and call dfs for that index for node'right
    # IMP: This is because for nodes right position, it is after all the nodes needed for nodes left
    # So use global variable as simply local variable will not work
    # Base Case when reached end of index or not a valid Node, return None
    # TC: O(N), SC: O(N)
    def deserialize(self, data):
        if len(data) == 0:
            return None
        serial = data.split(',')
        index = 0
        def dfs(i):
            if i >= len(serial) or serial[i] == "None":
                return None
            if serial[i] != None:
                node = TreeNode(int(serial[i]))
                nonlocal index
                index += 1
                node.left = dfs(index)
                index += 1
                node.right = dfs(index)
            return node
        root = dfs(0)
        return root




    # Perform BFS
    # Serialization:
    # Add root node to q,
    # Then until q is empty, popleft,
    # Then if not None, then add left and right to q
    # Finally merge using some delimiter as ','
    # Deserialization:
    # Deparse using delimiter
    # Create root node
    # Add root node to queue, queue will always contain created non None nodes
    # Use index, to set each node's left and right, intially set it to 1 (Pointing to left of root node position)
    # Pop the node, check if left is valid node (Left is available at index), if so create node, make it left, add to queue
    # Then increase index 
    # and check if that index position is valid, if so create node and make it right, and add to queue
    # Then again increase index, IMP: This is to ensure, for next iteration, index points to the correct position for left
    # TC: O(N), SC: O(N)
    def serialize(self, root):
        if not root:
            return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("None")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)
    
    def deserialize(self, data):
        if len(data) == 0:
            return None
        serial = data.split(',')
        q = deque([])
        root = TreeNode(int(serial[0]))
        q.append(root)
        index = 1
        while q:
            node = q.popleft()
            if serial[index] != "None":
                node.left = TreeNode(int(serial[index]))
                q.append(node.left)
            index += 1
            if serial[index] != "None":
                node.right = TreeNode(int(serial[index]))
                q.append(node.right)
            index += 1
        return root
