import { uniquePaths } from ".";

test("test case 1", () => {
  const [m, n] = [3, 7];
  const answer = 28;
  expect(uniquePaths(m, n)).toEqual(answer);
});

test("test case 2", () => {
  const [m, n] = [3, 2];
  const answer = 3;
  expect(uniquePaths(m, n)).toEqual(answer);
});

test("test case 3", () => {
  const [m, n] = [1, 1];
  const answer = 1;
  expect(uniquePaths(m, n)).toEqual(answer);
});

test("test case 4", () => {
  const [m, n] = [2, 1];
  const answer = 1;
  expect(uniquePaths(m, n)).toEqual(answer);
});
