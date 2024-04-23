import { main } from "."

test("test case 1", () => {
  const l1 = [2, 4, 3]
  const l2 = [5, 6, 4]
  const result = [7, 0, 8]
  expect(main(l1, l2)).toEqual(result)
})

test("test case 2", () => {
  const l1 = [0]
  const l2 = [0]
  const result = [0]
  expect(main(l1, l2)).toEqual(result)
})

test("test case 3", () => {
  const l1 = [9,9,9,9,9,9,9]
  const l2 = [9,9,9,9]
  const result = [8,9,9,9,0,0,0,1]
  expect(main(l1, l2)).toEqual(result)
})