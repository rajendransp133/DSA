from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        i = 0
        stack.append("")

        while i < len(s):

            if s[i].isnumeric():
                temp_val = i
                while i < len(s) and s[i].isnumeric():
                    i += 1
                val = stack.pop()
                stack.append(val + s[temp_val:i])
                continue

            if s[i] == "[":
                stack.append("")
                i += 1

            elif s[i] == "]":
                val = stack.pop()
                val2 = stack.pop()

                # extract full number (not just last digit)
                j = len(val2) - 1
                while j >= 0 and val2[j].isdigit():
                    j -= 1

                number = val2[j+1:]
                temp = val2[:j+1]

                for _ in range(int(number)):
                    temp += val

                stack.append(temp)
                i += 1

            else:
                val = stack.pop()
                stack.append(val + s[i])
                i += 1

        return stack[0]