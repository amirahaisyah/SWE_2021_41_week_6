from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_indices = {}
    for i, num in enumerate(nums):
        complemet=nt = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return[]
