class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) and len(s2) == 0:
            return False
        if len(s3) == 0:
            return F
        split1 = list(s1)
        split2 = list(s2)
        for i in range(len(s3) - 1, 0, -1):
            if len(split1) > 0 and s3[i] == split1[-1]:
                split1.pop()
                continue
            if len(split2) > 0 and s3[i] == split2[-1]:
                split2.pop()
                continue
            return False
        return True


sol = Solution()
print(sol.isInterleave("hello", "world", "heworllldo"))
