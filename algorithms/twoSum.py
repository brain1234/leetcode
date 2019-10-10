class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_dict = {}
        for inx, value in enumerate(nums):
            if(int_dict.__contains__(target-value)):
                return [inx, int_dict.get(target-value)]
            else:
                int_dict[value]=inx


