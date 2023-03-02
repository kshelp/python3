import requests
import os
from bs4 import BeautifulSoup

URL = 'https://www.reshot.com/search/animal'

html_reshot_image = requests.get(URL).text
soup_reshot_image = BeautifulSoup(html_reshot_image, "lxml")
reshot_image_elements = soup_reshot_image.select('a img')
reshot_image_elements[0:4]

reshot_image_url = reshot_image_elements[1].get('src')
print(reshot_image_url)
'''
https://res.cloudinary.com/twenty20/private_images/t_reshot-400/v1521838685/photosp/bae96789-a5ab-4471-b54f-9686ace09e33/bae96789-a5ab-4471-b54f-9686ace09e33.jpg
'''


html_image = requests.get(reshot_image_url)

folder = './ch17_webscraping/download'  # 이미지를 내려받을 폴더를 지정

# os.path.basename(URL)는 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리
imageFile = open(os.path.join(
    folder, os.path.basename(reshot_image_url)), 'wb')

# 이미지 데이터를 1000000 바이트씩 나눠서 저장
chunk_size = 1000000
for chunk in html_image.iter_content(chunk_size):
    imageFile.write(chunk)
imageFile.close()


import requests  
from bs4 import BeautifulSoup 
import os

# URL(주소)에서 이미지 주소를 추출
def get_image_url(url): 
    html_image_url = requests.get(url).text
    soup_image_url = BeautifulSoup(html_image_url, "lxml")  
    image_elements = soup_image_url.select('a img') 
    if(image_elements != None):
        image_urls = []
        for image_element in image_elements[1:]:
            image_urls.append(image_element.get('src'))
        return image_urls        
    else:
        return None
    
# 폴더를 지정해 이미지 주소에서 이미지 내려받기
def download_image(img_folder, img_url):
    if(img_url != None):  
        html_image = requests.get(img_url)
        # os.path.basename(URL)은 웹사이트나 폴더가 포함된 파일명에서 파일명만 분리 
        imageFile = open(os.path.join(img_folder, os.path.basename(img_url)), 'wb')

        chunk_size = 1000000 # 이미지 데이터를 1000000 바이트씩 나눠서 저장
        for chunk in html_image.iter_content(chunk_size):
            imageFile.write(chunk)
            imageFile.close()
        print("이미지 파일명: '{0}'. 내려받기 완료!".format(os.path.basename(img_url))) 
    else:       
        print("내려받을 이미지가 없습니다.")
        
# 웹 사이트의 주소를 지정   
reshot_url = 'https://www.reshot.com/search/animal'

figure_folder = "./ch17_webscraping/download" # 이미지를 내려받을 폴더를 지정  

reshot_image_urls = get_image_url(reshot_url) # 이미지 파일의 주소 가져오기

num_of_download_image = 7 # 내려받을 이미지 개수를 지정
# num_of_download_image = len(reshot_image_urls) # 전체 이미지 개수

for k in range(num_of_download_image):
    download_image(figure_folder, reshot_image_urls[k])
print("================================")
print("선택한 모든 이미지 내려받기 완료!")

num_of_download_image = len(reshot_image_urls)
print(num_of_download_image)
# 50
