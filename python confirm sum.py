class Solution:
    
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def cross(nums: List[int], value):
            for num in nums:
                if value == num:
                    return True
        
        
        new_list = []
        for first_num in nums:
            for second_num in nums:
                if first_num + second_num == target:
                    new_list.append(nums.index(first_num))
                    if cross(new_list, second_num) == True:
                        new_list.append(nums.index(second_num))
                        
        return new_list
        
    
            
            
    