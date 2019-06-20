from models.hive_config import connect
from config import *
import datetime

s = connect()
app.route("/home")
def func():
    try:
        query = 'select * from src_transpaymentfact'
        data = s.execute(query)
        print (data)
    except:
        return("not connected")
