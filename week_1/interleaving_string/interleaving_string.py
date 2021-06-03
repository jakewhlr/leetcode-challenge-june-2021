class Solution:

    def isInterleaveHelper(self, s1: str, s2: str, s3: str, current: str) -> bool:
        print(len(s1), len(s2), len(s3))
        if current == s3:
            return True
        s1_res = s2_res = False
        if s1:
            s1_res = self.isInterleaveHelper(s1[1:], s2, s3, s1[0] + current)
        if s2:
            s2_res = self.isInterleaveHelper(s1, s2[1:], s3, s2[0] + current)
        return s1_res or s2_res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleaveHelper(s1, s2, s3, '')
