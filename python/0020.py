class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for item in s:
            if item in mapping:
                if len(stack) >= 1:
                    if stack[len(stack)-1] == mapping[item]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(item)

        return not stack
