#1
def twoSum(nums,target:int):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j] == target and i != j:
                return [i,j]


#2
def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()
    l3 = [str(i) for i in l1]
    l4 = [str(i) for i in l2]
    s1 = "".join(l3)
    n1 = int(s1)
    s2 = "".join(l4)
    n2 = int(s2)
    s = n1+n2
    final = []
    for e in str(s):
        final.append(e)
    final.reverse()
    return final

#3
def lengthOfLongestSubstring(s: str):
    n = len(s)
    res = 0
    for i in range(n):
        visited = [0] * 256
        for j in range(i, n):
            if (visited[ord(s[j])] == True):
                break
            else:
                res = max(res, j - i + 1)
                visited[ord(s[j])] = True
        visited[ord(s[i])] = False
    return res

def f(x):
    return 100
