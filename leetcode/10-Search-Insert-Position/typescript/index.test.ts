import { main } from ".";

test("test case 1", () => {
  const nums = [1, 3, 5, 6];
  const target = 5;
  const result = 2;
  expect(main(nums, target)).toEqual(result);
});

test("test case 2", () => {
  const nums = [1, 3, 5, 6];
  const target = 2;
  const result = 1;
  expect(main(nums, target)).toEqual(result);
});

test("test case 3", () => {
  const nums = [1, 3, 5, 6];
  const target = 7;
  const result = 4;
  expect(main(nums, target)).toEqual(result);
});

test("test case 4", () => {
  const nums = [1];
  const target = 2;
  const result = 1;
  expect(main(nums, target)).toEqual(result);
});

test("test case 5", () => {
  const nums = [1];
  const target = 1;
  const result = 0;
  expect(main(nums, target)).toEqual(result);
});
