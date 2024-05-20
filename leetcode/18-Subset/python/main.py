class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(path, nums):
            result.append(path)

            for i in range(len(nums)):
                path.append(nums[i])
                backtrack(path[:], nums[i+1:])
                path.pop()

        backtrack([], nums)

        return result
