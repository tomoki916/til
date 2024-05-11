export function groupAnagrams(strs: string[]): string[][] {
  const cache: Map<string, string[]> = new Map();

  for (let i = 0; i < strs.length; i++) {
    const currentStr = strs[i];
    const tmpKey = currentStr.split("").sort().join("");
    if (!cache.has(tmpKey)) cache.set(tmpKey, []);
    cache.get(tmpKey)?.push(currentStr);
  }

  return Array.from(cache.values());
}
