export function maxSubArray(nums: number[]): number {
  let result = -10000;
  let currentSum = 0;
  for (let i = 0; i < nums.length; i++) {
    // for (let j = i; j < nums.length; j++) {
    //   const sum = nums.slice(i, j + 1).reduce((acc, cal) => acc + cal, 0);
    //   result = result > sum ? result : sum;
    // }
    currentSum += nums[i];
    if (currentSum > result) result = currentSum;
    if (currentSum < 0) currentSum = 0;
  }
  return result;
}
