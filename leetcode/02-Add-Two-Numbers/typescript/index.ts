export const main = (l1: number[], l2: number[]) => {
  const l1Int = l1.reduce((acc: number, val: number, index: number) => {
    return acc + val * 10 ** index
  }, 0)

  const l2Int = l2.reduce((acc: number, val: number, index: number) => {
    return acc + val * 10 ** index
  }, 0)

  const sum = l1Int + l2Int
  const result: number[] = []
  let resultInt = sum
  if (resultInt === 0) result.push(0)
  while (resultInt > 0) {
    const value = resultInt % 10
    result.push(value)
    resultInt = Math.floor(resultInt / 10)
  }
  return result
}

