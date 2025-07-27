a = [5,10,77,21,67,90,32,66,14,100,3]

if a:
    maximum = a[0]
    minimum = a[0]

    for i in a:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i

print(maximum)
print(minimum)

#Time complexity --> O(n)