def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for index, ele in enumerate(nums):
            if target- ele in dict:
                return dict[target- ele], index
            dict[ele]= index

nums=[1,2,2,6,4]
twoSum(nums,7,7)