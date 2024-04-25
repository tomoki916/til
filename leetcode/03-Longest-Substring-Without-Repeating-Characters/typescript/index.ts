export const main = (s: string): number => {
  return slideWindow(s)
}

const slideWindow = (s: string) => {
  const map = new Map<string, number>();
  let result = 0

  let head = 0
  for (let tail = 0; tail < s.length; tail++) {
    if (map.has(s[tail])) {
      // headを動かす
      head = map.get(s[tail]) ?? 0
    }
    result = Math.max(result, tail - head)
    map.set(s[tail], tail)
  }
  return result
}

const tmp = (s: string): number => {
  let result = 0 // max length
  const sArray = s.split('')
  for (let i = 0; i < sArray.length; i++) {
    const currentSubstring = [sArray[i]]

    for (let j = i+1; j < sArray.length; j++ ) {
      if (currentSubstring.includes(sArray[j])) break
      currentSubstring.push(sArray[j])
    }
    if(currentSubstring.length > result) result = currentSubstring.length
  }

  return result
}