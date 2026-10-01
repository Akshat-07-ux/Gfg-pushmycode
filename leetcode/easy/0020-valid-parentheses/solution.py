class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracks = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracks:
                top = stack.pop() if stack else ''

                if top != bracks[char]:
                    return False

            else:
                stack.append(char)

        return len(stack) == 0