nums = [3,2,4]
target = 6


def sum(nums:list, target:int):
    for i, x in enumerate(nums):
        temp = target - x
        print('i', i, 'temp',temp)
        if nums.index(temp, i+1) == True:
            print(nums.index(temp, i+1))
            return [i, nums.index(temp, i+1)]
        elif ValueError:
            continue
# print(sum(nums, target))

map = dict()

for i in range(len(nums)):
    map[nums[i]] = i

    temp = target - nums[i]
    if temp in map:
        print([map[temp], i])

# s = 'LVIII'

# def romanToInt(s: str) -> int:
#         revS = s[::-1]
#         rome = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
        
#         result = 0
        
#         for a, x in enumerate(revS):
#             # print(rome[revS[a]], type(rome[x]))
#             if rome[x+1] < rome[x]:
#                 print('dasda')
            

# romanToInt(s)