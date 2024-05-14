export function subsets(nums: number[]): number[][] {
  const result: number[][] = [];

  const tmp = (path: number[], index: number) => {
    result.push([...path]);

    for (let i = index; i < nums.length; i++) {
      path.push(nums[i]);

      tmp(path, i + 1);

      path.pop();
    }
  };
  tmp([], 0);

  console.log("result", result);

  return result;
}
