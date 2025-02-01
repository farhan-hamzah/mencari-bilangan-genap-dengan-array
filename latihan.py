nums = list(map(int, input("Masukan Array :").split()))
d = 0
for i, num in enumerate(nums):
    if nums[i]%2 == 0:
        d += 1
    else:
        d += 0
print(d)