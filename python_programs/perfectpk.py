def largestNumber( A):
         l=[]
         for i in range(len(A)):
             l.append(list(str(A[i]))) 
         l.sort(key=lambda x : x[0])
         print(l)
A=[3, 30, 34, 5, 9]
print(largestNumber(A))
