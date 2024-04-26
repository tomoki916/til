export const main = (l1: number[], l2: number[]) => {
  return carry(l1, l2);
};

const carry = (l1: number[], l2: number[]) => {
  const result: number[] = [];
  const maxLength = l1.length >= l2.length ? l1.length : l2.length;
  for (let i = 0; i < maxLength; i++) {
    const sum = (l1[i] ?? 0) + (l2[i] ?? 0) + (result[i] ?? 0);
    const carry = Math.floor(sum / 10);
    const n = sum % 10;

    if (!!result[i]) {
      result[i] = n;
    } else {
      result.push(n);
    }

    if (carry > 0) {
      result.push(carry);
    }
  }
  return result;
};

const toNumber = (l1: number[], l2: number[]) => {
  const l1Int = l1.reduce((acc: number, val: number, index: number) => {
    return acc + val * 10 ** index;
  }, 0);

  const l2Int = l2.reduce((acc: number, val: number, index: number) => {
    return acc + val * 10 ** index;
  }, 0);

  const sum = l1Int + l2Int;
  const result: number[] = [];
  let resultInt = sum;
  if (resultInt === 0) result.push(0);
  while (resultInt > 0) {
    const value = resultInt % 10;
    result.push(value);
    resultInt = Math.floor(resultInt / 10);
  }
  return result;
};
