import glob
import requests
from bs4 import BeautifulSoup

# 주간 뮤직 차트 (날짜 지정)
url = "https://music.bugs.co.kr/chart/track/week/total?chartdate=20200921"
# url = "https://music.bugs.co.kr/chart/track/realtime/total" # 실시간 뮤직 차트
# url = "https://music.bugs.co.kr/chart/track/day/total" # 일간 뮤직 차트
# url = "https://music.bugs.co.kr/chart/track/week/total" # 주간 뮤직 차트

html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

# p 태그의 요소 중에서 class 속성값이 "title" 인 것을 찾고
# 그 안에서 a 태그의 요소를 추출
titles = soup_music.select('p.title a')
print(titles[0:7])
'''
[<a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('32374864',true);
" title="쉬어 (Feat. MINO) (Prod. GRAY)">쉬어 (Feat. MINO) (Prod. GRAY)</a>, <a adultchheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09p_chart');bugs.music.listen('6132120',true);
" title="strawberry moon">strawberry moon</a>, <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('32374863',true);
" title="Wake Up (Prod. 코드 쿤스트)">Wake Up (Prod. 코드 쿤스트)</a>, <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('6133448',true);
" title="낮 밤 (feat. 박재범)">낮 밤 (feat. 박재범)</a>, <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('6135536',true);
" title="어제 너는 나를 버렸어">어제 너는 나를 버렸어</a>, <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('32349594',true);
" title="Savage">Savage</a>, <a adultcheckval="1" aria-label="새창" href="javascript:;" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('32374861',true);    
" title="TROUBLE (Prod. Slom)">TROUBLE (Prod. Slom)</a>]
'''

music_titles = [title.get_text() for title in titles]
print(music_titles[0:7])
'''
['쉬어 (Feat. MINO) (Prod. GRAY)', 'strawberry moon', 'Wake Up (Prod. 코드 쿤스트)', ' 
낮 밤 (feat. 박재범)', '어제 너는 나를 버렸어', 'Savage', 'TROUBLE (Prod. Slom)']  
'''

# p 태그의 요소 중에서 class 속성값이 "artist" 인 것을 찾고
# 그 안에서 a 태그의 요소를 추출
artists = soup_music.select('p.artist a')
print(artists[0:7])
'''
[<a class="artistTitle" href="https://music.bugs.co.kr/artist/80185895?wl_ref=list_tr_10_chart" title="MINO(송민호)">MINO(송민호)</a>, <a class="more" href="javascript:void(0);" name="atag_martist_list" onclick="bugs.layermenu.openMultiArtistSearchResultPopLayer(this, 'MINO(송민호)||MINO(송민호)||80185895||OK\\nAnandelight||아넌딜라이트(Anandelight)||20070271||OK\\nunofficialboyy||unofficialboyy||20036043||OK\\nBE\'O (비오)||BE\'O 
(비오)||80337001||OK\\n지구인||지구인||80126124||OK\\nMudd the student||Mudd the student||20096572||OK', ''); return false;" title="아티스트 전체보기" wise_log_str="?wl_ref=list_tr_10_chart">
MINO(송민호)
</a>, <a href="https://music.bugs.co.kr/artist/80049126?wl_ref=list_tr_10_chart" onclick="
" title="아이유(IU)">아이유(IU)</a>, <a class="artistTitle" href="https://music.bugs.co.kr/artist/2916?wl_ref=list_tr_10_chart" title="개코">개코</a>, <a class="more" href="javascript:void(0);" name="atag_martist_list" onclick="bugs.layermenu.openMultiArtistSearchResultPopLayer(this, '개코||개코||2916||OK\\nOurealgoat||Ourealgoat (아우릴고트)||20076067||OK\\nSINCE||SINCE||20056615||OK\\n안병웅||안병웅||20086251||OK\\nTabber||Tabber||80212388||OK\\n조광일||조광일||20087231||OK', ''); return false;" title="아티스트 전 
체보기" wise_log_str="?wl_ref=list_tr_10_chart">
개코
</a>, <a href="https://music.bugs.co.kr/artist/20079471?wl_ref=list_tr_10_chart" onclick="
" title="이영지">이영지</a>, <a href="https://music.bugs.co.kr/artist/80067149?wl_ref=list_tr_10_chart" onclick="
" title="10CM">10CM</a>]
'''

