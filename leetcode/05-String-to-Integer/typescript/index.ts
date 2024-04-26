export const main = (s: string): number => {
  return first(s)
}

const first = (s: string): number => {
  const sArray = s.split('')

  let result = 0
  let isLeadingWhiteSpace = true
  let isNegative = false

  // 変換表
  const dijits = new Map<string, number>([
    ['1', 1],
    ['2', 2],
    ['3', 3],
    ['4', 4],
    ['5', 5],
    ['6', 6],
    ['7', 7],
    ['8', 8],
    ['9', 9],
    ['0', 0],
  ])

  for (let i = 0; i < sArray.length; i++ ) {
    // 先頭の空白だけを無視する
    if (sArray[i] !== ' ') isLeadingWhiteSpace = false
    if (isLeadingWhiteSpace) continue
    
    // 正負の判定
    if (sArray[i] === '-') {
      isNegative = true
      continue
    }

    // 数値を読み込む
    const current = dijits.get(sArray[i]) 
    if (current !== undefined) {
      result = result * 10 + current
    } else {
      // 文字を読み込んだので終了する
      break
    }
  }

  // 正負の変換
  if (isNegative) result = -1 * result 

  // 範囲の確認
  result = result < -(2**31) ?  -(2**31) : result
  result = result > 2**31 - 1 ? 2**31 - 1 : result

  return result
}
