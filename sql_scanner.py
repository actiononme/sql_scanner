#!/usr/bin/env python3

import click

from core.Less1_Less4 import Less1_Less4
from core.Less5_Less6 import Less5_Less6
from core.Less7 import Less7
from core.Less8 import Less8
from core.Less9_Less10 import Less9_Less10
from core.Less11_Less12 import Less11_Less12
from core.Less13_Less14 import Less13_Less14
from core.Less15_Less16 import Less15_Less16
from core.Less17 import Less17
from core.Less18 import Less18
from core.Less19 import Less19
from core.Less20 import Less20
from core.Less21 import Less21
from core.Less22 import Less22
from core.Less23 import Less23
from core.Less25_Less25a import Less25_Less25a
from core.Less26_Less26a import Less26_Less26a
from core.Less27_Less27a import Less27_Less27a
from core.Less28_Less28a import Less28_Less28a
from core.Less29_Less31 import Less29_Less31
from core.Less32_Less37 import Less32_Less37
from core.Less38_Less41 import Less38_Less41
from core.Less42_Less45 import Less42_Less45
from core.Less46_Less47 import Less46_Less47
from core.Less48_Less49 import Less48_Less49
from core.Less50_Less53 import Less50_Less53
from core.Less54_Less57 import Less54_Less57
from core.Less58_Less61 import Less58_Less61
from core.Less62_Less65 import Less62_Less65







@click.command()
@click.option('--level',default=0,help='level of the labs')
@click.option('--dbs',is_flag=True,help='enumerate the databases')
@click.option('--tables',is_flag=True,help='enumerate the tables')
@click.option('--columns',is_flag=True,help='enumerate the columns')
@click.option('--schema',is_flag=True,help='enumerate the datas')
@click.option('-D',default='',help='database to enumerate')
@click.option('-T',default='',help='tables to enumerate')
@click.option('-C',default='',help='columns to enumerate')
@click.option('--shell',default='',help='provide a directory path for open a shell,only use for less_7')
@click.option('--exploit',default='',help='exploit username field or exploit password field,only for post method')
@click.option('--uname',default='',help='provide a uname,post method')
@click.option('--passwd',default='',help='provide a password,post method')
@click.option('-a',is_flag=True,help='use for 25a,26a,27a,28a method')

@click.argument('url')

