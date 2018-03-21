import re
import time
import Colors

class Employee: 
    def __init__(self,empId,empName,empValidPhone,empValidEmail):
        self.empId = empId
        self.empName = empName
        self.empValidPhone = empValidPhone
        self.empValidEmail = empValidEmail
    
class Portal(Employee):
    database = {}
    color_obj = Colors.Color()
    def __init__(self):
        pass 
    
    def createEmployeeDetails(self):
        d = {}
        l = {}
        loop_id = False
        loop_phone = False
        loop_email = False
        
        while loop_id == False:
            empId = int(input("%sEnter Employee Id:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white'))))
            empValidId = ''
            if empId in Portal.database:
                print ("%sEmployee Id {} Already Exists.".format(empId) %Portal.color_obj.setColor('red'))
                time.sleep(2)
            else:
                empValidId  = empId
                loop_id = True
        empName = input("%sEnter Employee Name:" %Portal.color_obj.setColor('blue'))
        l.update({"Name":empName})
        while loop_phone == False:
            empPhone = input("%sEnter Employee Phone Number:" %Portal.color_obj.setColor('blue'))
            phoneObj = re.search(r'\d{3}-\d{3}-\d{4}',empPhone)
            empValidPhone = ''
            if phoneObj:
                empValidPhone = empPhone
                empValidPhone = self.checkPhoneValidation(empValidPhone)
                if empValidPhone == None:
                    print ("%sPhone number {} which you entered is already exists".format(empPhone) %Portal.color_obj.setColor('red'))
                else:
                    l.update({"Phone":empValidPhone})
                    loop_phone = True
            else:
                print ("%sPlease enter phone details as xxx-xxx-xxxx format" %Portal.color_obj.setColor('red'))
        while loop_email == False:
            empEmail = input("%sEnter Employee Email:" %Portal.color_obj.setColor('blue'))
            emailObj = re.search(r'[\w.]+@[\w.]+',empEmail)
            empValidEmail = ''
            if emailObj:
                empValidEmail = empEmail
                empValidEmail = self.checkEmailValidation(empValidEmail)
                if empValidEmail == None:
                    print ("%sEmail id {} which you entered is already exists".format(empEmail) %Portal.color_obj.setColor('red'))
                else:
                    l.update({"Email":empValidEmail})
                    loop_email = True
            else:
                print ("%sPlease enter email details as xxx@xxx.xxx format" %Portal.color_obj.setColor('red'))
           
        d.update({empValidId:l})
        Portal.database.update(d)
        
    def updateEmployeeDetails(self):
        loop = False
        if not Portal.database.items():
            print ("\n%sNo records found. First you create employee details" %Portal.color_obj.setColor('red'))
            time.sleep(2)
            print ("\n%sProcess for creating new employee" %Portal.color_obj.setColor('white'))
            time.sleep(2)
            self.createEmployeeDetails()
            print ("%sEmployee created successfully" %Portal.color_obj.setColor('green'))
            time.sleep(2)
        print ("Employee Id List: ",list(Portal.database.keys()))
        print ("\nNow process for update employee details")
        time.sleep(2)
        while loop == False:
            num = int(input("Enter employee id which you want to update: "))
            if num in Portal.database:
                self.selectOption(num)
                print ("%sEmployee details updated successfully" %Portal.color_obj.setColor('green'))
                time.sleep(2)
                print ('\n%sNow select option for another process' %Portal.color_obj.setColor('white'))
                loop =True
            else:
                print ("%sEmployee Id {} doesn't exists in employee id list".format(num) %Portal.color_obj.setColor('red'),Portal.database.keys())
    
    def selectOption(self,num):
        loop_phone_data = False
        loop_email_data = False
        record = Portal.database.get(num)
        print ('''%sChoose option to update :
        Name
        Phone
        Email
        ''' %Portal.color_obj.setColor('orange'))
        print ("\n%sNOTE: Please select option as per format like option1,option2,option3,etc..." %Portal.color_obj.setColor('orange'))
        option = (input("Enter Options :")).split(',')
        for i in option:
            if i == "name" or i == "Name":
                name = input("Enter name which you want to update:")
                record.update({'Name':name})
            elif i == "phone" or i == "Phone":
                while loop_phone_data == False:
                    phone = input("Enter phone which you want to update:")
                    phoneData = re.search(r'\d{3}-\d{3}-\d{4}',phone)
                    empValidPhoneData = ''
                    if phoneData:
                        empValidPhoneData = phone
                        empValidPhoneData = self.checkPhoneValidation(empValidPhoneData)
                        if empValidPhoneData == None:
                            print ("Phone number",phone,"which you entered is already exists")
                        else:
                            record.update({'Phone':empValidPhoneData})
                            loop_phone_data = True
                    else:
                        print ("Please enter phone details as xxx-xxx-xxxx format")
            elif i == "email" or i == "Email":
                while loop_email_data == False:
                    email = input("Enter email which you want to update:")
                    emailData = re.search(r'[\w.]+@[\w.]+',email)
                    empValidEmailData = ''
                    if emailData:
                        empValidEmailData = email
                        empValidEmailData = self.checkEmailValidation(empValidEmailData)
                        if empValidEmailData == None:
                            print ("Email id",email,"which you entered is already exists")
                        else:
                            record.update({'Email':empValidEmailData})
                            loop_email_data = True
                    else:
                        print ("Please enter email details as xxx@xxx.xxx format")
            else:
                print ("Select valid options")
                time.sleep(2)
                return self.selectOption(num)
    
    def printAllEmployee(self,database):
        if not Portal.database.items():
            print ("No Any Records Available, Please Create Employee Details")
        else:
            print ("All Employee Details:",database)
        time.sleep(2)
        
    def deleteEmployeeDetails(self):
        loop_data = False
        if not Portal.database.items():
            print ("\nNo records found. First you create employee details")
            time.sleep(2)
            print ("\nProcess for creating new employee")
            time.sleep(2)
            self.createEmployeeDetails()
            print ("Employee created successfully")
            time.sleep(2)
            print ("\nNow Process for delete existing employee record")
        while loop_data == False:
            data = int(input('Enter employee id:'))
            if data in Portal.database:
                Portal.database.pop(data)
                print ("Employee id",data,"deleted successfully")
                loop_data = True
            else:
                print ("No record found")
    
    def checkPhoneValidation(self,empValidPhone):
        record = {}
        list1 = []
        phone = None
        data = Portal.database.values()
        for data1 in data:
            record.update(data1)
            if "Phone" in record:
                list1.append(record.get("Phone"))
        if empValidPhone not in list1:
            #print "Phone which you entered is valid"
            phone = empValidPhone
            return phone
        else:
            return phone   
     
    def checkEmailValidation(self,empValidEmail):
        record = {}
        list1 = []
        email = None
        data = Portal.database.values()
        for data1 in data:
            record.update(data1)
            if "Email" in record:
                list1.append(record.get("Email"))
        if empValidEmail not in list1:
            #print "Phone which you entered is valid"
            email = empValidEmail
            return email
        else:
            return email 
