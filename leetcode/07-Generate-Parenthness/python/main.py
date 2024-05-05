class Solution:
    def generateParenthesis(self, n: int):
        result = []
        # self.tmp(n, "", 0, 0, result)
        self.another(n, 0, 0, "", result)
        return result

    def tmp(self, n, s, counter, total, result):
        if len(s) == 2*n:
            result[s] = ""
            return

        if counter == 0:
            self.tmp(n, s + "(", counter + 1, total + 1, result)
        else:
            self.tmp(n, s + ")", counter - 1, total, result)

        if total < n:
            self.tmp(n, s + "(", counter + 1, total + 1, result)

    def another(self, n, left, right, s, result):
        if len(s) == 2*n:
            result.append(s)
            return

        if left < n:
            self.another(n, left+1, right, s + "(", result)
        if right < left:
            self.another(n, left, right+1, s + ")", result)
