import re
import sys
import csv

INPUT = open(sys.argv[1],'r')
input_data = INPUT.readlines()

TEMP = open('test.txt','w')
def write_csv(name,content):
    with open(name+'.csv', 'a',newline='') as csvFile:
        writer = csv.writer(csvFile)
        for row in content:
            writer.writerow(row)



def getting_form_name(line):
    f1 = re.search(r'([^\s]+)',line).group(1)
    if f1 == 'FORM':
        line = line.strip().split('\n')[0]
        if re.search(r'\s*(.*\))',line):
            f1 = re.search(r'\s*(.*\))',line).group(1)
        else:
            f1 = line.split(':')[0]
    f1 = f1.replace(' ','').replace(':','-')
    return f1



def clening_row_header(line):
    lines = line.split('\n')
    ss = []
    for i in lines:
        if i:
            ss.extend([j.strip() for j in i.split('|')])
    # line = [i.strip() for i in line.split('|')]
    line = ss
    temp = []
    for i in line:
        j = re.split(r'^\d+\s',i)
        for t in j:
            if t:
                for k in re.split(r'\s\d+\s',t):
                    temp.append(k)
    return temp




def cleaning_row_old(line):
    lines = line.split('\n')
    ss = []
    for i in lines:
        if i:
            ff = [re.search(r'\s*(.*)',j).group(1) for j in i.split('|')]
            ss.extend(ff)
    line = ss
    if len(line) < 2:
        return []
    temp = [line[0],line[1]]
    for i in line[2:]:
        if re.search(r'^\d+$',i):
            temp.append(i)
        j = re.split(r'^\d+\s',i)
        for t in j:
            if t:
                if re.search(r'^1A',t):
                    t = t.replace('1A','')
                # if re.search(r'^\d+$',t):
                #     temp.append(t)
                #     continue
                for k in re.split(r'\s\d+\s',t):
                    temp.append(k)
    return temp

def cleaning_row(line):
    a = line
    a = a.split('\n')
    temp = []
    for i in a:
        i = re.search(r'\s*(.*)',i).group(1)
        i = i.split('|')
        tt = [] 
        for k in i:
            if k:
                if re.search(r'^\s*\d{1,2}\s.*\s\d{1,2}\s.*',k):
                    w = re.split(r'\d{1,2}\s',k)
                    tt.extend(w[1:])
                    continue
                if re.search(r'^\s?[\dA-Z]*\s.{2,}',k):
                    k = re.search(r'^\s?[\dA-Z]*\s(.{2,})',k).group(1)
                    tt.append(k)
                    continue
                tt.append(k)
        temp.extend(tt)
    # temp1 = []
    # for i in temp:
    #     if re.search():
    return temp


content = 0
temp = []
for line in input_data:
    line = line.replace('=','-')
    if 'FORM' in line:
        content = 1
    if re.search(r'^SEGMENT\s',line):
        TEMP.write(line)
        temp.append(line)
        continue
    if 'STATE BANK' in line:
        content = 0
    if content:
        TEMP.write(line)
        temp.append(line)

temp_1 = []
for item in ''.join(temp).split('--'):
    if item:
        temp_1.append(item)

head = False
rows = []
form_name = ''
count = 0
for i in range(len(temp_1)):
    if 'FORM' in temp_1[i]:
        if rows != []:
            write_csv(form_name,rows)
            rows = []
        if form_name != getting_form_name(temp_1[i]):
            form_name = getting_form_name(temp_1[i])
            count += 1
            header = ['Segment']+clening_row_header(temp_1[i+1])
            write_csv(form_name,[header])   #'test'+str(count)
            write_csv(form_name,rows)
        line = temp_1[i].replace('\n',' ')
        segment_name = re.search(r'SEGMENT :(.*)',line)
        if segment_name:
            segment_name = segment_name.group(1)
        else:
            segment_name = ''

        head = True
        continue
    if head:
        head = False
        continue
    row = temp_1[i].strip()
    row = cleaning_row(row)
    if len(row) < len(header)-3:
        continue
    row.insert(0,segment_name)
    rows.append(row)
    
write_csv(form_name,rows)        
    
        

  
