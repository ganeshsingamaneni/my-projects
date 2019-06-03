# from PyPDF2 import PdfFileReader, PdfFileWriter

# file = open('/home/ganesh/2012.pdf','rb')
# reader = PdfFileReader(file)


# n = reader.getNumPages()

# for i in range (n):
#     writer = PdfFileWriter()
#     writer.addPage(reader.getPage(i))
#     split_motive = open('/home/ganesh/p' + str(i+1) + '.pdf','wb')
#     writer.write(split_motive)
#     split_motive.close()

import os
path = '/home/ganesh/Downloads/dri_new/'
files = os.listdir(path)


#for index, file in enumerate(files):
 #   index = index+265
    #os.rename(os.path.join(path, file), os.path.join(path, str(index)+'.JPG'))

import os.path, time
#print("Last modified: %s" % time.ctime(os.path.getmtime("/home/ganesh/example.py")))
#print("Created: %s" % time.ctime(os.path.getctime("/home/ganesh/example.py")))
x = 10
def globallyChange():
    global x            # Access the global var
    x = "didn't work"
    print("/", x)
globallyChange()        # Call the function
#print(x)

# from sqlalchemy import *
# from sqlalchemy.engine import create_engine
# from sqlalchemy.schema import *
# from sqlalchemy.sql import select, insert
# from sqlalchemy import MetaData

# engine = create_engine('hive://fraud:ntR$on#01@115.31.153.211:10000/fraud_test',connect_args={'auth': 'LDAP'})
# from sqlalchemy.orm import sessionmaker
# session = sessionmaker()
# session.configure(bind=engine)
# s = session()
# if engine:
# 	print("Ok")
from pyhive import hive
import pandas as pd

#Create Hive connection 
# conn = hive.Connection(host="115.31.153.211", port=10000, username="fraud")#,password="ntR$on#01")

# # Read Hive table and Create pandas dataframe
# df = pd.read_sql("SELECT * FROM fraud_test.src_transpaymentfact ", conn)
# print(df.head())

# hive://fraud:ntR$on#01@115.31.153.211:10000/fraud_test

from sqlalchemy.orm import sessionmaker
from pyhive import hive

# from sqlalchemy import *
# from sqlalchemy.engine import create_engine
# from sqlalchemy.schema import *
# from sqlalchemy import MetaData

# engine = create_engine(
#    'hive://fraud:ntR$on#01@115.31.153.211:10000/welfare',
#    connect_args={'auth': 'LDAP'},
# )

# session = sessionmaker()
# session.configure(bind=engine)
# s = session()
# # query = s.execute('select * from src_transpaymentfact')
# print(s)


# host_name = "115.31.153.211"
# port = 10000
# user = "fraud"
# password = "ntR$on#01"
# database = "fraud_test"


# conn = hive.Connection(host=host_name, port=port, username=user, password=password, database=database, auth='CUSTOM')
# cur = conn.cursor()

# Python Programming illustrating 
# numpy.eye method 

import numpy as geek 

# 2x2 matrix with 1's on main diagnol 
b = geek.eye(2, dtype = float) 
print("Matrix b : \n", b) 

# matrix with R=4 C=5 and 1 on diagnol 
# below main diagnol 
a = geek.eye(4, 5,k=-1) 
print("\nMatrix a : \n", a)

