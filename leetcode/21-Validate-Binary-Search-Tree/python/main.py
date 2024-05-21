class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def backtrack(currentNode, min, max, result):
            if not currentNode:
                return

            if not (min < currentNode.val < max):
                result["value"] = False
                return

            backtrack(currentNode.left, min, currentNode.val, result)
            backtrack(currentNode.right, currentNode.val, max, result)

        result = {"value": True}
        backtrack(root, -(2**31)-1, 2**31, result)

        return result["value"]
