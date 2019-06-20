from pyhive import hive

from sqlalchemy import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
from sqlalchemy import MetaData

engine = create_engine(
    'hive://fraud:ntR$on#01@10.10.88.192:10000/welfare',
    connect_args={'auth': 'LDAP'},
)
""" # 'hive://fraud:ntR$on#01@10.10.88.192:10000/fraud_test', """

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
s = session()


host_name = "115.31.153.211"
port = 10000
user = "fraud"
password = "ntR$on#01"
database = "fraud_test"


""" # conn = hive.Connection(host=host_name, port=port, username=user, password=password,
#                        database=database, auth='CUSTOM')
# cur = conn.cursor()

# with open('csvfile.csv', "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     writer.writerow(['actionlog_id', 'ip', 'username', 'title', 'description', 'created_date', 'email', 'last_login',
#                      'mobile', 'is_approved_by_admin', 'citizen_no', 'first_name_en', 'last_name_en', 'first_name_th', 'last_name_th'])
#     for val in data """

def connect():
    return s
print("--ok--")
