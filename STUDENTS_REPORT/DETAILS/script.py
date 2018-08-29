import random
import csv
students = ['student'+str(i) for i in range(1, 101)]

faculties  = [('Mathematics', 'Murali Krishna'), ('Telugu', 'Amarnath'), ('English', 'Samuel'),
              ('Social', 'Krishna Reddy'), ('Physics', 'Raja Gopal'), ('Chemistry', 'Ravi') ]

with open('student_marks.csv', 'w') as f:
    for student in students:
        for sub, fac in faculties:
            f.write(','.join([student, sub, str(random.sample(range(1, 101), 1)[0])]) + '\n')

with open('subject_faculty.csv', 'w') as f:
    for rec in faculties:
        f.write(','.join(rec) + '\n')



students_marks = []
with open('student_marks.csv') as f:
    for line in f:
        columns = line.split(',')
        columns[-1] = int(columns[-1].rstrip('\n'))
        students_marks.append(tuple(columns))


subject_faculty = []
with open('subject_faculty.csv') as f:
       for line in f:
           columns = line.split(',')
           columns[-1] = columns[-1].rstrip('\n')
           subject_faculty.append(tuple(columns))
