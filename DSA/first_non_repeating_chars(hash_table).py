NO_OF_CHARS = 256

class hashtable():

    def getCharCountArray(self,string):
        #create hash table and increment values based on its ascii value
        count = [0] * NO_OF_CHARS
        for i in string:
            count[ord(i)] += 1

        return count
    
    def findChar(self,string,char):
        # find the char using hash table
        count = self.getCharCountArray(string)
        value = ord(char)
        if count[value] != 0:
            print("Value found")
        else:
            print("Not found")    

    
    
    def firstNonRepeating(self,string):
        count = self.getCharCountArray(string)
        index = -1
        k = 0

        #hash table with values 1 are non repeating and >1 are repeating
        for i in string:
            if count[ord(i)] == 1:
                index = k
                break
            k += 1
    
        return index
 
 
if __name__ == '__main__':
    string = "bharathkumar"
    o = hashtable()
    o.findChar(string,'b')
    index = o.firstNonRepeating(string)
    if index == -1:
        print("Either all characters are repeating or string is empty")
    else:
        print("First non-repeating character is", string[index])