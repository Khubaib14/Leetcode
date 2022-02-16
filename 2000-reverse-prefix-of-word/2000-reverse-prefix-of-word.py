class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list = list(word)
        ind = 0
        for i in range(len(word_list)):
            if word_list[i] == ch:
                ind = i
                break
        j = 0
        for i in range(len(word_list[:ind+1])//2):
            j = (len(word_list[:ind+1])) - 1 - i
            word_list[i], word_list[j] = word_list[j], word_list[i]

        return "".join(word_list)    
