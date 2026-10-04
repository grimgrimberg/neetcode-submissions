class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        bracket_map = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in bracket_map:
                if stack and stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        # middle = n //2
        # middle_string = s[middle:n:1]
        # print(n)
        # print(middle)
        # print(middle_string)
        # print(s)
        # if n%2: #if odd
        #     return False

        # return True
        # for i in range(n):
        #     if ord(s[i]) -1 != ord(s[n-1-i]):
        #         return False
        # return True
