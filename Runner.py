from colored import fg, bg, attr
import ClassDemo
import Colors
import sys
import time

class Runner:
    def employeeOpration(self,portal_obj):
        loop = False
        print ('''Employee Details:
        1) Create Employee
        2) Update Employee
        3) Get Employee by Id
        4) Print All Employee
        5) Delete Employee
        6) Exit the program
        ''')
        color_obj = Colors.Color()
        while loop == False:
            option = input('Please Select any option : ')
            if option.isdigit():
                op = int(option)
                if op == 1: 
                    print ("\nYou select option",option,", Now Process for creating new employee details")
                    time.sleep(2)
                    portal_obj.createEmployeeDetails()
                    time.sleep(2)
                    print ('%sEmployee details created successfully'%color_obj.setColor('green'))
                    time.sleep(2)
                    print ('')
                    print ('%sNow choose any option for another process'%color_obj.setColor('white'))
                    time.sleep(2)
                    self.employeeOpration(portal_obj)
                elif op == 2:
                    print ("\nYou select option",option,", Now Process for updating existing employee details")
                    time.sleep(2)
                    portal_obj.updateEmployeeDetails()
                    self.employeeOpration(portal_obj)
                elif op == 3:
                    print ("\nYou select option",option,", Now Process for getting existing employee details based on employeeId")
                    time.sleep(2)
                    portal_obj.getEmployeeDetailsById()
                    print ('\n%sNow choose any option for another process'%color_obj.setColor('white'))
                    self.employeeOpration(portal_obj)
                elif op == 4:
                    print ("\nYou select option",option,", Now Process for getting all employee with details")
                    time.sleep(2)
                    portal_obj.printAllEmployee(portal_obj.database)
                    print ('\n%sNow choose any option for another process'%color_obj.setColor('white'))
                    self.employeeOpration(portal_obj)
                elif op == 5:
                    print ("\nYou select option",option,", Now Process for deleting employee details")
                    time.sleep(2)
                    portal_obj.deleteEmployeeDetails()
                    time.sleep(2)
                    print ('\n%sNow choose any option for another process'%color_obj.setColor('white'))
                    self.employeeOpration(portal_obj)
                elif op == 6:
                    print ("%sSuccessfully exit from Application. Thanking You...!!!"%color_obj.setColor('orange'))
                    sys.exit()
                else:
                    print ("\n%sYou select option {} is invalid. Please choose valid option".format(option) %color_obj.setColor('red'))
                    time.sleep(2)
                    return self.employeeOpration(portal_obj)
                loop = True
            else:
                print ("%sYou select wrong option" %color_obj.setColor('red'))
                time.sleep(1)
                print ("%sPlease enter value as digit like 1,2,3,...." %color_obj.setColor('red'))
        
portal_obj = ClassDemo.Portal()
runner_obj = Runner().employeeOpration(portal_obj)
