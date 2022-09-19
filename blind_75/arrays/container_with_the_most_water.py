from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            max_height = min(height[right], height[left])
            container_length = right - left
            water_vol = max_height * container_length

            if water_vol > max_water:
                max_water = water_vol

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]

sol = Solution()

print(sol.maxArea(h1))
