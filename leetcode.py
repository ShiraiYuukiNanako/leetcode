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



