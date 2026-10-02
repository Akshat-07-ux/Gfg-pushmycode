class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(text):
            stack = []

            for char in text:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()

            return "".join(stack)

        return build(s) == build(t)