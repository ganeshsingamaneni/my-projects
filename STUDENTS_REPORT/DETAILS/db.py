import csv
import MySQLdb
HOST = 'localhost'
USER = 'ganesh'
PASSWORD = 'ganesh55'
DATABASE = 'STUDENTSREPORT'


db=MySQLdb.connect(host = HOST, user = USER, passwd = PASSWORD, db = DATABASE)
cursor = db.cursor()

with open('/home/ganesh/dev/STUDENTS_REPORT/DETAILS/subject_faculty.csv','r') as subject_csv:
    subject_data = csv.reader(subject_csv)
    for y in subject_data:
        print (y)
        cursor.execute('INSERT INTO DETAILS_subject (name,faculty) values(%s ,%s  )',(y[0],y[1]))

with open('/home/ganesh/dev/STUDENTS_REPORT/DETAILS/student_marks.csv','r') as marks_csv:
    student_data = csv.reader(marks_csv)
    for x in student_data:
        cursor.execute('INSERT INTO DETAILS_studentmarks (student_name,subject,marks) values(%s ,%s ,%s )',(x[0],x[1],x[2]))

db.commit()
cursor.close()
