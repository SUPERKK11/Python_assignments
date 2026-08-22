class Solution:
    def Sol(self,arr:list[int])->int:
        res=0
        for num in arr:
            res=res^num
        if res==0:
            return -1
        return res
if __name__ =="__main__":
    arr=list(map(int,input().strip().split(",")))
    Sol=Solution()
    print(Sol.Sol(arr))