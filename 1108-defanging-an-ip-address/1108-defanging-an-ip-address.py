class Solution:
    def defangIPaddr(self, address: str) -> str:
        x = []
        for i in address:
            if i != '.':
                x.append(i)
            elif i == '.':
                x.append("[.]")
        return "".join(x)