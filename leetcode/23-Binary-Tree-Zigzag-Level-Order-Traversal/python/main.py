from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        q.append({"node": root, "depth": 0})

        result = []
        while len(q) > 0:
            currentNode = q.popleft()
            if not currentNode["node"]:
                continue
            if len(result) <= currentNode["depth"]:
                result.append([])

            result[currentNode["depth"]].append(currentNode["node"].val)

            q.append(
                {"node": currentNode["node"].left, "depth": currentNode["depth"] + 1})
            q.append(
                {"node": currentNode["node"].right, "depth": currentNode["depth"] + 1})

        for i in range(len(result)):
            if i % 2 == 1:
                result[i].reverse()

        return result
