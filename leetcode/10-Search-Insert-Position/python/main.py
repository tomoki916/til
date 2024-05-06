class Solution:
    def searchInsert(self, nums, target: int) -> int:
        head_index = 0
        tail_index = len(nums) - 1
        result = 0

        while head_index <= tail_index:
            mid_index = (head_index + tail_index) // 2

            if nums[mid_index] == target:
                result = mid_index
                break

            if nums[head_index] <= target < nums[mid_index]:
                # 左側にあるので次のループは左
                tail_index = mid_index - 1
            elif nums[mid_index] < target <= nums[tail_index]:
                # 右側にあるので次のループは右
                head_index = mid_index + 1
            elif target < nums[head_index]:
                result = head_index
                break
            elif nums[tail_index] < target:
                result = tail_index + 1
                break

        return result
