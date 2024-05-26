# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # result = {"value": 10**5}

        # def backtrack(node, currentDepth, result):
        #     if node.left:
        #         backtrack(node.left, currentDepth+1, result)

        #     if node.right:
        #         backtrack(node.right, currentDepth+1, result)

        #     if not node.left and not node.right:
        #         result["value"] = min(result["value"], currentDepth)
        #         return

        # backtrack(root, 1, result)

        # return result["value"]
        if not root.left and not root.right:
            return 1

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if not root.left:
            return rightDepth + 1

        if not root.right:
            return leftDepth + 1

        return min(leftDepth, rightDepth) + 1
