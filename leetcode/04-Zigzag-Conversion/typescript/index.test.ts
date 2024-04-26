import { main } from ".";

test("test case 1", () => {
  const s = "PAYPALISHIRING";
  const numRows = 3;
  const result = "PAHNAPLSIIGYIR";
  expect(main(s, numRows)).toEqual(result);
});

test("test case 2", () => {
  const s = "PAYPALISHIRING";
  const numRows = 4;
  const result = "PINALSIGYAHRPI";
  expect(main(s, numRows)).toEqual(result);
});

test("test case 3", () => {
  const s = "A";
  const numRows = 1;
  const result = "A";
  expect(main(s, numRows)).toEqual(result);
});
