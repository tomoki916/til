import { maxProfit } from ".";

test("test case 1", () => {
  const prices = [7, 1, 5, 3, 6, 4];
  const answer = 5;
  expect(maxProfit(prices)).toEqual(answer);
});

test("test case 2", () => {
  const prices = [7, 6, 4, 3, 1];
  const answer = 0;
  expect(maxProfit(prices)).toEqual(answer);
});
