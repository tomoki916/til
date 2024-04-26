import { main } from ".";

test("test case 1", () => {
  const nums = [2, 7, 11, 15];
  const target = 9;
  const answer = [0, 1];
  expect(main(nums, target)).toEqual(answer);
});

test("test case 2", () => {
  const nums = [3, 2, 4];
  const target = 6;
  const answer = [1, 2];
  expect(main(nums, target)).toEqual(answer);
});

test("test case 3", () => {
  const nums = [3, 3];
  const target = 6;
  const answer = [0, 1];
  expect(main(nums, target)).toEqual(answer);
});
