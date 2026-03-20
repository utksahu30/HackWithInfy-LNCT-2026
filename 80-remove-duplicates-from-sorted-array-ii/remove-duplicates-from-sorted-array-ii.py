class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 0
        count = 0
        
        for current_num in nums:
            if write_index == 0 or current_num != nums[write_index - 1]:
                count = 1
                nums[write_index] = current_num
                write_index += 1
            elif count < 2:
                count += 1
                nums[write_index] = current_num
                write_index += 1
        
        return write_index