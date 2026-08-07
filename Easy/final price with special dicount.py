class Solution(object):
    def finalPrices(self, prices):
        d = []
        for i in range(len(prices)):
            found = False
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    d.append(prices[i] - prices[j])
                    found = True
                    break
            if not found:
                d.append(prices[i])
        return d

        