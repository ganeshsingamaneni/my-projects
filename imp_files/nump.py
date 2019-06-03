# import numpy as np
# from numpy import pi
# import pdb
# a = np.array([[[1,2,3],[4,5,6],[1,2,3],[2,3,4]]])
# # print(a.data)
# c = np.array( [ [1,2], [3,4] ], dtype=complex )
# # print(c)
# # print(np.zeros((2,3,4),dtype = int))
# # print(np.ones((2,3,4),dtype = float))
# # print(np.empty((5,2),dtype=int))
# # print(np.arange(10).reshape(2,5))
# x = np.linspace(1,3*pi,100)
# # print(np.sin(x))
# A = np.array( [[1,1],[0,1]])
# B = np.array( [[2,0],[3,4]] )
# # print("1",A*B)
# # print("2",A@B)
# # print(":",A.dot(B))
# a = np.arange(3*4*5*6).reshape((3,4,5,6))
# # print(a)
# b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
# # print(b)
# # print(np.dot(a, b)[2,3,2,1])
# c = np.arange(120).reshape(2,3,4,5)         
# # print(c)
# # np.set_printoptions(threshold=np.nan)
# # print(np.arange(10000).reshape(100,100))
# a = np.array( [20,30,40,50] )
# b = np.arange(4)
# # breakpoint()
# # print(a-b)
# v  = np.zeros((5), dtype = np.int,order = 'F') 
# vv = np.array([1,2,3,4,5])
# vvv = v+vv
# # print(vvv)
# # pdb.set_trace()


# x = ord('A')
# # print(x)

# # print(ord('c'))
# # print(ord('ç'))
# # print(ord('$'))

# code_str = 'x=5\ny=10\nprint("sum =",x+y)'
# code = compile(code_str, 'sum.py', 'exec')
# # print(type(code))
# # exec(code)
# # print(dir(vvv))

# # simple example, returns (a // b, a % b) for integers
# # dm = divmod(20, 3)
# # print(dm)

# # x, y = divmod(10, 3)
# # print(x)
# # print(y)

# # dm = divmod(0xF, 0xF)  # hexadecimal
# # print(dm)

# # dm = divmod(3 + 2J, 3)
# # print(dm)
# # class Person:
# #     name = 'Adam'
    
# # p = Person()
# # print('Before modification:', p.name)

# # # setting name to 'John'
# # setattr(p, 'age', 22)

# # print('After modification:', p.age)
# arr2d_b = np.array([1,0,10], dtype='object')
# # print(arr2d_b,arr2d_b.tolist())

# import matplotlib.pyplot as plt
# N = 8
# y = np.zeros(N)
# x1 = np.linspace(0, 10, N, endpoint=True)
# x2 = np.linspace(0, 10, N, endpoint=False)
# # plt.plot(x1, y, 'r')
# # print(x1,x2)

# # plt.plot(x2, y + 0.5, 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.scatter(x1, x1, 'r--', x1, x1**2, 'b', x1, x1**3, 'g*')


# # plt.ylim([-0.5, 2])
# # plt.xlim([-2,12])
# plt.xlabel('chinoodu')
# plt.ylabel('pedoodu')


# plt.show()
# import numpy as np 
# a = np.arange(16).reshape(4,4) 

# # print'First array:' 
# # print(a) 
# # print '\n'  

# # print 'Horizontal splitting:' 
# b = np.vsplit(a,2) 
# # print(b) 
# # print '\n'
# import schedule
# import time
# def geeks():
#     nnn=np.linspace(2.0, 3.0, num=5)
#     print(nnn)
# # schedule.every(10).seconds.do(geeks) 
# # while True: 
  
# #    # Checks whether a scheduled task  
# #     # is pending to run or not 
# #     schedule.run_pending() 
# #     time.sleep(1)
# import pandas as pd
# customer_data_file = '/home/ganesh/Downloads/carated_pkg17085572.xls'
# customers = pd.read_html(customer_data_file)
# sheetname=0,
# header=0,
# index_col=False,
# keep_default_na=True)
# print(customers)
from pandas.io import sql

import mysql.connector as sql
import MySQLdb
import pandas as pd
db=MySQLdb.connect(host = 'localhost', user = 'ganesh', passwd = 'ganesh55', db = 'mall')
# cursor = db.cursor()

df = pd.read_sql('SELECT * FROM user', con=db)
# print(":",df)

d = pd.DataFrame(df,index=[x for x in range(len(df))])
# print(d)
dattt = {'name':'pr2asant2h','email':'prasanth12@caratred.com'}
t = pd.DataFrame(data = dattt,index = ['2'])
# print(db)
# t.to_sql( name='user',con=db, if_exists = 'append',index=False)
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://ganesh:"+'ganesh55'+"@localhost/mall")
t.to_sql(con=engine,name = 'user', if_exists='append', index=False)

