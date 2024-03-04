class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 转化成字符型
        x=str(x)
        x=list(x)
        print(x)
        #将x取逆向保存至y中
        y=x[::-1]
        print(y)
        #判断x与y是否相等
        if x==y:
            return True
        else:
            return False
if __name__ == "__main__":
    x = Solution().isPalindrome(111)
    print(x)