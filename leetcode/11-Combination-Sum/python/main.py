class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        self.backtrack([], candidates, target, result)

        return result

    def backtrack(self, current, candidates, target, result):
        if sum(current) == target:
            result.append(current)
            return
        if sum(current) > target:
            return

        for i in range(len(candidates)):
            current.append(candidates[i])
            self.backtrack(current[:], candidates[i:], target, result)
            current.pop()
