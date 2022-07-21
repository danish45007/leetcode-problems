class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            img.reverse()
            for c in range(len(img)):
                img[c] = int(not img[c])
        return image