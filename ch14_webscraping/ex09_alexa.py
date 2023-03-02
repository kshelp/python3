import requests
from bs4 import BeautifulSoup

url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')

print(website_ranking[0:6])
'''
[<a href="https://support.alexa.com/hc/en-us/articles/200444340" target="_blank">this explanation</a>, <a href="/siteinfo/google.com">Google.com</a>, <a href="/siteinfo/naver.com">Naver.com</a>, <a href="/siteinfo/youtube.com">Youtube.com</a>, <a href="/siteinfo/daum.net">Daum.net</a>, <a href="/siteinfo/tistory.com">Tistory.com</a>]
'''

print(website_ranking[1].get_text())
# Google.com

website_ranking_address = [website_ranking_element.get_text(
) for website_ranking_element in website_ranking[1:]]
print(website_ranking_address[0:6])
'''
['Google.com', 'Naver.com', 'Youtube.com', 'Daum.net', 'Tistory.com', 'Kakao.com']
'''


url = "https://www.alexa.com/topsites/countries/KR"

html_website_ranking = requests.get(url).text
soup_website_ranking = BeautifulSoup(html_website_ranking, "lxml")

# p 태그의 요소 안에서 a 태그의 요소를 찾음
website_ranking = soup_website_ranking.select('p a')
website_ranking_address = [website_ranking_element.get_text(
) for website_ranking_element in website_ranking]

print("[Top Sites in South Korea]")
for k in range(6):
    print("{0}: {1}".format(k+1, website_ranking_address[k]))
'''
[Top Sites in South Korea]
1: this explanation
2: Google.com
3: Naver.com
4: Youtube.com
5: Daum.net
6: Tistory.com
'''
