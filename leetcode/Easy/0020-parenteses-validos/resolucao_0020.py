open_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if not s:
            return True

        for char in s:
            if char in open_dict:
                 stack.append(open_dict[char])
            else:
                if stack:
                    char_opening = stack.pop()
                    if not char == char_opening:
                        return False
                else:
                    return False

        return not stack