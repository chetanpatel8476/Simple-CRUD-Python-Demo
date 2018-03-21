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
        empName = input("%sEnter Employee Name:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))
        l.update({"Name":empName})
        while loop_phone == False:
            empPhone = input("%sEnter Employee Phone Number:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))
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
            empEmail = input("%sEnter Employee Email:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))
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
        print ("%sEmployee Id :" %Portal.color_obj.setColor('dark_green'),list(Portal.database.keys()))
        time.sleep(1)
        print ("\n%sNow process for update employee details" %Portal.color_obj.setColor('white'))
        time.sleep(2)
        while loop == False:
            num = int(input("%sEnter employee id which you want to update: " %Portal.color_obj.setColor('white')))
            if num in Portal.database:
                self.selectOption(num)
                print ("%sEmployee details updated successfully" %Portal.color_obj.setColor('green'))
                time.sleep(2)
                print ('\n%sNow select option for another process' %Portal.color_obj.setColor('white'))
                loop =True
            else:
                print ("%sEmployee Id {} doesn't exists in employee id list".format(num) %Portal.color_obj.setColor('red'),list(Portal.database.keys()))
    
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
        option = (input("%sEnter Options :%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))).split(',')
        for i in option:
            if i == "name" or i == "Name":
                name = input("%sEnter name which you want to update:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))
                record.update({'Name':name})
            elif i == "phone" or i == "Phone":
                while loop_phone_data == False:
                    phone = input("%sEnter phone which you want to update:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))
                    phoneData = re.search(r'\d{3}-\d{3}-\d{4}',phone)
                    empValidPhoneData = ''
                    if phoneData:
                        empValidPhoneData = phone
                        empValidPhoneData = self.checkPhoneValidation(empValidPhoneData)
                        if empValidPhoneData == None:
                            print ("%sPhone number {} which you entered is already exists".format(phone) %Portal.color_obj.setColor('red'))
                        else:
                            record.update({'Phone':empValidPhoneData})
                            loop_phone_data = True
                    else:
                        print ("%sPlease enter phone details as xxx-xxx-xxxx format" %Portal.color_obj.setColor('red'))
            elif i == "email" or i == "Email":
                while loop_email_data == False:
                    email = input("%sEnter email which you want to update:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white')))
                    emailData = re.search(r'[\w.]+@[\w.]+',email)
                    empValidEmailData = ''
                    if emailData:
                        empValidEmailData = email
                        empValidEmailData = self.checkEmailValidation(empValidEmailData)
                        if empValidEmailData == None:
                            print ("%sEmail id {} which you entered is already exists".format(email) %Portal.color_obj.setColor('red'))
                        else:
                            record.update({'Email':empValidEmailData})
                            loop_email_data = True
                    else:
                        print ("%sPlease enter email details as xxx@xxx.xxx format" %Portal.color_obj.setColor('red'))
            else:
                print ("%sSelect valid options" %Portal.color_obj.setColor('red'))
                time.sleep(2)
                return self.selectOption(num)

    def getEmployeeDetailsById(self):
        loop_data = False
        while loop_data == False:
            data = int(input('%sEnter employee id:%s' % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('white'))))
            if data in Portal.database:
               print ("%sEmployee details for employeeId {}:%s".format(data) % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('green')),Portal.database.get(data))
               loop_data = True
            else:
               print ("%sEmployee Id {} doesn't exist from employee list".format(data) %Portal.color_obj.setColor('red'))
        time.sleep(2)

    def printAllEmployee(self,database):
        if not Portal.database.items():
            print ("%sNo record found in employee list" %Portal.color_obj.setColor('red'))
        else:
            print ("%sAll Employee Details:%s" % (Portal.color_obj.setColor('blue'), Portal.color_obj.setColor('green')),database)
        time.sleep(2)
        
    def deleteEmployeeDetails(self):
        loop_data = False
        if not Portal.database.items():
            print ("\nNo records found. First you create employee details")
            time.sleep(2)
            print ("\nProcess for creating new employee")
            time.sleep(2)
            self.createEmployeeDetails()
            print ("%sEmployee created successfully" %Portal.color_obj.setColor('green'))
            time.sleep(2)
            print ("\n%sNow Process for delete existing employee record" %Portal.color_obj.setColor('white'))
        while loop_data == False:
            data = int(input('%sEnter employee id:' %Portal.color_obj.setColor('blue')))
            if data in Portal.database:
                Portal.database.pop(data)
                print ("Employee id {} deleted successfully from employee list".format(data) %Portal.color_obj.setColor('green'))
                loop_data = True
            else:
                print ("%sNo record found" %Portal.color_obj.setColor('red'))
    
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
