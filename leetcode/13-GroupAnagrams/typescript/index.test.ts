import { groupAnagrams } from ".";

test("test case 1", () => {
  const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
  const answer = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]];
  expect(groupAnagrams(strs)).toEqual(answer);
});

test("test case 2", () => {
  const strs = [""];
  const answer = [[""]];
  expect(groupAnagrams(strs)).toEqual(answer);
});

test("test case 3", () => {
  const strs = ["a"];
  const answer = [["a"]];
  expect(groupAnagrams(strs)).toEqual(answer);
});
