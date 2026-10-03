class Solution:
    def longestValidParentheses(self, s: str) -> int:

        st = [-1]
        win = 0

        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)

            else:
                st.pop()
                if not st:
                    st.append(i)

                else:
                    win = max(win, i - st[-1])

        return win
        