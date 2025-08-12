class Solution(object):
    def __init__(self):
        heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
        self.area = self.max_area(heights)

    def max_area(self, heights):
        left = 0
        right = len(heights) - 1
        current_max = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height
            current_max = max(current_area, current_max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return current_max

if __name__ == "__main__":
    solution = Solution()
    print("Max area:", solution.area)
