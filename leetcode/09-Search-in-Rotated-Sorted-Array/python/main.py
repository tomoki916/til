import math


class Solution:
    def search(self, nums, target: int) -> int:
        head_index = 0
        tail_index = len(nums) - 1

        result = -1

        while head_index <= tail_index:
            mid_index = math.floor((head_index + tail_index) / 2)

            if nums[mid_index] == target:
                result = mid_index

            if nums[head_index] <= nums[mid_index]:
                # 左側がソートされている場合（右側のどこかで境界がある）
                if nums[head_index] <= target and target < nums[mid_index]:
                    # 左側に存在しているので次のループは左へ
                    tail_index = mid_index - 1
                else:
                    # 左側には存在しないので次のループは右へ
                    head_index = mid_index + 1
            elif nums[mid_index] <= nums[tail_index]:
                # 右側がソートされている場合（左側のどこかで境界がある）
                if nums[mid_index] < target and target <= nums[tail_index]:
                    # 右側に存在しているので次のループは右へ
                    head_index = mid_index + 1
                else:
                    # 右側には存在していないので次のループは左へ
                    tail_index = mid_index - 1

        return result
