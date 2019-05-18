import sys
class Solution:
    # 方法1:拿第一个字符串和后面字符串依次做对比,找到共同最长的前缀
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 如何输入字符串list为空,返回空
        if len(strs) == 0:
            return ''
        # 取出第一个字符串,作为对比
        prefix = strs[0]
        # 用后面的字符串依次和它对比,并取出共同的前缀。直到最后一个字符串对比完,那么都是大家共同的前缀。
        for i in range(1,len(strs)):
            while strs[i].find(prefix) != 0:  # 如果prefix不是strs[i]的前缀,即find结果不是0
                prefix = prefix[0:len(prefix)-1] # 那么继续把prefix减少最后一位
                if prefix == '':  #直到prefix为空,那么返回空。否则跳出while,返回一个有值的prefix
                    return ''
        return prefix

    # 方法2:这个方法是把竖向比较,把第一个字符串字符拿出来,然后挨个去拿后面的字符串,从头到尾去对比
    def longestCommonPrefix2(self, strs):
        # 如果输入为空,返回空
        if len(strs) == 0 or strs == None:
            return ''
        # 以第一个字符串长度来循环
        for i in range(len(strs[0])):
            c = strs[0][i] # 先取出第一个字符串的位
            for j in range(1,len(strs)):  # 和后面的字符串对比
                # 如果 i 等于这时候 j 字符串的长度,说明j到头,或者他们头部不相同
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i] # 返回对比好相同的那部分。

        return strs[0]

    # 方法3:
    def longestCommonPrefix3(self,strs):
        if strs == None or len(strs) == 0:
            return ''
        return self.__longestCommonPrefix3(strs, 0 ,len(strs) - 1)

    def __longestCommonPrefix3(self,strs,l,r):
        if l == r:
            return strs[l]
        else:
            mid = int((l + r)/2)
            lcpLeft = self.__longestCommonPrefix3(strs, l, mid)
            lcpRight = self.__longestCommonPrefix3(strs, mid+1, r)
            return self.__commomPrefix(lcpLeft,lcpRight)

    def __commomPrefix(self,left, right):
        min_len = min(len(left),len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[0:i]
        return left[0:min_len]

    def longestCommonPrefix4(self,strs):
        if strs == None or len(strs) == 0:
            return ''
        minLen = sys.maxsize
        for str in strs:
            minLen = min(minLen,len(str))
        low = 1
        high = minLen
        while low <= high:
            middle = int((low + high)/2)

            if self.__isCommonPrefix(strs,middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][0:int((low+high)/2)]

    def __isCommonPrefix(self,strs,len_str):
        str1 = strs[0][0:len_str]
        for i in range(len(strs)):
            if strs[i].find(str1) != 0:
                return False
        return True


s = Solution()
list1 = ["flower","flow","flight"]
list2 = ["dog","racecar","car"]
list3 = ["c","acc","ccc"]
list4 = []
print("The 1st method:")
print(s.longestCommonPrefix(list1))
print(s.longestCommonPrefix(list2))
print(s.longestCommonPrefix(list3))

print("The 2nd method:")
print(s.longestCommonPrefix2(list1))
print(s.longestCommonPrefix2(list2))
print(s.longestCommonPrefix2(list3))
print(s.longestCommonPrefix2(list4))
print("The 3rd method:")
print(s.longestCommonPrefix3(list1))
print(s.longestCommonPrefix3(list2))
print(s.longestCommonPrefix3(list3))

print("The 4rd method:")
print(s.longestCommonPrefix4(list1))
print(s.longestCommonPrefix4(list2))
print(s.longestCommonPrefix4(list3))
print(s.longestCommonPrefix4(list4))