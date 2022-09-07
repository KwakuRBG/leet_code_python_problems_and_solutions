"""

**1. Two Sum**

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

_____

Example 1:

- Input: nums = [2,7,11,15], target = 9
- Output: [0,1]
- Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

- Input: nums = [3,2,4], target = 6
- Output: [1,2]

Example 3:

- Input: nums = [3,3], target = 6
- Output: [0,1]

Constraints:

- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists.

"""

from itertools import combinations


def two_sum(nums: list[int], target: int) -> list[int]:
    lookup_table = {num: i for i, num in enumerate(nums)}
    for i in range(len(nums)):
        other = target - nums[i]
        if other in lookup_table and i != (result := lookup_table[other]):
            return [i, result]


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
assert two_sum([3, 2, 3], 6) == [0, 2]
