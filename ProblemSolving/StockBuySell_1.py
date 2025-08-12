class Solution(object):
    def __init__(self):
        prices = [3, 2, 6, 5, 0, 3]
        self.profit = self.max_area(prices)

    def max_area(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, (price - min_price))

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    print("Max area:", solution.profit)
