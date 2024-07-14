class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        for n in nums:
            target = n
            l = 0
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + target == 0:
                    result.append([nums[l], nums[r], target])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] + target:
                    l += 1
                else:
                    r -= 1

        return result


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    # [[-1,-1,2],[-1,0,1]]
