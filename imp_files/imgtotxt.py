import pytesseract
from PIL import Image

# result = pytesseract.image_to_string(Image.open("/home/ganesh/my-projects/latest_dar/darknet/result_img/2.jpg"), lang="eng")#,graceful_errors=True)
# print(result)
import base64
import json
import requests,re
# from itertools import izip, chain



def detect_text(image_file):
    
    with open(image_file, "rb") as image_fil:
        encoded_string = base64.b64encode(image_fil.read()).decode()
    url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyAOztXTencncNtoRENa1E3I0jdgTR7IfL0'
    header = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': encoded_string,
            },
            'features': [{
                'type': 'DOCUMENT_TEXT_DETECTION',
                'maxResults': 100,
            }],
            "imageContext":{
            "languageHints":["en-t-iO-handwrit"]
            }
        }]
    }
    response = requests.post(url, headers=header, json=body).json()
    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
    split_text=re.split(r'\n',text)
    print(text)
    indexes=[]
    for x,y in enumerate(split_text):
        if y.startswith("xy!="):
            indexes.append(x+1)       
    total_data = [split_text[i : j] for i, j in zip([0] + indexes, indexes + [None])] 
    output = {}
    for x in total_data:
        length = len(x)
        if length == 0:
            pass
        elif length == 1:
            output.update({x[0]:"None"})
        else:
            key = x[-1]  
            value = ' '.join(x[:length-1])
            output.update({key:value})
    print(output)          


detect_text("/home/ganesh/my-projects/latest_dar/15:37:02.565731stiched.jpeg")

