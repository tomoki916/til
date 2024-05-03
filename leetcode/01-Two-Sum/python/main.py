class Solution:
  def twoSums(self, nums, target):
    result = []
    map = {}

    for index in range(len(nums)):
      num = nums[index]
      diff = target - num
      if num in map:
        result.append(index)
        result.append(map[num])

      map[diff] = index

    result.sort()
    return result
