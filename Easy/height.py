class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        c = [0] * 101
        for h in heights:
            c[h] += 1

        expected = []
        for h in range(1, 101):
            ca = c[h]
            for _ in range(ca):
                expected.append(h)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1

        return res