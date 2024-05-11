import { combinationSum } from ".";

test("test case 1", () => {
  const candidates = [2, 3, 6, 7];
  const target = 7;
  const answer = [[2, 2, 3], [7]];
  expect(combinationSum(candidates, target)).toEqual(answer);
});

test("test case 2", () => {
  const candidates = [2, 3, 5];
  const target = 8;
  const answer = [
    [2, 2, 2, 2],
    [2, 3, 3],
    [3, 5],
  ];
  expect(combinationSum(candidates, target)).toEqual(answer);
});

test("test case 3", () => {
  const candidates = [2];
  const target = 1;
  const answer: number[] = [];
  expect(combinationSum(candidates, target)).toEqual(answer);
});
