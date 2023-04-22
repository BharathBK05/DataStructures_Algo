class Armstrong:
    def find(self,num):
        result = 0
        original = num
        digits = []
        if num > 9:
            while num:
                val = num % 10
                digits.append(val)
                num = num // 10

            size = len(digits)
            for i in digits:
                result = result + pow(i,size)
            if result == original:
                print('Armstrong number')  
            else:
                print('Not Armstrong')    

if __name__ == '__main__':
    try:
        s = Armstrong()
        value = int(input())
        s.find(value)

    except Exception as e:
        print(e)    