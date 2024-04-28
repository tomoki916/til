import { main } from ".";

test("test case 1", () => {
  const n = 3;
  const result = ["((()))", "(()())", "(())()", "()(())", "()()()"];
  expect(main(n)).toEqual(result);
});

test("test case 2", () => {
  const n = 1;
  const result = ["()"];
  expect(main(n)).toEqual(result);
});

// test("test case 4", () => {
//   const n = 8;
//   const result: string[] = [];
//   expect(main(n)).toEqual(result);
// });
