# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
#
# Example 2:
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
#
# Example 3:
#
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.


from typing import List


class Solution:
    def longestSubarrayBruteForce(self, nums: List[int]) -> int:
        global_max = 0

        for i in range(len(nums)):
            local_max = 0
            deleted_one = False
            for j in range(i, len(nums)):
                if nums[j] == 1:
                    local_max += 1
                elif nums[j] == 0 and not deleted_one:
                    deleted_one = True
                else:
                    break

            if not deleted_one:
                local_max -= 1
            global_max = max(global_max, local_max)

        return global_max

    def longestSubarray(self, nums: List[int]) -> int:
        global_max = 0
        curr_max = 0
        length = len(nums)

        removed_one = False

        if sum(nums) == 0:
            return 0

        if sum(nums) == length:
            return length - 1

        for n in nums:
            if n == 0 and not removed_one:
                removed_one = True
            elif n==1:
                curr_max+=1
                removed_one=False
            else:
                curr_max-=1
                removed_one = False



        # for n in nums:
        #     if n == 1:
        #         curr_max += 1
        #     elif n == 0 and not removed_one:
        #         removed_one = True
        #     else:
        #         removed_one = False
        #         curr_max -= 1

        global_max = max(global_max, curr_max)

        return global_max


print(Solution().longestSubarray([1]))  # 0
print(Solution().longestSubarray([1, 1]))  # 1
print(Solution().longestSubarray([1, 1, 0, 1]))  # 3
print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
print(Solution().longestSubarray([1,1,0,0,1,1,1,0,1]))  # 4
