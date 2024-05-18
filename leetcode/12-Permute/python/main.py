class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 0:
            return result

        def backtrace(path, candidates):
            if len(path) == len(nums):
                result.append(path)
                return

            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrace(path[:], candidates[:i] + candidates[i+1:])
                path.pop()

        backtrace([], nums)

        return result
