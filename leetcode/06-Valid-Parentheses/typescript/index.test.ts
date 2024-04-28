import { main } from ".";

test("test case 1", () => {
  const s = "()";
  const result = true;
  expect(main(s)).toEqual(result);
});

test("test case 2", () => {
  const s = "()[]{}";
  const result = true;
  expect(main(s)).toEqual(result);
});

test("test case 3", () => {
  const s = "(]";
  const result = false;
  expect(main(s)).toEqual(result);
});

test("test case 4", () => {
  const s = "([)]";
  const result = false;
  expect(main(s)).toEqual(result);
});

test("test case 5", () => {
  const s = "([{([])}])[]";
  const result = true;
  expect(main(s)).toEqual(result);
});

test("test case 6", () => {
  const s = "[";
  const result = false;
  expect(main(s)).toEqual(result);
});
