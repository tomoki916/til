from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if not endWord in wordList:
            return 0

        # 変換表を作る
        # allComboDict = defaultdict(list)
        # wordLength = len(beginWord)
        # for word in wordList:
        #     for i in range(wordLength):
        #         allComboDict[word[:i] + "*" + word[i+1:]].append(word)

        # print("allCombo", allComboDict)

        # # BFS
        # step = 1
        # queue = deque()
        # queue.append(beginWord)

        # visited = set()
        # visited.add(beginWord)

        # while len(queue) > 0:
        #     currentQueueLength = len(queue)

        #     for _ in range(currentQueueLength):
        #         current = queue.popleft()

        #         # １文字だけ違う単語を抽出する。
        #         for i in range(wordLength):
        #             key = current[:i] + "*" + current[i+1:]
        #             for word in allComboDict[key]:
        #                 if word == endWord:
        #                     return step + 1
        #                 if not word in visited:
        #                     visited.add(word)
        #                     queue.append(word)

        #     step += 1

        # return 0

        # backtrackは時間がかかりすぎる
        result = {"value": len(wordList)+1}
        visited = set()
        visited.add(beginWord)

        def backtrack(currntStep, beginWord, endWord, wordList, path, result):
            if currntStep > result["value"]:
                return
            if self.isDifferntOnlyOneChar(beginWord, endWord):
                # 見つかった場合
                result["value"] = min(result["value"], currntStep+1)
                return

            # wordListの中から１文字だけ違う単語を抜き出す
            nextEndWords = [
                word for word in wordList if self.isDifferntOnlyOneChar(endWord, word) and not word in visited]

            for next in nextEndWords:
                nextPath = [*path, next]
                visited.add(next)
                backtrack(currntStep+1,
                          beginWord,
                          next,
                          [word for word in wordList if not word in nextPath],
                          nextPath,
                          result
                          )

        backtrack(1, beginWord, endWord, wordList, [], result)

        # 該当するパスがなかった場合
        if result["value"] == len(wordList) + 1:
            return 0

        return result["value"]

    def isDifferntOnlyOneChar(self, str1, str2):
        # 2つの文字列が１文字だけ違うかを判別する
        # 文字列の長さは常に同じ
        differntNum = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                differntNum += 1

        return differntNum == 1
