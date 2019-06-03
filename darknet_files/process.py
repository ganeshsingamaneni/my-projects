import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

# Directory where the data will reside, relative to 'darknet.exe'
path_data = 'aadhaar/'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('/home/ganesh/my-projects/darknet/train.txt', 'w')
file_test = open('/home/ganesh/my-projects/darknet/test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
# print("okkkkkk")
index_test = round(100 / percentage_test)
# print("i: ",index_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.JPG")):
    # print("//////")
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1

        file_test.write(path_data + title + '.JPG' + "\n")
    else:

        file_train.write(path_data + title + '.JPG' + "\n")
        counter = counter + 1
