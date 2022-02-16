class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            j = 0
            while j != len(image[i]) -1 - j and j < len(image[i])//2:
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
                if image[i][len(image[i]) -1 - j] == 0:
                    image[i][len(image[i]) -1 - j] = 1
                else:
                    image[i][len(image[i]) -1 - j] = 0
                image[i][j], image[i][len(image[i]) -1 - j] = image[i][len(image[i]) -1 - j], image[i][j]
                j += 1

            if len(image) % 2 != 0:
                if image[i][(len(image)//2)] == 0:
                    image[i][(len(image)//2)] = 1
                else:
                    image[i][(len(image)//2)] = 0
        return image
        