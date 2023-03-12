




nums = [0,0,1,1,1,2,2,3,3,4]
print(nums)



for i in range(0, len(nums)):

    if nums[i - 1] == nums[i]:
        print(nums[i - 1], '==', nums[i])

        for index in range(i + 1, len(nums)):
            nums[index - 1] = nums[index]
            nums[-1:] = '_'

    print('----')

    print(nums)


        # break

