class Solution:
    def StringToList(self, sentence):
        prev = -1
        result = []
        for i in range(len(sentence)):
            if sentence[i] == " ":
                result.append(sentence[prev+1:i])
                prev = i
        result.append(sentence[prev+1:])
        return result
    
    def GoatGrammar(self, arr):
        result = []
        cnt = 1
        for i in arr:
            if i[0] in "aeiouAEIOU":
                i += "ma"
            else:
                temp = i[0]
                i = i[1:] + temp + "ma"
            i += "a"*cnt
            cnt += 1
            result.append(i)
        return " ".join(result)
    
    
    def toGoatLatin(self, sentence: str) -> str:
        arr = self.StringToList(sentence)
        return self.GoatGrammar(arr)