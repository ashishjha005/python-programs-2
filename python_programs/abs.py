def ex(n):
  x=list(map(int,input("enter coins").split()))
  count=0
  for i in set(x):
      for j in x:
          if i==j:
              count+=1
      if count%2!=0:
          print(i)
      count=0
          
     
  return
ex(8)
           
