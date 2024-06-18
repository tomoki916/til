class Solution:
    def findMin(self, nums) -> int:
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2

            if nums[head] <= nums[mid] and nums[tail] < nums[head]:
                # 左半分が順番通りになっていて、右半分のどこかに切れ目がある場合
                # この時は右半分に答えがある
                head = mid+1
            elif nums[mid] < nums[tail] and nums[tail] < nums[head]:
                # 右半分が順番通りになっていて、左半分のどこかに切れ目がある場合
                # この時は左半分に答えがある
                tail = mid
            else:
                # 範囲内が正しくソートされている場合
                # この時の左端が最小値
                return nums[head]
