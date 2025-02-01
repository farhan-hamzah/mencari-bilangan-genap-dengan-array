nums = list(map(int, input("Masukan Array :").split()))
for i, num in enumerate(nums):
    if nums[i]%2 == 0:
        print(nums[i])
