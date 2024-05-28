export function maxProfit(prices: number[]): number {
  if (prices.length === 1) return 0;
  let result = 0;
  let buyDay = 0;
  for (let i = 1; i < prices.length; i++) {
    const profit = prices[i] - prices[buyDay];
    if (profit < 0) {
      buyDay = i;
    }
    result = Math.max(profit, result);
  }

  return result;
}
