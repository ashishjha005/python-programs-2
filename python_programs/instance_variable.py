class students:
    def __init__(self,roll_no,name,branch,sem):
       self.roll_no=roll
       self.name=name
       self.branch=branch
       self.sem=sem
    
print("enter 1st student detail ")
name=input("name of student")
roll=int(input("roll no."))
sem=int(input("sem"))
branch=input("enter branch")
s=students(roll,name,branch,sem)
print(s.__dict__)
