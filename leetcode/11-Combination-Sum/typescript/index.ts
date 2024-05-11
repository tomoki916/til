export function combinationSum(
  candidates: number[],
  target: number
): number[][] {
  const answer: number[][] = [];

  const backTrack = (candidates: number[], path: number[]): void => {
    const sum = path.reduce((acc, cur) => acc + cur, 0);

    if (sum >= target) {
      if (sum === target) answer.push([...path]);
      return;
    }

    for (let i = 0; i < candidates.length; i++) {
      backTrack([...candidates.slice(i)], [...path, candidates[i]]);
    }
  };

  backTrack(candidates, []);

  return answer;
}
