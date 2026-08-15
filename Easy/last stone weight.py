class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0
        