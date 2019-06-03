import os
import csv

path="gs://passport_ocr/p_u_arab_emirates"
x='p_u_arab_emirates'

def test():

   for root,dirs,files in os.walk("/home/ganesh/new_images/e-visas/new_p_visas"):
       for filename in files:
           file=os.path.join(path, filename)
           with open('/home/ganesh/ganesh.csv', 'a') as csv_file:
               writer = csv.writer(csv_file)
               writer.writerow([file, x])
test()
