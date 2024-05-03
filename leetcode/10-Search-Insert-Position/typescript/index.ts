export const main = (nums: number[], target: number): number => {
  return first(nums, target);
};

const first = (nums: number[], target: number): number => {
  let low = 0;
  let high = nums.length - 1;
  let result = 0;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    let midNum = nums[mid];

    if (midNum === target) {
      result = mid;
      break;
    }

    if (target < midNum) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  // 見つからなかった時
  if (low > high) {
    if (nums[high] > target) {
      result = high;
    } else {
      result = high + 1;
    }
  }

  return result;
};
