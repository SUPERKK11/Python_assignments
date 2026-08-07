class Solution:
    def solve(self,arr:list[int],k:int)->list[int]:
        s=set() ### {}
        for i in range(len(arr)):
            if arr[i] in s:
                return "Yes" 
            s.add(arr[i])
            if i >= k:
                s.remove(arr[i-k])
        return "No"
            
if __name__ == "__main__":
    k=int(input())
    arr=list(map(int,input().strip().split()))
    sol=Solution()
    print(sol.solve(arr,k))