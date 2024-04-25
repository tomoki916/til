import { main } from "."

test("test case 1", () => {
  const s = "abcabcbb"
  const result = 3
  expect(main(s)).toEqual(result)
})

test("test case 2", () => {
  const s = "bbbbb"
  const result = 1
  expect(main(s)).toEqual(result)
})

test("test case 3", () => {
  const s = "pwwkew"
  const result = 3
  expect(main(s)).toEqual(result)
})
