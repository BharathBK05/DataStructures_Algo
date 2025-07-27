class Bubble:
    def Bsort(self,values):
        size = len(values)

        for i in range(size-1):
            for j in range(i, size-i-1):
                if values[j] > values[j+1]:
                    values[j], values[j+1] = values[j+1],values[j] 

        print(values)     

if __name__ == '__main__':
    try:
        s = Bubble()
        value = str(input())
        value = value.split(',')
        s.Bsort(value)

    except Exception as e:
        print(e)    