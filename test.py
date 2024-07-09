def twoSum(nums: list, target: int):
        for i, x in enumerate(nums):
            temp = target - x
            try:
                q = nums.index(temp, i+1)
                if type(q) == int:
                    print([i, nums.index(temp, i+1)])
                    # return [i, nums.index(temp, i+1)]
                else:
                    break
            except:
                 print('except')

twoSum(nums=[3,2,4], target=6)