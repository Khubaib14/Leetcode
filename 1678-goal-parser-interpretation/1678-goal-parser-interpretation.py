class Solution:
    def interpret(self, command: str) -> str:
        i,l = 0,[]
        while i < len(command):
            if command[i] == "(" or command[i] == "G":
                if command[i] == "G":
                    l.append("G")
                else:
                    if command[i+1] == ")":
                        l.append("o")
                    else:
                        l.append("al")
            i += 1

        return "".join(l)