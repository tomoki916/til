import { subsets } from ".";

test("test case 1", () => {
  const nums = [1, 2, 3];
  const answer = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]];
  expect(subsets(nums).sort()).toEqual(answer.sort());
});

test("test case 2", () => {
  const nums = [0];
  const answer = [[], [0]];
  expect(subsets(nums)).toEqual(answer);
});
