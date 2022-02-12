class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        d = {}

        for i in range(97, 123):
            d[i] = morse[i-97]

        def morser(word):
            l = []
            for alphabet in word:
                l.append(d[ord(alphabet)])
            return ''.join(l)

        l = set()
        for word in words:
            l.add(morser(word))

        return len(l)
        