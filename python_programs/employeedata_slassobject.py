class employee:
    def __init__(self,a,b,c):
        self.empid=a
        self.name=b
        self.salary=c
    def f1(self):
        print("The employee data is :")
    def f2(self):
        print("the sorted by salary in descending order :")
        
    def f3(self):
        print("the sorted names in ascending order")
       
       
        
x=int(input("enter the number of employes"))
l=[]
l2=[]
l3=[]
for i in range (x):
    print("enter the employ detail ",i+1)
    e=int(input("enter empid"))
    n=input("enter name")
    s=int(input("enter salary"))
    em=employee(e,n,s)
    l.append(em)
for i in l:
 i.f1()
 print(i.__dict__)

em.f2()
em.salary=em
l.sort()
for i in l:
 i.f1()
 print(i.__dict__)
 
em.f3()
print(l3.sort())