artists = soup_music.select('p.artist a:not(.more)')
print(artists[0:7])
'''
[<a class="artistTitle" href="https://music.bugs.co.kr/artist/80185895?wl_ref=list_tr_10_chart" title="MINO(송민호)">MINO(송민호)</a>, <a href="https://music.bugs.co.kr/artist/80049126?wl_ref=list_tr_10_chart" onclick="
" title="아이유(IU)">아이유(IU)</a>, <a class="artistTitle" href="https://music.bugs.co.kr/artist/2916?wl_ref=list_tr_10_chart" title="개코">개코</a>, <a href="https://music.bugs.co.kr/artist/20079471?wl_ref=list_tr_10_chart" onclick="
" title="이영지">이영지</a>, <a href="https://music.bugs.co.kr/artist/80067149?wl_ref=list_tr_10_chart" onclick="
" title="10CM">10CM</a>, <a href="https://music.bugs.co.kr/artist/80347326?wl_ref=list_tr_10_chart" onclick="
" title="aespa">aespa</a>, <a class="artistTitle" href="https://music.bugs.co.kr/artist/80085859?wl_ref=list_tr_10_chart" title="Zion.T">Zion.T</a>]
'''

music_artists = [artist.get_text() for artist in artists]
print(music_artists[0:7])
# ['MINO(송민호)', '아이유(IU)', '개코', '이영지', '10CM', 'aespa', 'Zion.T']


url = "https://music.bugs.co.kr/chart/track/week/total?chartdate=20200921"
html_music = requests.get(url).text
soup_music = BeautifulSoup(html_music, "lxml")

titles = soup_music.select('p.title a')
artists = soup_music.select('p.artist a:not(.more)')

music_titles = [title.get_text() for title in titles]
music_artists = [artist.get_text().strip() for artist in artists]

for k in range(7):
    print("{0}: {1} / {2}".format(k+1, music_titles[k], music_artists[k]))
'''
1: Dynamite / 방탄소년단
2: Bad Boy / 청하
3: 취기를 빌려 (취향저격 그녀 X 산들) / 산들
4: Tight / 10CM
5: 그리워하면 그댈 만날까봐 / 김나영
6: 숲의 아이 (Bon voyage) / 유아 (오마이걸)
7: 밤새 (취향저격 그녀 X 카더가든) / 카더가든
'''

music_titles_artists = {}
order = 0

for (music_title, music_artist) in zip(music_titles, music_artists):
    order = order + 1
    music_titles_artists[order] = [music_title, music_artist]

print(music_titles_artists[1])
# ['Dynamite', '방탄소년단']

print(music_titles_artists[2])
# ['Bad Boy', '청하']


# 날짜를 입력하면 벅스 차트에서 주간 음악 순위(1~100위)의 곡명과 아티스트를 반환
def bugs_music_week_top100(year, month, day):

    # 월과 일의 경우는 항상 두 자리로 맞춤
    month = "{0:02d}".format(month)
    day = "{0:02d}".format(day)

    base_url = 'https://music.bugs.co.kr/chart/track/week/total?'
    url = base_url + 'chartdate={0}{1}{2}'.format(year, month, day)

    html_music = requests.get(url).text
    soup_music = BeautifulSoup(html_music, "lxml")

    titles = soup_music.select('p.title a')
    artists = soup_music.select('p.artist a:not(.more)')

    music_titles = [title.get_text() for title in titles]
    music_artists = [artist.get_text().strip() for artist in artists]

    return music_titles, music_artists


# 날짜를 지정해 bugs_music_week_top100() 함수 호출
bugs_music_titles, bugs_music_artists = bugs_music_week_top100(2020, 9, 21)

# 곡명과 아티스트를 저장할 파일 이름을 폴더와 함께 지정
file_name = './ch17_webscraping/bugs_week_top100.txt'

f = open(file_name, 'w', encoding="utf-8")  # 파일 열기

# 추출된 노래 제목과 아티스트를 파일에 저장
for k in range(len(bugs_music_titles)):
    f.write("{0:2d}: {1}/{2}\n".format(k+1,
                                       bugs_music_titles[k],  bugs_music_artists[k]))

f.close()  # 파일 닫기

glob.glob(file_name)  # 생성된 파일 확인
