class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        map = {}
        for end in range(len(s)):
            currentChar = s[end]
            if currentChar in map and start <= map[currentChar]:
                # すでに今の文字が出てきていたらstart位置をずらす
                start = map[currentChar] + 1

            # 現在の文字をmapに保存する
            map[currentChar] = end

            currentLength = end - start + 1
            result = currentLength if currentLength > result else result

        return result
