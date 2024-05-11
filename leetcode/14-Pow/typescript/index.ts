export function myPow(x: number, n: number): number {
  const isNegative = n < 0;
  let result = 1;
  n = Math.abs(n);

  while (n > 0) {
    if (n % 2 === 1) result *= x;
    x *= x;
    n = Math.floor(n / 2);
  }
  return isNegative ? 1 / result : result;
}
