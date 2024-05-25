from mylib.python.binary_search_tree import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        # node = TreeNode(preorder[0])

        # rootIndex = inorder.index(preorder[0])

        # preorder = preorder[1:]
        # node.left = self.buildTree(
        #     preorder[:rootIndex], inorder[:rootIndex])
        # node.right = self.buildTree(
        #     preorder[rootIndex:], inorder[rootIndex+1:])

        currentValue = preorder.pop(0)
        node = TreeNode(currentValue)
        rootIndex = inorder.index(currentValue)
        node.left = self.buildTree(preorder, inorder[:rootIndex])
        node.right = self.buildTree(preorder, inorder[rootIndex+1:])

        return node
