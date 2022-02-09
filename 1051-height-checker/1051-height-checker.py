class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # initiate an empty list and dict 
        expected = [0] * (len(heights))
        count_dict = dict()

        # populate the dict
        for height in heights:
            if height in count_dict:
                count_dict[height] += 1
            else:
                count_dict[height] = 1

        # arrange the dict by its value
        # [[# of occurence, num]]
        x = [[k,v] for k,v in sorted(count_dict.items())]
        print(x)

        # create the list called "expected"
        c = 0
        for i in x:
            for j in range(i[1]):
                expected[c] = i[0]
                c += 1

        return sum([1 for i,j in zip(heights, expected) if i!= j])