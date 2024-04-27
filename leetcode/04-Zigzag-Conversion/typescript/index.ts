export const main = (s: string, numRows: number): string => {
  return tmp(s, numRows);
};

const tmp = (s: string, numRows: number): string => {
  const sArray = s.split("");

  const rows = new Array(numRows);
  for (let i = 0; i < rows.length; i++) {
    rows[i] = new Array<string>();
  }

  let currentRow = 0;
  let isReverse = false;
  for (let i = 0; i < sArray.length; i++) {
    rows[currentRow].push(sArray[i]);
    if (currentRow === 0) isReverse = false;
    if (currentRow === numRows - 1) isReverse = true;

    if (numRows > 1) {
      currentRow += isReverse ? -1 : 1;
    }
  }

  return rows.flat().join("");
};
