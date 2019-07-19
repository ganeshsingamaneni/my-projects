# from __future__ import print_function
# import os

# from PIL import Image

# files = [
#   '~/1.jpg',
#   '~/2.jpg',
#   '~/3.jpg',
#   '~/4.jpg',
#   '~/4.jpg',
#   '~/5.jpg',
#   '~/6.jpg',
#   '~/7.jpg',
#   '~/8.jpg',
#   '~/9.jpg',
#   '~/10.jpg',]

# result = Image.new("RGB", (800, 800))

# for index, file in enumerate(files):
#   path = os.path.expanduser(file)
#   img = Image.open(path)
#   img.thumbnail((400, 400), Image.ANTIALIAS)
#   x = index // 2 * 400
#   y = index % 2 * 400
#   w, h = img.size
# #   print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
#   result.paste(img, (x, y, x + w, y + h))

# result.save(os.path.expanduser('~/merge.jpg'))


import os
import os.path
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime,date
work_dir =os.getcwd()
# draw = ImageDraw.Draw(image)
def imgstich(dir):
  
    finalpath=work_dir+'/'+str(datetime.now().time())+'stiched.jpeg'
    empty=[]
    image_dir = os.path.abspath(dir)
    files = sorted([ f for f in os.listdir(image_dir)])
    num = len(files)
    for x in files:
        empty.append(os.sep.join([image_dir,x]))

    # print(empty,",,,,,,")
    n_files = len(empty)
    # print (n_files)

    target_img = None
    n_targets = 0
    collage_saved = False
    for n in range(n_files):
        # print(len(files[n]))
        file_name = files[n][10:len(files[n])-7]
        if files[n].endswith("invoice.jpg.jpg"):
            pass
        elif files[n].endswith("Total_description_table.jpg.jpg"):
            pass    
        else:    
            img = Image.open(empty[n])

            img.thumbnail((700, 300))
            

            if n % num*num == 0:
                
                target_img = Image.new("RGB", (1000, 1000))
                n_targets += 1
                collage_saved = False

            # paste the image at the correct position
            i = int(n / num)
            j = n % num
            draw = ImageDraw.Draw(target_img)
            font = ImageFont.truetype("arial.ttf", 25)
            draw.text((700,n*105), "xy!="+file_name, fill='rgb(350, 350, 350)', font=font)
            target_img.paste(img, (100*i, 100*j))

            if (n + 1) % num*num == 0 and target_img is not None:
                # save a finished 8x8 collage
                target_img.save(finalpath.format(n_targets))
                collage_saved = True

    # save the last collage
    if not collage_saved:
        target_img.save(finalpath.format(n_targets))
        return finalpath

        
imgstich("/home/ganesh/my-projects/latest_dar/darknet/result_img/")



