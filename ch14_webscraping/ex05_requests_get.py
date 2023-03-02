import requests

r = requests.get("https://www.google.co.kr")
print(r)
# <Response [200]>

print(r.text[0:100])
'''
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content
'''

html = requests.get("https://www.google.co.kr").text
print(html[0:100])
'''
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content
'''
