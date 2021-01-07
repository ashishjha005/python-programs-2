def solve(A, B):
        l=0
        h=len(A)-1 
        c=0
        while l<=h:
            mid=l+(h-l)//2
            if A[mid-1]<A[mid]<A[mid+1]:
                    c=mid
                    break
            elif A[mid]>=A[l]:
                
                l=mid+1   
            else:
                h=mid-1
        l=0
        h=c
        while l<=h:
            mid=(l+h)//2
            if A[mid]==B:
                return mid 
            elif A[mid]>=B:
                h=mid-1 
            else:
                l=mid+1
        l=c+1 
        h=len(A)-1 
        while l<=h:
            mid=(l+h)//2
            if A[mid]==B:
                return mid 
            elif A[mid]>=B:
                l=mid+1
            else:
                h=mid-1
        return -1
A= [ 1, 2, 3, 4, 5, 10, 9, 8, 7, 6 ]
B=5
print(solve(A,B))
