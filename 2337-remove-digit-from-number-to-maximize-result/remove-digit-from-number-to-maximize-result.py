class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        ind=-1
        for i in range(0,len(number)):
            if number[i]==digit:
                if i+1<len(number) and int(number[i+1])>int(number[i]):
                    return number[:i]+number[i+1:]
                else:
                    index=i
        return number[:index]+number[index+1:]

