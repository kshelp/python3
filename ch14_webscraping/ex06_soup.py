from bs4 import BeautifulSoup

# 테스트용 html 코드
html = """<html><body><div><span>\
        <a href=http://www.naver.com>naver</a>\
        <a href=https://www.google.com>google</a>\
        <a href=http://www.daum.net/>daum</a>\
        </span></div></body></html>"""

# BeautifulSoup를 이용해 HTML 소스를 파싱
soup = BeautifulSoup(html, 'lxml')
print(soup)
'''
<html><body><div><span> <a href="http://www.naver.com">naver</a> <a href="https://www.google.com">google</a> <a href="http://www.daum.net/">daum</a> </span></div></body></html>
'''

print(soup.prettify())
'''
<html>
 <body>
  <div>
   <span>
    <a href="http://www.naver.com">
     naver
    </a>
    <a href="https://www.google.com">
     google
    </a>
    <a href="http://www.daum.net/">
     daum
    </a>
   </span>
  </div>
 </body>
</html>
'''

print(soup.find('a'))
# <a href="http://www.naver.com">naver</a>

print(soup.find('a').get_text())
# naver

print(soup.find_all('a'))
'''
[<a href="http://www.naver.com">naver</a>, <a href="https://www.google.com">google</a>, <a href="http://www.daum.net/">daum</a>]
'''

site_names = soup.find_all('a')
for site_name in site_names:
    print(site_name.get_text())
'''
naver
google
daum
'''


# 테스트용 HTML 코드
html2 = """
<html>
 <head>
  <title>작품과 작가 모음</title>
 </head>
 <body>
  <h1>책 정보</h1>
  <p id="book_title">토지</p>
  <p id="author">박경리</p>
  
  <p id="book_title">태백산맥</p>
  <p id="author">조정래</p>

  <p id="book_title">감옥으로부터의 사색</p>
  <p id="author">신영복</p>
 </body>
</html>
"""

soup2 = BeautifulSoup(html2, "lxml")
print(soup2.title)
# <title>작품과 작가 모음</title>

print(soup2.body)
'''
<body>
<h1>책 정보</h1>
<p id="book_title">토지</p>
<p id="author">박경리</p>
<p id="book_title">태백산맥</p>
<p id="author">조정래</p>
<p id="book_title">감옥으로부터의 사색</p>
<p id="author">신영복</p>
</body>
'''

print(soup2.body.h1)
# <h1>책 정보</h1>

print(soup2.find_all('p'))
'''
[<p id="book_title">토지</p>, <p id="author">박경리</p>, <p id="book_title">태백 
산맥</p>, <p id="author">조정래</p>, <p id="book_title">감옥으로부터의 사색</p>, 
<p id="author">신영복</p>]
'''

print(soup2.find('p', {"id": "book_title"}))
# <p id="book_title">토지</p>

print(soup2.find('p', {"id": "author"}))
# <p id="author">박경리</p>

print(soup2.find_all('p', {"id": "book_title"}))
'''
[<p id="book_title">토지</p>, <p id="book_title">태백산맥</p>, <p id="book_title">감옥으로부터의 사색</p>]
'''

print(soup2.find_all('p', {"id": "author"}))
'''
[<p id="author">박경리</p>, <p id="author">조정래</p>, <p id="author">신영복</p>]
'''

soup2 = BeautifulSoup(html2, "lxml")

book_titles = soup2.find_all('p', {"id": "book_title"})
authors = soup2.find_all('p', {"id": "author"})

for book_title, author in zip(book_titles, authors):
    print(book_title.get_text() + '/' + author.get_text())
'''
토지/박경리
태백산맥/조정래
감옥으로부터의 사색/신영복
'''

print(soup2.select('body h1'))
# [<h1>책 정보</h1>]

print(soup2.select('body p'))
# print(soup2.select('p'))
'''
[<p id="book_title">토지</p>, <p id="author">박경리</p>, <p id="book_title">태백 
산맥</p>, <p id="author">조정래</p>, <p id="book_title">감옥으로부터의 사색</p>, 
<p id="author">신영복</p>]
'''

print(soup2.select('p#book_title'))
'''
[<p id="book_title">토지</p>, <p id="book_title">태백산맥</p>, <p id="book_title">감옥으로부터의 사색</p>]
'''

print(soup2.select('p#author'))
'''
[<p id="author">박경리</p>, <p id="author">조정래</p>, <p id="author">신영복</p>]
'''

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
