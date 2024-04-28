import { main } from ".";

test("test case 1", () => {
  const s = "42";
  const result = 42;
  expect(main(s)).toEqual(result);
});

test("test case 2", () => {
  const s = "   -42";
  const result = -42;
  expect(main(s)).toEqual(result);
});

test("test case 3", () => {
  const s = "4193 with words";
  const result = 4193;
  expect(main(s)).toEqual(result);
});

test("test case 4", () => {
  const s = "+1";
  const result = 1;
  expect(main(s)).toEqual(result);
});

test("test case 5", () => {
  const s = "+-12";
  const result = 0;
  expect(main(s)).toEqual(result);
});

test("test case 6", () => {
  const s = "00000-42a1234";
  const result = 0;
  expect(main(s)).toEqual(result);
});
