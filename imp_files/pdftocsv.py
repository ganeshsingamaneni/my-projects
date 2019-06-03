# import tabula
# from tabula import read_pdf


# output = read_pdf('/home/ganesh/p2.pdf',multiple_tables=True,guess = False,pages="all")
# # a = output.to_string()
# # tfile = open('/home/ganesh/test.txt', 'a')
# # tfile.write(a)
# # tfile.close()
# print(output)#.iloc[:,:3])
# # output.to_csv('/home/ganesh/1.csv',sep=' ', index=False, header=False)
# tabula.convert_into("/home/ganesh/2012.pdf", "pdf2.txt", output_format="text",multiple_tables=True,guess = False,pages="all")

# # Input = open('/home/ganesh/test.txt','r')
# # input_data = Input.readlines()
# # print(": ",input_data)
# # for x in input_data[6]:
# #     print(x,type(x))


# # import PyPDF2
# # pdfFileObj = open('/home/ganesh/2012.pdf','rb')     
# # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# # print(pdfReader.numPages)
# # pageObj = pdfReader.getPage(1)          
# # a = pageObj.extractText()
# # print(a)

# # import io
 
# # from pdfminer.converter import TextConverter
# # from pdfminer.pdfinterp import PDFPageInterpreter
# # from pdfminer.pdfinterp import PDFResourceManager
# # from pdfminer.pdfpage import PDFPage
 
# # def extract_text_from_pdf(pdf_path):
# #     resource_manager = PDFResourceManager()
# #     fake_file_handle = io.StringIO()
# #     converter = TextConverter(resource_manager, fake_file_handle)
# #     page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
# #     with open(pdf_path, 'rb') as fh:
# #         for page in PDFPage.get_pages(fh, 
# #                                       caching=True,
# #                                       check_extractable=True):
# #             page_interpreter.process_page(page)
 
# #         text = fake_file_handle.getvalue()
 
# #     # close open handles
# #     converter.close()
# #     fake_file_handle.close()
 
# #     if text:
# #         return text
 
# # if __name__ == '__main__':
# #     # print(extract_text_from_pdf('/home/ganesh/2012.pdf'))


# import textract
# text = textract.process('/home/ganesh/page_2.jpg')#, method='pdfminer')
# # print(text)

# from tika import parser
# # print("=======================================================")
# raw = parser.from_file('/home/ganesh/2012.pdf')
# # print(raw['content'])
# # print(raw.viewkeys())
# # print(raw.keys())


# import pdf2image
# from PIL import Image
# import time

# PDF_PATH = "/home/ganesh/2012.pdf"
# DPI = 200
# OUTPUT_FOLDER = None
# FIRST_PAGE = None
# LAST_PAGE = None
# FORMAT = 'jpg'
# THREAD_COUNT = 1
# USERPWD = None
# USE_CROPBOX = False
# STRICT = False

# def pdftopil():
#     start_time = time.time()
#     pil_images = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER, first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT, userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)
#     print ("Time taken : " + str(time.time() - start_time))
#     return pil_images
    
# def save_images(pil_images):
#     index = 1
#     for image in pil_images:
#         image.save("page_" + str(index) + ".jpg")
#         index += 1

# # if __name__ == "__main__":
#     # pil_images = pdftopil()
#     # save_images(pil_images)


# Simple Python program to compare dates 

# importing datetime module 
import datetime 
# from datetime import datetime

# d = datetime.now()
# print(d)
# date in yyyy/mm/dd format 
d1 = datetime.datetime(2018, 5, 3) 
d2 = datetime.datetime(2018, 6, 1) 

# # Comparing the dates will return 
# #either True or False 
# print("d1 is greater than d2 : ", d1 > d2) 
# print("d1 is less than d2 : ", d1 < d2) 
# print("d1 is not equal to d2 : ", d1 != d2) 
# import dateutil.parser
# import datetime
# from pytz import utc
# date_time1 ='2017-04-15 00:00:00'
# date_time2 ='2017-04-17 15:35:19+00:00'


# parsed1 = dateutil.parser.parse(date_time1).astimezone(utc)
# parsed2 = dateutil.parser.parse(date_time2).astimezone(utc)
# if parsed1 > parsed2:
#     print("ok")
# else:
#     print("fail")    

