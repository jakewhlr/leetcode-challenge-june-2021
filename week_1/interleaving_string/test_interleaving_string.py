import unittest
from interleaving_string import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_s1_true(self):
        s1 = ""
        s2 = "world"
        s3 = "world"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)

    def test_empty_s2_true(self):
        s1 = "hello"
        s2 = ""
        s3 = "hello"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)

    def test_empty_s3_true(self):
        s1 = ""
        s2 = ""
        s3 = ""
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)

    def test_empty_s1_false(self):
        s1 = ""
        s2 = "world"
        s3 = "hello"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), False)

    def test_empty_s2_false(self):
        s1 = "hello"
        s2 = ""
        s3 = "world"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), False)

    def test_empty_s3_false(self):
        s1 = ""
        s2 = ""
        s3 = "a"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), False)

    def test_substring(self):
        s1 = "hello"
        s2 = "world"
        s3 = "helloworld"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)

    def test_longstring(self):
        s1 = "hello"
        s2 = "world"
        s3 = "hihellwoorld"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), False)

    def test_case_01(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)

    def test_case_01_flipped(self):
        s1 = "dbbca"
        s2 = "aabcc"
        s3 = "aadbbcbcac"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)

    def test_case_02(self):
        s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
        s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
        s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
        self.assertEqual(self.solution.isInterleave(s1, s2, s3), True)
