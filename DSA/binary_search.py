class BinarySearch:
    def Bsearch(self,arr, max,low, x):
        if max>=low:
            mid = (max+low) //2

            if arr[mid] == x:
                return mid

            elif arr[mid] < x:
                return self.Bsearch(arr, max, mid+1, x)    

            elif arr[mid] > x:
                return self.Bsearch(arr, mid-1, low, x)  
        else:
            return -1 

if __name__ == '__main__':
    try:
        s = BinarySearch()
        arr = [1,4,6,9,2]
        arr.sort()
        x = 2
        res = s.Bsearch(arr,len(arr)-1,0, x)
        if res:
            print(res)

    except Exception as e:
        print(e)        