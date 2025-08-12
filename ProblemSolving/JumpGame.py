class Solution(object):
    def __init__(self):
        arr = [1, 2, 3, 4, 5]
        self.is_possible = self.jump_game(arr)

    def jump_game(self, arr):
        max_reach = 0
        for i in range(len(arr)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + arr[i])

        return True

if __name__ == "__main__":
    solution = Solution()
    print("Reaching is possible :", solution.profit)
