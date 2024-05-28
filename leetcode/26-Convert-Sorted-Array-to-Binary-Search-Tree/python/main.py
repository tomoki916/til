from mylib.python.binary_search_tree import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        center = len(nums) // 2

        node = TreeNode(nums[center])
        node.left = self.sortedArrayToBST(nums[:center])
        node.right = self.sortedArrayToBST(nums[center+1:])

        return node
