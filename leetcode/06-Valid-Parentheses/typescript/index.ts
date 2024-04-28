export const main = (s: string): boolean => {
  return first(s);
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

  return array.length === 0;
};
