nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

op = []

final = m + n 



for i in range(m):
    op.append(nums1[i])

for i in range(n):
    op.append(nums2[i])

op.sort()

print(op)