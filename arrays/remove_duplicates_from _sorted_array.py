a = [1,2,2,3,4,5,5,6,7,7,8,9,10,10]

out = []
siz = len(a)
prev = a[siz-1]
for count,i in enumerate(a):
    if count != siz-1:
        if i != a[count+1]:
            if i != prev:
                prev = i
                out.append(i)
    else:
        if i != prev:
           out.append(i) 

print(out)

#Time complexity --> O(n)


