class Solution:
    def isValid(self, s: str) -> bool:
        """
        1st approach using stack data structure
        """
        n = len(s)
        stack = []

        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" or char == "}" or char == "]":
                if not stack:
                    return False
                if char == ")" and stack[-1] != "(":
                    return False
                if char == "}" and stack[-1] != "{":
                    return False
                if char == "]" and stack[-1] != "[":
                    return False

                stack.pop()
            else:
                return False
        return len(stack) == 0