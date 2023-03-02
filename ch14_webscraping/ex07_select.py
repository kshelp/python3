from bs4 import BeautifulSoup

f = open('./ch17_webscraping/HTML_example_my_site.html', encoding='utf-8')
html3 = f.read()
f.close()
soup3 = BeautifulSoup(html3, "lxml")

print(soup3.select('a'))
'''
[<a class="portal" href="http://www.naver.com" id="naver">네이버</a>, <a class="search" href="https://www.google.com" id="google">구글</a>, <a class="portal" href="http://www.daum.net" id="daum">다음</a>, <a class="government" href="http://www.nl.go.kr" id="nl">국립중앙도서관</a>]
'''

print(soup3.select('a.portal'))
'''
[<a class="portal" href="http://www.naver.com" id="naver">네이버</a>, <a class="portal" href="http://www.daum.net" id="daum">다음</a>]
'''

print(soup3.select('a#naver'))
'''
[<a class="portal" href="http://www.naver.com" id="naver">네이버</a>]
'''
