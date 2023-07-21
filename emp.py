d = dict()
class employee():
 def insert(self):
  self.empid=int(input("Enter your Employee ID: "))
  if self.empid in d:
     self.duplicate()
     return None
  self.name=input("Enter employee name: ")
  self.address=input("Enter address: ")
  self.pan=int(input("Enter PAN: "))
  self.basic=int(input("Enter Basic pay: "))
  self.TDS=int(input("Enter TDS: "))
  self.deduct=int(input("Enter Deductions: "))
  self.hra=1.25*self.basic
  self.da=0.25*self.basic
  self.gross_salary=self.basic+self.hra+self.da
  self.net_pay=self.gross_salary-self.deduct
  self.update()

 def duplicate(self):
  print ("Duplicate Entry \nEnter Unique Employee ID \n")
  self.insert()

 def update(self):
  d.update({self.empid: {
   "Name": self.name,
   "Address": self.address,
   "PAN": self.pan,
   "Basic Pay": self.basic,
   "TDS": self.TDS,
   "Deductions": self.deduct,
   "HRA": self.hra,
   "DA": self.da,
   "Gross Salary": self.gross_salary,
   "Net Pay": self.net_pay
  }})
  print ("Employee details updated \n")

 def printemp(self):
  for i in d:
   print ("Employee ID: ", i)
   for j in d[i]:
    print (j, ": ", d[i][j])
   print ()

 def search(self, empid):
   flag=0
   for key in d:
    if key==empid:
      print ("Employee details found \n")
      for i in d[key]:
        print (i, ": ", d[key][i])
        flag=1
      print ()
   if flag==0:
    print ("Employee details not found \n")

class employees(employee):
 emp=employee()
 while True:
  print("*"*10, "Employee Management System", "*"*10)
  print ("1. Enter employee details \n2. Print employee details \n3. Search employee \n4. Exit")
  ch=int(input("Enter your choice: "))
  if ch==1:
   emp.insert()
  elif ch==2:
   emp.printemp()
  elif ch==3:
   empid=int(input("Enter employee id: "))
   emp.search(empid)
  elif ch==4:
   break
