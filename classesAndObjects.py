class Employee:
    def __init__(self, empid=None, name=None, salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary

    def setEmpid(self, empid):
        self.empid = empid

    def setName(self, name):
        self.name = name

    def setSalary(self, salary):
        self.salary = salary

    def getEmpid(self):
        return self.empid

    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary


e1 = Employee()
e2 = Employee(1, "rahul", 40000)
e1.setEmpid(2)
e1.setName("romes")
e1.setSalary(303030)
print(e1.getEmpid(), e1.getName(), e1.getSalary())
print(e2.getEmpid(), e2.getName(), e2.getSalary())


# class Test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def show(self):
#         print(self.a, self.b)
#     @staticmethod
#     def ff2():
#         pass
#     @classmethod
#     def ff3(cls):
#         pass

# t1= Test(3,4)
# t2= Test(2,3)
# print(t1.a, t1.b)
# print(t2.a, t2.b)
