import os
from os import walk, getcwd
from PIL import Image




def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    a = (box[0] + box[1])/2.0
    b = (box[2] + box[3])/2.0
    c = box[1] - box[0]
    d= box[3] - box[2]
    x = a*dw
    w = c*dw
    y = b*dh
    h = d*dh
    return (x,y,w,h)


"""-------------------------------------------------------------------"""

""" Configure Paths"""
mypath = "/home/ganesh/my-projects/darknet/textfiles/licence_3/"
outpath = "/home/ganesh/my-projects/darknet/scripts/images/licence_3/"
dir=["licence_3"]
cls = "licence_3"
if cls not in dir:
    exit(0)
cls_id = dir.index(cls)
#/home/ganesh/my-projects/darknet/scripts/images/visa
wd = getcwd()
list_file = open('%s/%s_list.txt'%(wd, cls), 'w')

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
# print(txt_name_list)

""" Process """
for txt_name in txt_name_list:

    """ Open input text files """
    txt_path = mypath + txt_name
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\r\n')   #for ubuntu, use "\r\n" instead of "\n"

    """ Open output text files """
    txt_outpath = outpath + txt_name
    print(txt_outpath)
    txt_outfile = open(txt_outpath, "w")


    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        if(len(line) >= 2):
            ct = ct + 1
            elems = line.split(' ')
            a=elems[0].split("  ")
            ele=[]
            for x in elems:
                if '\n' in x:
                    b,c = x.split("\n")
                    ele.append(b)
                    ele.append(c)
                else:
                    ele.append(x)
            #print(ele)
            m=ele.pop(0)
            print(m)
            #print(m)
            last_e_pop = ele.pop()
            len_ele = len(ele)
            ele_in_a_list = len_ele/int(m)
            new_list = [ele[int(ele_in_a_list)*i:int(ele_in_a_list)*(i+1)] for i in range(len(ele)//int(ele_in_a_list) + 1)]
            #print(new_list)
            new_list.pop()
            classes =[]
            class_textfile = open("/home/ganesh/my-projects/darknet/class.txt",'r')
            class_readlines = class_textfile.readlines()
            for x in class_readlines:
                classes.append(x)
            for x, y in zip(new_list, classes):
                x.append(y)
            #print(new_list)
            for elems in new_list:
                xmin = elems[0]
                xmax = elems[2]
                ymin = elems[1]
                ymax = elems[3]
                label_name = elems[4]
                label_id = classes.index(label_name+"\n")
                img_path = str('%s/scripts/images/%s/%s.JPG'%(wd, cls, os.path.splitext(txt_name)[0]))
                #print(img_path)
                im=Image.open(img_path)
                #print(img_path)
                w= int(im.size[0])
                h= int(im.size[1])
                b = (float(xmin),
                float(xmax), float(ymin), float(ymax))
                #print(w,h,b)
                bb = convert((w,h), b)
                #print("/////: ",bb)
                txt_outfile.write(str(label_id) + " " + " ".join([str(a) for a in bb]) + '\n')

        """ Save those images with bb into list"""
    if(ct != 0):
        list_file.write('%s/images/%s/%s.JPG\n'%(wd, cls, os.path.splitext(txt_name)[0]))

list_file.close()
