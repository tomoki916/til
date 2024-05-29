export function maxProfit(prices: number[]): number {
  if (prices.length === 1) return 0;
  let result = 0;

  for (let i = 1; i < prices.length; i++) {
    const currentProfit = prices[i] - prices[i - 1];
    if (currentProfit > 0) result += currentProfit;
  }

  return result;
}
