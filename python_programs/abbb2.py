try:
   l=list(map(int,input().split()))
   n1=l[0]
   n2=l[1]
   l2=[]
   s=set()
   l4=[]
   prime=[True for i in range(n2+1)]
   for p in range(2,n2+1):
      if prime[p-1]==True:
         for j in range(p*p,n2+1,p):
            prime[j-1]=False
   for i in range(n1,n2+1):
     if prime[i-1]:
      l2.append(i)
   
   for i in range(len(l2)):
       for j in range(len(l2)):
         if l2[i]==l2[j]:
            continue
         else:
          l22=int(str(l2[i]) + str(l2[j]))
          s.add(l22)
         
          l23=int(str(l2[j]) + str(l2[i]))
          s.add(l23)
   l3=list(s)
   print(l3)
   prime=[True for i in range(max(l3)+1)]
   for p in range(2,max(l3)+1):
      if prime[p-1]==True:
         for j in range(p*p,max(l3)+1,p):
            prime[j-1]=False
   for i in l3:
      if prime[i-1]:
         l4.append(i)
   
   
except:
   pass
