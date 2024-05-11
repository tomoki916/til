import { myPow } from ".";

test("test case 1", () => {
  const x = 2.0;
  const n = 10;
  const answer = 1024.0;
  expect(myPow(x, n)).toEqual(answer);
});

test("test case 2", () => {
  const x = 2.1;
  const n = 3;
  const answer = 9.261;
  expect(myPow(x, n)).toEqual(answer);
});

test("test case 3", () => {
  const x = 2.0;
  const n = -2;
  const answer = 0.25;
  expect(myPow(x, n)).toEqual(answer);
});

test("test case 4", () => {
  const x = 23.0;
  const n = 0;
  const answer = 1;
  expect(myPow(x, n)).toEqual(answer);
});

test("test case 5", () => {
  const x = 1.0;
  const n = 2147483647;
  const answer = 1;
  expect(myPow(x, n)).toEqual(answer);
});
