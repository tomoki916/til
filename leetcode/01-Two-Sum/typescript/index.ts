export const main = (nums: number[], target: number): number[] => {
  return hashMap(nums, target);
};

const bruteForce = (nums: number[], target: number): number[] => {
  let answer = [0, 0];
  loop: for (let i = 0; i < nums.length; i++) {
    let sum;
    for (let j = i + 1; j < nums.length; j++) {
      sum = nums[i] + nums[j];
      if (sum === target) {
        answer = [i, j];
        break loop;
      }
    }
  }
  return answer;
};

const hashMap = (nums: number[], target: number): number[] => {
  let answer = [0, 0];
  const map = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    const prev = map.get(diff);
    if (prev === 0 || !!prev) {
      answer = [prev, i];
      break;
    }
    map.set(nums[i], i);
  }
  return answer;
};
