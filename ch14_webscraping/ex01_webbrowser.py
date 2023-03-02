import webbrowser

url = 'www.naver.com'
webbrowser.open(url)


naver_search_url = "http://search.naver.com/search.naver?query="
search_word = '파이썬'
url = naver_search_url + search_word

webbrowser.open_new(url)


google_url = "https://www.google.com/search?q="
search_word = 'python'
url = google_url + search_word

webbrowser.open_new(url)
