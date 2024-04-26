import { main } from "."

test("test case 1", () => {
  const s = "42"
  const result = 42
  expect(main(s)).toEqual(result)
})

test("test case 2", () => {
  const s = "   -42"
  const result = -42
  expect(main(s)).toEqual(result)
})

test("test case 3", () => {
  const s = "4193 with words"
  const result = 4193
  expect(main(s)).toEqual(result)
})
