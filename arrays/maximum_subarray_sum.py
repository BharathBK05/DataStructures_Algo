a = [1,3,6,-2,4,5,1,4,5,7,-80,2]


max_so_far = a[0]
max_ending_here = a[0]

for i in range(1, len(a)):
    a1 = a[i]
    b1 = max_ending_here + a[i]
    max_ending_here = max(a[i], max_ending_here + a[i])
    max_so_far = max(max_so_far, max_ending_here)

print(max_so_far)