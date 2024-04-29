import { ListNode, main } from ".";

test("test case 1", () => {
  const l1: ListNode = new ListNode(2, new ListNode(4, new ListNode(3)));
  const l2: ListNode = new ListNode(5, new ListNode(6, new ListNode(4)));
  const result = new ListNode(7, new ListNode(0, new ListNode(8)));
  expect(main(l1, l2)).toEqual(result);
});

// test("test case 2", () => {
//   const l1 = [0];
//   const l2 = [0];
//   const result = [0];
//   expect(main(l1, l2)).toEqual(result);
// });

// test("test case 3", () => {
//   const l1 = [9, 9, 9, 9, 9, 9, 9];
//   const l2 = [9, 9, 9, 9];
//   const result = [8, 9, 9, 9, 0, 0, 0, 1];
//   expect(main(l1, l2)).toEqual(result);
// });

// test("test case 4", () => {
//   const l1 = [9, 9, 9];
//   const l2 = [1];
//   const result = [0, 0, 0, 1];
//   expect(main(l1, l2)).toEqual(result);
// });
