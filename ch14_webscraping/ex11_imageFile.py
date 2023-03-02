import requests  

url = 'https://www.python.org/static/img/python-logo.png'

html_image = requests.get(url)
print(html_image)


import os

image_file_name = os.path.basename(url)
print(image_file_name)
# python-logo.png


folder = './ch17_webscraping/download' 

if not os.path.exists(folder):
    os.makedirs(folder)


image_path = os.path.join(folder, image_file_name)
print(image_path)
# ./ch17_webscraping/download\python-logo.png

imageFile = open(image_path, 'wb')

# 이미지 데이터를 1000000 바이트씩 나눠서 내려받고 파일에 순차적으로 저장
chunk_size = 1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()

print(os.listdir(folder))
# ['python-logo.png']



import requests  
import os

url = 'https://www.python.org/static/img/python-logo.png'
html_image = requests.get(url)
image_file_name = os.path.basename(url)

folder = './ch17_webscraping/download' 

if not os.path.exists(folder):
    os.makedirs(folder)

image_path = os.path.join(folder, image_file_name)

imageFile = open(image_path, 'wb')
# 이미지 데이터를 1000000 바이트씩 나눠서 저장
chunk_size = 1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()