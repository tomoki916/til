import { main } from ".";

test("test case 1", () => {
  const nums = [1, 2, 3];
  const result = [1, 3, 2];
  expect(main(nums)).toEqual(result);
});

test("test case 2", () => {
  const nums = [3, 2, 1];
  const result = [1, 2, 3];
  expect(main(nums)).toEqual(result);
});
test("test case 3", () => {
  const nums = [1, 1, 5];
  const result = [1, 5, 1];
  expect(main(nums)).toEqual(result);
});

test("test case 4", () => {
  const nums = [1, 3, 2];
  const result = [2, 1, 3];
  expect(main(nums)).toEqual(result);
});

test("test case 4", () => {
  const nums = [1, 2];
  const result = [2, 1];
  expect(main(nums)).toEqual(result);
});

test("test case 5", () => {
  const nums = [1, 2, 3, 4];
  const result = [1, 2, 4, 3];
  expect(main(nums)).toEqual(result);
});

test("test case 6", () => {
  const nums = [4, 1, 3, 7, 6, 5, 2];
  const result = [4, 1, 5, 2, 3, 6, 7];
  expect(main(nums)).toEqual(result);
});
