import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
# p = pd.Panel(data)
# print(p)
s = pd.Series(5, index=[0, 1, 2, 3])
# print (s)
# importing pandas as pd 
import pandas as pd 

# Create the MultiIndex 
# midx = pd.MultiIndex.from_tuples([(10, 'Ten'), (10, 'Twenty'), 
								# (20, 'Ten'), (20, 'Twenty')], 
								# 		names =['Num', 'Char']) 

# Print the MultiIndex 
# print(midx)
d = {'one' : pd.Series([1, 2, 3],dtype = int),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)
# print (df)
# d = {'one' : pd.Series([1, 2, 3],index = ['a','b','c'],dtype= int),
#    'two' : pd.Series([1, 2, 9, 4], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)
# print (df.iloc[3])
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
# p = pd.Panel(data)
# print (p['Item1'])
# print(p['Item2']) 
# print(p.major_xs(0))
# print(p.minor_xs(1))
import mysql.connector as sql
import MySQLdb
db=MySQLdb.connect(host = '104.199.146.29', user = 'root', passwd = 'Welcome@123', db = 'sakila')
# cursor = db.cursor()

df = pd.read_sql('SELECT * FROM rental', con=db)
d = pd.DataFrame(df,columns = ['id','rental_date','inventory_id'])
# v = d.head()
# se = d[['id','rental_date','inventory_id']]
rec = d.to_dict('records')
r = pd.DataFrame(rec)
# print(rec,type(rec))
# print(se.to_dict('records'))
# print(se.set_index('id').T.to_dict('list'))
from sqlalchemy import create_engine
# engine = create_engine("mysql+mysqldb://ganesh:"+'ganesh55'+"@localhost/sakila")
# se.to_sql(con=engine,name = 'rental', if_exists='append', index=False)
l= []
for x in rec:
   if x['id']>=100 and len(str(x['inventory_id']))>1:#s and x['rental_date'].strftime("%d")=='25':
      if len(str(x['id']))>2:
         l.append(x)
# print(l)
ree = pd.DataFrame(l)
print(ree.ndim)
engine = create_engine("mysql+mysqldb://ganesh:"+'ganesh55'+"@localhost/sakila")
ree.to_sql(con=engine,name = 'rental', if_exists='append', index=False)
