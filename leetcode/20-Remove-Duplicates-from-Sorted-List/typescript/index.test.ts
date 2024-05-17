import {
  convertListNodeToList,
  convertListToListNode,
  deleteDuplicates,
} from ".";

test("test case 1", () => {
  const head = [1, 1, 2];

  const answer = [1, 2];
  expect(
    convertListNodeToList(deleteDuplicates(convertListToListNode(head)))
  ).toEqual(answer);
});

test("test case 2", () => {
  const head = [1, 1, 2, 3, 3];

  const answer = [1, 2, 3];
  expect(
    convertListNodeToList(deleteDuplicates(convertListToListNode(head)))
  ).toEqual(answer);
});

test("test case 3", () => {
  const head = [1, 2, 3, 4, 5];

  const answer = [1, 2, 3, 4, 5];
  expect(
    convertListNodeToList(deleteDuplicates(convertListToListNode(head)))
  ).toEqual(answer);
});
