# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # result = {"value": False}

        # def backtrack(node, path, result, targetSum):
        #     currentSum = path + node.val

        #     if not node.left and not node.right and currentSum == targetSum:
        #         result["value"] = True
        #         return

        #     if node.left:
        #         backtrack(node.left, currentSum, result, targetSum)

        #     if node.right:
        #         backtrack(node.right, currentSum, result, targetSum)

        # if root:
        #     backtrack(root, 0, result, targetSum)

        # return result["value"]
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum-root.val)
