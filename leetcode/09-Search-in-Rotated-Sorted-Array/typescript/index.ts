export const main = (nums: number[], target: number): number => {
  return solution(nums, target);
};

const first = (nums: number[], target: number): number => {
  let index = 0;
  tmp(nums, target, index);
  return index;
};

const tmp = (nums: number[], target: number, index: number): number => {
  console.log("nums", nums);
  if (nums.length === 1) {
    if (nums[0] === target) {
      return index;
    } else {
      return -1;
    }
  }

  const centerIndex = Math.floor(nums.length / 2);
  const center = nums[centerIndex];
  if (center === target) {
    index += centerIndex;
  }

  if (nums[0] <= target && target <= center) {
    return tmp(nums.slice(0, centerIndex), target, index);
  } else {
    index += centerIndex + 1;
    return tmp(nums.slice(centerIndex + 1), target, index);
  }
};

// ref: https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/4080241/optimal-solution-using-binary-search
const solution = (nums: number[], target: number): number => {
  let low = 0;
  let high = nums.length - 1;
  let result = -1;

  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    const num = nums[mid];

    if (num === target) {
      result = mid;
      break;
    }

    // 左側がソートされている
    if (nums[low] <= num) {
      if (nums[low] <= target && target <= num) {
        // 左側の配列にtargetが入っているので左側を次の対象にする
        high = mid - 1;
      } else {
        // 右側の配列にtargetが入っているので右側を次の対象にする
        low = mid + 1;
      }
    } else {
      if (num <= target && target <= nums[high]) {
        // 右側の配列にtargetが入っているので右側を次の対象にする
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
  }
  return result;
};
