import re
import sys
import csv

Input = open(sys.argv[1],'r')
input_data = Input.readlines()

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

def cleaing_header_row(line):
    line_ = re.sub(r"[?]","|",line)
    line_1 = re.sub(r"'","",line_)
    line_2 = re.sub('\s+',' ',line_1) 
    a = line_2.split('|')
    headers=[]
    m_headers=[]
    for zz in a:
        i = zz.rstrip(" ")
        if i.startswith("1A"):
            v = i[2:]
            headers.append(v)
        if i.isdigit():
            headers.append(i)
        else:
            if zz.startswith("1A"):
                pass
            else:    
                v = re.split(r'\d',i)
                headers.extend(v)
    headers.insert(0,'SEGMENT')
    for i in headers:
        if i.isspace():
            pass                
        if len(i)<=1:
            pass   
        else:
            m_headers.append(i)
    headers_data=[]        
    for x in m_headers:
        if x.endswith(("Fac.","Sec.")):
            H_ind = m_headers.index(x)
            H_L = len(x)
            H1 = m_headers[H_ind][:H_L-4]
            H2 = m_headers[H_ind][-4:]
            headers_data.append(H1)
            headers_data.append(H2)
        else:
            headers_data.append(x)     
    for x in headers_data:
        if x == ' ':
            headers_data.remove(x)
    return headers_data        

def cleaning_row(line):
    line_1 = line
    line_1 = line_1.split("\n")
    row_data=[]    
    for x in line_1:
        if x:
            if x.endswith("|"):
                x = re.sub(r"\|$","",x,1)
            l = re.sub(r"\,","+",x)      
            l1 = l.replace("|",",")
            l1 = l1.split(",")
            la=[]
            for x in l1:
                v=x.strip(" ")
                la.append(v)
            if la[0] == '':
                la.pop(0)
            row_data.extend(la)
    for x in row_data:
        if x == 'A':
            p = row_data.index(x)
            row_data[p] = ''            
        if "No" and "Yes" in x:
            if len(x)>9:
                ind = row_data.index(x)
                d1 = x[:4]
                d2 = x[len(x)-3:]
                row_data[ind] = d1
                row_data.insert(ind+1,d2)
            else:
                pass
    for x in row_data:
        if re.search(r'\d{2}       \d{2}$',x):
            ind_r = row_data.index(x)
            row_emp  = re.sub(r'\s+',',',x)
            sep = row_emp.split(',')
            row_data[ind_r] = sep[0]
            row_data.insert(ind_r+1,sep[1])
    final_data = []        
    for x in row_data:
        if row_data.index(x) == 0:
            final_data.append(x)
        elif len(x)>2:
            if x[0].isdigit():
                v = re.sub(r'\d{1,2}\s',' ',x,1)
                final_data.append(v)
            else:
                final_data.append(x)
        else:
            if x == '':
                final_data.append(x)
            elif x[0].isdigit():
                x= ' '
                final_data.append(x)
            else:
                final_data.append(x)            
    for x in final_data:
        if x.startswith("1A "):
            a_ind = final_data.index(x)
            a = x[2:]
            final_data[a_ind]= a#| \d{1,2} (.*)
        if re.search(r'\d+ \d+ (.*)|\d+ (.*) \d+ (.*)|(.*) \d{1,2} \d(.*)| \d{1,2} (.*)\d',x):
            f_index = final_data.index(x)
            d = re.sub(r'\s\d{1,2}\s',',',x)
            d_list = d.split(',')
            # print(d_list)
            final_data[f_index]=d_list[0]
            final_data.insert(f_index+1,d_list[1])    
    # print(": ",final_data)    
    return final_data           
             

content = 0
temp = []
for line in input_data:
    line = line.replace('=','-')
    if 'FORM' in line:
        content = 1
    if re.search(r'^SEGMENT\s',line):
        temp.append(line)
        continue
    if 'STATE BANK' in line:
        content = 0
    if content:
        temp.append(line)

temp_1 = []
for item in ''.join(temp).split('--'):
    if item:
        temp_1.append(item)


form_count = 0
form_name = []
form_=''
segment_name=''
for i in range(len(temp_1)):
    rows = []
    if "FORM" in temp_1[i]:
        form_ = getting_form_name(temp_1[i])
        if form_ not in form_name:
            form_name.append(form_)
            headers = cleaing_header_row(temp_1[i+1])
            write_csv(form_,[headers])
        segment_name = re.search(r'SEGMENT :(.*)',temp_1[i])
        if segment_name:
            segment_name = segment_name.group(1)
        else:
            segment_name = ''
    if not temp_1[i].startswith(("\nSrNo.","\nSLNO")):
        v = re.sub(r"\s+","",temp_1[i])
        if "|" in v:
            if v[0].isdigit():
                row = cleaning_row(temp_1[i])
                row.insert(0,segment_name)
                write_csv(form_,[row])
                
   
        




            

    

          


    



        