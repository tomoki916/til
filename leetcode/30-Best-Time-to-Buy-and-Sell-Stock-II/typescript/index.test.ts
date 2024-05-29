import { maxProfit } from ".";

test("test case 1", () => {
  const prices = [7, 1, 5, 3, 6, 4];
  const answer = 7;
  expect(maxProfit(prices)).toEqual(answer);
});

test("test case 2", () => {
  const prices = [1, 2, 3, 4, 5];
  const answer = 4;
  expect(maxProfit(prices)).toEqual(answer);
});

test("test case 3", () => {
  const prices = [7, 6, 4, 3, 1];
  const answer = 0;
  expect(maxProfit(prices)).toEqual(answer);
});

test("test case 4", () => {
  const prices = [1, 2];
  const answer = 1;
  expect(maxProfit(prices)).toEqual(answer);
});
