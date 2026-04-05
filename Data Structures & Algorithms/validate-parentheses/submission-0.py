class Solution:
    def helper(self, element, top):
        if element == ')' and top == '(':
            return True
        elif element == ']' and top == '[':
            return True
        elif element == '}' and top == '{':
            return True
        return False
        
        
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ')}]':
                if not stack:
                    return False
                top = stack.pop()
                if not self.helper(char, top):
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
                