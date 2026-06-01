class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        num_set = set(nums)
        max_count = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1
                if count > max_count:
                    max_count = count
        return max_count