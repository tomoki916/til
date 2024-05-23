class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(node, result, currentDepth):
            if not node:
                return

            if currentDepth >= len(result):
                result.append([node.val])
            else:
                result[currentDepth].append(node.val)

            backtrack(node.left, result, currentDepth + 1)
            backtrack(node.right, result, currentDepth + 1)

        backtrack(root, result, 0)
        return result
