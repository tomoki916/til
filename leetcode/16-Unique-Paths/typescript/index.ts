export function uniquePaths(m: number, n: number): number {
  // Combination: (m+n-2)C(m-1)
  let top = 1;
  let bottom = 1;

  for (let i = 0; i < m - 1; i++) {
    top *= m + n - 2 - i;
    bottom *= m - 1 - i;
  }

  return top / bottom;
}
