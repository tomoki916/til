class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRowsが１の時はそのまま返す
        if numRows == 1:
            return s

        # ジグザグの表を作る
        table = [[] for _ in range(numRows)]
        currentRow = 0
        goDown = True

        for i in range(len(s)):
            table[currentRow].append(s[i])

            if goDown:
                currentRow += 1
            else:
                currentRow -= 1

            if currentRow == 0:
                goDown = True
            elif currentRow == numRows - 1:
                goDown = False

        # 繋げて文字列にする
        return ''.join([''.join(x) for x in table])
