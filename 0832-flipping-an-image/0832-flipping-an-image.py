class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image= [row[::-1] for row in image]
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] ^= 1
        return image
        