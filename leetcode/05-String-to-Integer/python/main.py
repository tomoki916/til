class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0

        # 変換表
        map = {
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '0': 0,
        }

        # 頭の空白を取り除く
        for i in range(len(s)):
            if not s[i] == ' ':
                s = s[i:]
                break

        # 符号を確認する
        negative = False
        if len(s) > 0 and s[0] == '-':
            # 先頭にマイナスがある時
            negative = True
            s = s[1:]
        elif len(s) > 0 and s[0] == '+':
            # 先頭にプラスがある時
            negative = False
            s = s[1:]
        # 先頭に符号がない時は何もしない

        # 数字以外が現れるまで読み込む
        for i in range(len(s)):
            if not s[i] in map:
                s = s[:i]
                break

        # 数字に変換する
        for i in range(len(s)):
            currentCar = s[i]
            currentNum = map[s[i]]

            result += currentNum * 10 ** (len(s) - 1 - i)

        # 符号を反映する
        result = result * -1 if negative else result

        # 範囲を確認
        result = (-2)**31 if result < (-2)**31 else result
        result = 2**31-1 if 2**31-1 < result else result

        return result
