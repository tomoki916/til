import { permute } from ".";

test("test case 1", () => {
  const nums = [1, 2, 3];
  const answer = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
  ];
  expect(permute(nums)).toEqual(answer);
});

test("test case 2", () => {
  const nums = [0, 1];
  const answer = [
    [0, 1],
    [1, 0],
  ];
  expect(permute(nums)).toEqual(answer);
});

test("test case 3", () => {
  const nums = [1];
  const answer = [[1]];
  expect(permute(nums)).toEqual(answer);
});
