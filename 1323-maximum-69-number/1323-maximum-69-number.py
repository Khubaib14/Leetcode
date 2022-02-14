class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = num
        index = 0
        leftmost = -1

        while temp > 0:
            if temp % 10 == 6:
                leftmost = index 
            temp = temp // 10
            index += 1

        if leftmost > -1:
            x = num + (3 * (10**leftmost))
            return x
        else:
            return num
           
             
    def usesString(num):
        l = list(str(num))

        for i in range(len(l)):
            if l[i] == '6':
                l[i] = '9'
                break

        return "".join(l)
