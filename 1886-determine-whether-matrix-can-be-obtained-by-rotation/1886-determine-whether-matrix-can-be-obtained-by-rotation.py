class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
         rotated_mat90 = [list(reversed(col)) for col in zip(*mat)]
         rotated_mat180 = [list(reversed(col)) for col in zip(*rotated_mat90)]
         rotated_mat270 = [list(reversed(col)) for col in zip(*rotated_mat180)]
         
         if target ==mat or target ==rotated_mat90 or target ==rotated_mat180 or target ==rotated_mat270:
            return True
         return False