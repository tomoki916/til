import { maxSubArray } from ".";

test("test case 1", () => {
  const nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
  const answer = 6; //  [4,-1,2,1]
  expect(maxSubArray(nums)).toEqual(answer);
});

test("test case 2", () => {
  const nums = [1];
  const answer = 1;
  expect(maxSubArray(nums)).toEqual(answer);
});

test("test case 3", () => {
  const nums = [5, 4, -1, 7, 8];
  const answer = 23; // [5,4,-1,7,8]
  expect(maxSubArray(nums)).toEqual(answer);
});

test("test case 4", () => {
  const nums = [-1, -2, -3, -4, -5];
  const answer = -1; //
  expect(maxSubArray(nums)).toEqual(answer);
});

test("test case 4", () => {
  const nums = [-1, -2, -3, -4, -5, 5];
  const answer = 5; //
  expect(maxSubArray(nums)).toEqual(answer);
});