def options(url,level,dbs,tables,columns,schema,d,t,c,shell,exploit,uname,passwd,a):
    
    less1_less4 = Less1_Less4(url,level,dbs,tables,columns,schema,d,t,c)

    less5_less6 = Less5_Less6(url,level,dbs,tables,columns,schema,d,t,c)

    less7 = Less7(url,level,shell)

    less8 = Less8(url,level,dbs,tables,columns,schema,d,t,c)
                                                                                # 初始化类，实例化类
    less9_less10 = Less9_Less10(url,level,dbs,tables,columns,schema,d,t,c)

    less11_less12 = Less11_Less12(url,level,dbs,tables,columns,schema,d,t,c,exploit)

    less13_less14 = Less13_Less14(url,level,dbs,tables,columns,schema,d,t,c,exploit)

    less15_less16 = Less15_Less16(url,level,dbs,tables,columns,schema,d,t,c,exploit)

    less17 = Less17(url,level,dbs,tables,columns,schema,d,t,c,exploit)

    less18 = Less18(url,level,dbs,tables,columns,schema,d,t,c,uname,passwd)

    less19 = Less19(url,level,dbs,tables,columns,schema,d,t,c,uname,passwd)

    less20 = Less20(url,level,dbs,tables,columns,schema,d,t,c,uname,passwd)

    less21 = Less21(url,level,dbs,tables,columns,schema,d,t,c,uname,passwd)

    less22 = Less22(url,level,dbs,tables,columns,schema,d,t,c,uname,passwd)

    less23 = Less23(url,level,dbs,tables,columns,schema,d,t,c)

    less25_less25a = Less25_Less25a(url,level,dbs,tables,columns,schema,d,t,c,a)

    less26_less26a = Less26_Less26a(url,level,dbs,tables,columns,schema,d,t,c,a)

    less27_less27a = Less27_Less27a(url,level,dbs,tables,columns,schema,d,t,c,a)

    less28_less28a = Less28_Less28a(url,level,dbs,tables,columns,schema,d,t,c,a)

    less29_less31 = Less29_Less31(url,level,dbs,tables,columns,schema,d,t,c)

    less32_less37 = Less32_Less37(url,level,dbs,tables,columns,schema,d,t,c,exploit)

    less38_less41 = Less38_Less41(url,level)

    less42_less45 = Less42_Less45(url,level,exploit)

    less46_less47 = Less46_Less47(url,level,dbs,tables,columns,schema,d,t,c)

    less48_less49 = Less48_Less49(url,level,dbs,tables,columns,schema,d,t,c)

    less50_less53 = Less50_Less53(url,level)

    less54_less57 = Less54_Less57(url,level,dbs,tables,columns,schema,d,t,c)

    less58_less61 = Less58_Less61(url,level,dbs,tables,columns,schema,d,t,c)

    less62_less65 = Less62_Less65(url,level,dbs,tables,columns,schema,d,t,c)

    if level == 1:

        less1_less4.Less_1()

    elif level == 2:

        less1_less4.Less_2()

    elif level == 3:

        less1_less4.Less_3()

    elif level == 4:

        less1_less4.Less_4()

    elif level == 5:

        less5_less6.Less_5()

    elif level == 6:

        less5_less6.Less_6()

    elif level == 7 and shell != '':

        less7.Less_7()

    elif level == 8:
                                            # 调用各自的level 等级,exploit them
        less8.Less_8()

    elif level == 9:

        less9_less10.Less_9()

    elif level == 10:

        less9_less10.Less_10()

    elif level == 11:

        less11_less12.Less_11()

    elif level == 12:

        less11_less12.Less_12()

    elif level == 13:
        
        less13_less14.Less_13()
        
    elif level == 14:

        less13_less14.Less_14()

    elif level == 15:

        less15_less16.Less_15()

    elif level == 16:

        less15_less16.Less_16()

    elif level == 17:

        less17.Less_17()

    elif level == 18:

        less18.Less_18()

    elif level == 19:

        less19.Less_19()

    elif level == 20:

        less20.Less_20()

    elif level == 21:

        less21.Less_21()

    elif level == 22:

        less22.Less_22()

    elif level == 23:

        less23.Less_23()

    elif level == 24:

        print("coming soon")

    elif level == 25 and not a:

        less25_less25a.Less_25()

    elif a and level == 25:
        
        less25_less25a.Less_25a()


    elif level == 26 and not a:

        less26_less26a.Less_26()

    elif level == 26 and a:

        less26_less26a.Less_26a()

    elif level == 27 and not a:

        less27_less27a.Less_27()

    elif level == 27 and a:

        less27_less27a.Less_27a()

    elif level == 28 and not a:

        less28_less28a.Less_28()

    elif level == 28 and a:

        less28_less28a.Less_28a()

    elif level == 29:

        less29_less31.Less_29()

    elif level == 30:

        less29_less31.Less_30()

    elif level == 31:

        less29_less31.Less_31()

    elif level == 32:

        less32_less37.Less_32()

    elif level == 33:

        less32_less37.Less_33()

    elif level == 34:

        less32_less37.Less_34()

    elif level == 35:

        less32_less37.Less_35()

    elif level == 36:

        less32_less37.Less_36()

    elif level == 37:

        less32_less37.Less_37()

    elif level == 38:

        less38_less41.Less_38()
    
    elif level == 39:

        less38_less41.Less_39()

    elif level == 40:

        less38_less41.Less_40()

    elif level == 41:

        less38_less41.Less_41()

    elif level == 42:

        less42_less45.Less_42()

    elif level == 43:

        less42_less45.Less_43()

    elif level == 44:

        less42_less45.Less_44()

    elif level == 45:

        less42_less45.Less_45()

    elif level == 46:

        less46_less47.Less_46()

    elif level == 47:

        less46_less47.Less_47()

    elif level == 48:

        less48_less49.Less_48()

    elif level == 49:

        less48_less49.Less_49()

    elif level == 50:

        less50_less53.Less_50()

    elif level == 51:

        less50_less53.Less_51()

    elif level == 52:

        less50_less53.Less_52()

    elif level == 53:

        less50_less53.Less_53()

    elif level == 54:

        less54_less57.Less_54()

    elif level == 55:

        less54_less57.Less_55()

    elif level == 56:

        less54_less57.Less_56()

    elif level == 57:

        less54_less57.Less_57()

    elif level == 58:

        less58_less61.Less_58()

    elif level == 59:

        less58_less61.Less_59()

    elif level == 60:

        less58_less61.Less_60()

    elif level == 61:

        less58_less61.Less_61()

    elif level == 62:

        less62_less65.Less_62()

    elif level == 63:

        less62_less65.Less_63()

    elif level == 64:

        less62_less65.Less_64()

    elif level == 65:

        less62_less65.Less_65()

if __name__=="__main__":

    options()
