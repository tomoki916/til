export function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
  let result = 0;
  // const goalX = obstacleGrid[0].length - 1;
  // const goalY = obstacleGrid.length - 1;

  // if (obstacleGrid[0][0] === 1) {
  //   return result;
  // }

  // const move = (x: number, y: number) => {
  //   if (goalX === x && goalY === y) {
  //     result += 1;
  //     return;
  //   }

  //   // 右に動ける場合
  //   if (x < goalX && obstacleGrid[y][x + 1] === 0) {
  //     move(x + 1, y);
  //   }

  //   // 下に動ける場合
  //   if (y < goalY && obstacleGrid[y + 1][x] === 0) {
  //     move(x, y + 1);
  //   }
  // };

  // move(0, 0);

  const rows = obstacleGrid.length;
  const cols = obstacleGrid[0].length;

  // エッジケースを先に処理する
  if (obstacleGrid[0][0] === 1) return result;
  if (obstacleGrid[rows - 1][cols - 1] === 1) return result;

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (row === 0 && col === 0) {
        obstacleGrid[row][col] = 1;
        continue;
      }
      if (obstacleGrid[row][col] === 1) {
        obstacleGrid[row][col] = 0;
      } else {
        const up = row > 0 ? obstacleGrid[row - 1][col] : 0;
        const left = col > 0 ? obstacleGrid[row][col - 1] : 0;
        obstacleGrid[row][col] = left + up;
      }
    }
  }
  result = obstacleGrid[rows - 1][cols - 1];
  return result;
}
