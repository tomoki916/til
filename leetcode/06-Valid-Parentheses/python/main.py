class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        stack = []

        for currentChar in s:
            if currentChar == "(" or currentChar == "[" or currentChar == "{":
                stack.append(currentChar)
            elif currentChar == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            elif currentChar == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            elif currentChar == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                result = False
                break

        if len(stack) > 0:
            result = False

        return result
