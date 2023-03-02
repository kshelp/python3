import glob
import requests
from bs4 import BeautifulSoup


def btop100():

    url = 'https://www.billboard.com/charts/hot-100/'

    html_music = requests.get(url).text
    soup_music = BeautifulSoup(html_music, "lxml")

    titles = soup_music.select('li.o-chart-results-list__item h3')
    artists = soup_music.select('li.o-chart-results-list__item h3+span')

    music_titles = [title.get_text().strip() for title in titles]
    music_artists = [artist.get_text().strip() for artist in artists]

    return music_titles, music_artists


# 날짜를 지정해 bugs_music_week_top100() 함수 호출
bugs_music_titles, bugs_music_artists = btop100()

# 곡명과 아티스트를 저장할 파일 이름을 폴더와 함께 지정
file_name = './ch17_webscraping/btop100.txt'

f = open(file_name, 'w', encoding="utf-8")  # 파일 열기

# 추출된 노래 제목과 아티스트를 파일에 저장
for k in range(len(bugs_music_titles)):
    f.write("{0:2d}: {1}/{2}\n".format(k+1,
                                       bugs_music_titles[k],  bugs_music_artists[k]))

f.close()  # 파일 닫기

print(glob.glob(file_name))  # 생성된 파일 확인
