class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def make_table(s):
            table = dict()
            for i in s:
                if i in table:
                    table[i] += 1
                else:
                    table[i] = 1
            return table

        table1 = make_table(s)
        table2 = make_table(t)

        def test(table1, table2):
            if len(table1) == len(table2):
                for i in table1.items():
                    if i[0] not in table2: 
                        return False
                    elif i[1] != table2[i[0]]:
                        return False
                    else:
                        pass
                return True
            else:
                return False

        
        return test(table1, table2)