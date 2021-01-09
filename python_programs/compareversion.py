def compareVersion( A, B):
       l=A.split('.')
       l2=B.split('.')
       n=len(l)
       m=len(l2)
       print(l,l2)
       if n<m:
        for i in range(n):
               if int(l[i])<int(l2[i]):
                   return -1
               elif int(l[i])>int(l2[i]):
                   return 1 
        else:
                   for j in range(i+1,m):
                           if int(l2[j])>0:
                               return -1
                   return 0 
       elif n==m:
           for i in range(m):
               if int(l[i])>int(l2[i]):
                  
                   return 1 
               elif int(l[i])<int(l2[i]):
                   return -1 
               else:
                   pass
           return 0
       else:
         for i in range(m):
               if int(l[i])<int(l2[i]):
                   return -1
               elif int(l[i])>int(l2[i]):
                   return 1 
         else:
                       for j in range(i+1,n):
                           if int(l[j])>0:
                               return 1
                       
                       return 0
A='8.8888888888888888888888888888'
B='8.888888888'
print(compareVersion(A, B))
