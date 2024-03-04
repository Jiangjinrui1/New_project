class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        #将dic映射至s
        # print(dic)
        # print(s)
        s=list(s)
        # print(s)
        for i in range(len(s)):
            s[i]=dic[s[i]]
        # 计算求和结果
        sum=0
        for i in range(len(s)):
            sum+=s[i]
        return sum

if __name__=="__main__":
    solution=Solution().romanToInt("LVIII")
    print(solution)