export const main = (s: string): boolean => {
  return second(s);
};

const first = (s: string): boolean => {
  const pare = new Map<string, string>([
    ["(", ")"],
    ["{", "}"],
    ["[", "]"],
  ]);
  const stack = new Array<string>();

  for (let i = 0; i < s.length; i++) {
    const tmp = s[i];
    if (pare.has(tmp)) {
      // かっこの左側の時
      stack.push(tmp);
    } else {
      // かっこの右側の時
      if (pare.get(stack[stack.length - 1]) === tmp) {
        stack.pop();
      } else {
        return false;
      }
    }
  }

  return stack.length === 0;
};

const second = (s: string): boolean => {
  const stack = new Array<string>();
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "{" || s[i] === "[") {
      stack.push(s[i]);
    } else if (s[i] === ")" && stack.at(-1) === "(") {
      stack.pop();
    } else if (s[i] === "}" && stack.at(-1) === "{") {
      stack.pop();
    } else if (s[i] === "]" && stack.at(-1) === "[") {
      stack.pop();
    } else {
      return false;
    }
  }

  return stack.length === 0;
};
