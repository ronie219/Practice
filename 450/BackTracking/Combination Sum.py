class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    
    
    def combinationalSum(self,A, B):
        answer = []
        
        def _solve(A, B, parent = -1, ans= [], curr=0):
            if curr == B:
                answer.append(tuple(ans))
            if curr > B:
                return
            for idx in range(len(A)):
                if A[idx] >= parent :
                    _solve(A,B,A[idx], ans + [A[idx]], curr + A[idx])
                
        
        _solve(A,B)
        return sorted(answer)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()