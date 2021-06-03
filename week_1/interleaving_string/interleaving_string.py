class Solution:
    def isInterleaveHelper(self, s1: str, s2: str, s3: str, current: str) -> bool:
        if current == s3 and not s2 and not s1:
            return True
        s1_res = s2_res = False
        if s1:
            if s1[0] == s3[len(current)]:
                s1_res = self.isInterleaveHelper(s1[1:], s2, s3, current + s1[0])
        if s2:
            if s2[0] == s3[len(current)]:
                s2_res = self.isInterleaveHelper(s1, s2[1:], s3, current + s2[0])
        return s1_res or s2_res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.isInterleaveHelper(s1, s2, s3, '')
