class Solution:
    def isValid(self, s: str) -> bool:
        dictio = {')': '(', '}': '{', ']': '['}
        ouvrante = ['(','{','[']
        fermante = [')','}',']']
        valid = True
        stack = []
        for element in s:
            if element in ouvrante:
                stack.append(element)
            if element in fermante:
                if not stack:
                    valid = False
                    break
                elif stack.pop() == dictio[element]:
                     continue
                else:
                    valid = False
                    break
        return  (valid and not stack)