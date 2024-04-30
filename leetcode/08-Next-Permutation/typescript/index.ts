export const main = (nums: number[]): number[] => {
  solution(nums);
  return nums;
};

const first = (nums: number[]): void => {
  if (nums.length === 1) return;
  if (nums.length === 2) {
    nums = [nums[1], nums[0]];
    return;
  }

  if (nums[nums.length - 1] > nums[nums.length - 2]) {
    const tmp = nums[nums.length - 1];
    nums[nums.length - 1] = nums[nums.length - 2];
    nums[nums.length - 2] = tmp;
  } else {
    nums.sort();
  }
};

// ref: https://leetcode.com/problems/next-permutation/solutions/4826050/easy-nextpermutation
const solution = (nums: number[]): void => {
  // numsの要素が1つの場合は処理する必要がない
  if (nums.length === 1) return;

  // Step1: num[i] < num[i+1]を満たす最大のindex iを求める
  let i: number = nums.length - 2;
  for (i; i >= 0; i--) {
    if (nums[i] < nums[i + 1]) break;
  }

  // Step2: num[j] > num[i]を満たす最大のindex jを求める
  let j: number = nums.length - 1;
  for (j; j > i; j--) {
    if (nums[j] > nums[i]) break;
  }

  // Step3: num[i]とnum[j]を入れ替える
  [nums[i], nums[j]] = [nums[j], nums[i]];

  // Step4: nums[i]より後ろを反転する
  reverse(nums, i + 1, nums.length - 1);
};

const reverse = (
  nums: number[],
  startIndex: number,
  endIndex: number
): void => {
  while (startIndex < endIndex) {
    [nums[startIndex], nums[endIndex]] = [nums[endIndex], nums[startIndex]];
    startIndex++;
    endIndex--;
  }
};
