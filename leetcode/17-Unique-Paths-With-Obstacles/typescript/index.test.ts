import { uniquePathsWithObstacles } from ".";

test("test case 1", () => {
  const obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
  ];
  const answer = 2;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 2", () => {
  const obstacleGrid = [
    [0, 1],
    [0, 0],
  ];
  const answer = 1;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 3", () => {
  const obstacleGrid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0],
  ];
  const answer = 1;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 4", () => {
  const obstacleGrid = [[1]];
  const answer = 0;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 5", () => {
  const obstacleGrid = [
    [0, 1],
    [1, 0],
  ];
  const answer = 0;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 6", () => {
  const obstacleGrid = [[0]];
  const answer = 1;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 7", () => {
  const obstacleGrid = [[0, 1]];
  const answer = 0;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});

test("test case 8", () => {
  const obstacleGrid = [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
  ];
  const answer = 1;
  expect(uniquePathsWithObstacles(obstacleGrid)).toEqual(answer);
});
