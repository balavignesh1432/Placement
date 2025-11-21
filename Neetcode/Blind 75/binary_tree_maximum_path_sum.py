# Logic: Perform DFS, 
# At each step, get left path sum, right path sum
# Find max of left path sum, right path sum, left + right + val (Path centered at node), val(Path ending at val)
# When returning to parent, 
# Path sum to be returned can be either val (Path ends with it), left + val, or right + val
# TC: O(N), SC: O(N)
def maxPathSum(self, root: Optional[TreeNode]) -> int:
    maxSum = float('-inf')
    def helper(node):
        if not node:
            return float('-inf')
        left = helper(node.left)
        right = helper(node.right)
        leftPathSum = left + node.val
        rightPathSum = right + node.val
        nonlocal maxSum
        maxSum = max(maxSum, leftPathSum, rightPathSum, left + right + node.val, node.val)
        return max(leftPathSum, rightPathSum, node.val)   
    helper(root)
    return maxSum