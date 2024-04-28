export const main = (n: number): string[] => {
  return backTrack(n);
};

const backTrack = (n: number): string[] => {
  const result = new Array<string>();
  _backTrack(result, "", 0, 0, n);

  return result;
};

const _backTrack = (
  result: Array<string>,
  s: string,
  open: number,
  close: number,
  max: number
) => {
  if (s.length === max * 2) {
    result.push(s);
    return;
  }

  if (open < max) _backTrack(result, s + "(", open + 1, close, max);
  if (close < open) _backTrack(result, s + ")", open, close + 1, max);
};

const first = (n: number): string[] => {
  // すべてのパターンを列挙した後、正しい形式のものだけに絞って返却する

  // ありうるすべてのパターンを列挙する
  const allList: Set<string> = createParentheses(n);
  // console.log("n", n);
  // console.log("all num", allList.size);

  const answer = [...allList].filter((item) => isValidParenthes(item));
  console.log("num", answer.length);
  // console.log("all list", answer);

  return answer.sort();
};

// これだと数え上げられない
const createParentheses = (n: number): Set<string> => {
  if (n === 1) {
    return new Set(["()", ")("]);
  } else {
    const set = new Set<string>();
    const prevSet = createParentheses(n - 1);
    prevSet.forEach((s) =>
      [`()${s}`, `(${s})`, `${s}()`, `)(${s}`, `)${s}(`, `${s})(`].forEach(
        (item) => set.add(item)
      )
    );
    return set;
  }
};

const isValidParenthes = (s: string): boolean => {
  const stack = new Array<string>();
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(s[i]);
    } else if (s[i] === ")") {
      if (stack.length === 0) return false;
      stack.pop();
    } else {
      return false;
    }
  }

  return stack.length === 0;
};

const kataran = [1, 2, 5, 14, 42, 132, 429, 1430];

// for (let i = 0; i < 8; i++) {
//   console.log("== n=", i + 1, "==");
//   main(i + 1);
//   console.log("Theory", kataran[i]);
// }

// main(4);
