try:
   x=int(input())
   t=x//2
   for i in range(1,5):
    for j in range(1,x+1):
        if t+1 ==i+j or j-i==t-1:
            print("*",end=' ')
            if i+j>=t+1 and j-1<t-1:
                print("*",end=' ')
            
        else:
            print(' ',end=' ')
        
    print()
except:
    pass
        
