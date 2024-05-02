import { main } from ".";

test("test case 1", () => {
  const nums = [4, 5, 6, 7, 0, 1, 2];
  const target = 0;
  const result = 4;
  expect(main(nums, target)).toEqual(result);
});

test("test case 2", () => {
  const nums = [4, 5, 6, 7, 0, 1, 2];
  const target = 3;
  const result = -1;
  expect(main(nums, target)).toEqual(result);
});
test("test case 3", () => {
  const nums = [1];
  const target = 0;
  const result = -1;
  expect(main(nums, target)).toEqual(result);
});

test("test case 4", () => {
  const nums = [4, 5, 6, 7, 0, 1, 2];
  const target = 5;
  const result = 1;
  expect(main(nums, target)).toEqual(result);
});

test("test case 4", () => {
  const nums = [6, 7, 0, 1, 2, 4, 5];
  const target = 5;
  const result = 6;
  expect(main(nums, target)).toEqual(result);
});
