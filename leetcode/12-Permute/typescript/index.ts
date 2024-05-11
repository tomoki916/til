export function permute(nums: number[]): number[][] {
  const result: number[][] = [];

  const backTrack = (nums: number[], currentNums: number[]) => {
    if (nums.length === 0) {
      result.push(currentNums);
    }

    // nums.map((num, index) =>
    //   backTrack(
    //     [...nums.slice(0, index), ...nums.slice(index + 1)],
    //     [...currentNums, num]
    //   )
    // );

    for (let i = 0; i < nums.length; i++) {
      backTrack(
        [...nums.slice(0, i), ...nums.slice(i + 1)],
        [...currentNums, nums[i]]
      );
    }
  };

  backTrack(nums, []);

  return result;
}
