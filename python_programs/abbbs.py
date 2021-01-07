try:
   l=list(map(int,input().split()))
   n1=l[0]
   n2=l[1]
   l2=[]
   l3=[]
   prime=[True for i in range(n2+1)]
   for p in range(2,n2+1):
       if prime[p-1]==True:
           for j in range(p*p,n2+1,p):
            prime[j-1]=False
   for p in range(n1,n2+1):
           if prime[p-1]:
               if p>=n1:
                   l2.append(p)
   
   
   for i in range(len(l2)):
      if i>0:
       for j in range(0,i):
         l22=int(str(l2[i]) + str(l2[j]))
         for t in range(2,l22):
            if l22%t==0:
               break
         else:
            if l22 not in l3:
              l3.append(l22)
      if i < len(l2)-1:            
       for j in range(i+1,len(l2)):
         l22=int(str(l2[i]) + str(l2[j]))
         for t in range(2,l22):
            if l22%t==0:
               break
         else:
            if l22 not in l3:
              l3.append(l22)
   a=l3[0]
   b=l3[len(l3)-1]
   for i in range(len(l3)-2):
      c=a+b
      a=b
      b=c
      if i==len(l3)-3:
         print(c)
except:
   pass
