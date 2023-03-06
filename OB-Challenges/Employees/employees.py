class Employees:
    def __init__(self, firstname, lastname, employeeid):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__fullname = firstname + ' ' + lastname
        self.__email = firstname.lower() + '.' + lastname.lower() + '@company.com'
        self.__employeeid = employeeid
        
    def GetEmployeeEmail(self, employeeid):
        if self.__employeeid == employeeid:
            return self.__email
        
    def PrintDetails(self, employeeid):
        if self.__employeeid == employeeid:
            return 'First Name: ' + self.__firstname + '\nLast Name: ' + self.__lastname + '\nFull Name: ' + self.__fullname +'\nEmail: ' + self.__email + '\nEmployee ID: ' + str(self.__employeeid)
        
employee_list = []
import os
try:
    with open('emailList.txt','r') as f:
        num_lines = len(f.readlines())
        f.seek(0)
        for i in range(num_lines//2):
            first_name = f.readline().strip()
            last_name = f.readline().strip()
            employee_id = i+1
            employee_list.append(Employees(first_name,last_name,employee_id))
            
except IOError:
    print("Sorry, file not found. Directory:",os.getcwd())
        
        
for i in employee_list:
    if i.PrintDetails(2) != None:
        print(i.PrintDetails(2))
    
"""
OUTPUT:
First Name: Abra
Last Name: Bacon
Full Name: Abra Bacon
Email: abra.bacon@company.com
Employee ID: 2
"""
