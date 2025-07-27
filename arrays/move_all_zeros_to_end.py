a = [1,0,3,2,0,5,0,2,0,9,9,3,0]


#------------------------Method 1---------------------------------->
non_zero_index = 0

#move all non zeo to front and note down the index number
for i in a:
    if i != 0:
        a[non_zero_index] = i
        non_zero_index += 1

#replce all the remaining values after non zero index as zero
for i in range(non_zero_index,len(a)):
    a[i] = 0

#Time complexity --> O(n)
#Space complexity --> O(1)


#------------------------Method 2---------------------------------->
val = []
zero = []

for i in a:
    if i != 0:
        val.append(i)
    else:
        zero.append(0)

print(val+zero)

#Time complexity --> O(n)
#Space complexity --> O(n)