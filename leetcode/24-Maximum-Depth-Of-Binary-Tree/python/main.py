# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = {"value": 0}

        def backtrack(node, currentDepth, result):
            if not node:
                result["value"] = max(result["value"], currentDepth)
                return

            backtrack(node.left, currentDepth+1, result)
            backtrack(node.right, currentDepth+1, result)

        backtrack(root, 0, result)

        return result["value"]
