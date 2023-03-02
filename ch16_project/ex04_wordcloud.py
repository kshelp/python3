from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_name = './ch19_project/littleprince_djvu.txt'

with open(file_name) as f: # 파일을 읽기 모드로 열기
    text = f.read() # 파일의 내용 읽어오기

# 워드 클라우드의 이미지를 생성합니다.
wordcloud_image = WordCloud().generate(text)

# 생성한 워드 클라우드 이미지를 화면에 표시합니다.
plt.imshow(wordcloud_image, interpolation='bilinear')
plt.axis("off")
plt.show()


wordcloud_image = WordCloud(background_color='white', max_font_size=300, width=800, height=400).generate(text)

plt.imshow(wordcloud_image, interpolation="bilinear")
plt.axis("off")
plt.show()


image_file_name = './ch19_project/little_prince.png'

wordcloud_image.to_file(image_file_name)
plt.show()


import pandas as pd

word_count_file = "./ch19_project/word_count.csv"
word_count = pd.read_csv(word_count_file, index_col = '단어')
print(word_count.head(5))
'''
        빈도
단어
산업혁명  1662
기술    1223
사업    1126
혁신    1084
경제    1000
'''

print(word_count['빈도'][0:5])
'''
단어
산업혁명    1662
기술      1223
사업      1126
혁신      1084
경제      1000
Name: 빈도, dtype: int64
'''


from wordcloud import WordCloud
import matplotlib.pyplot as plt

korean_font_path = 'C:/Windows/Fonts/malgun.ttf' # 한글 폰트(맑은 고딕) 파일명

# 워드 클라우드 이미지 생성
wc = WordCloud(font_path=korean_font_path, background_color='white')

frequencies = word_count['빈도'] # pandas의 Series 형식이 됨
wordcloud_image = wc.generate_from_frequencies(frequencies)

# 생성한 워드 클라우드 이미지를 화면에 표시
plt.imshow(wordcloud_image, interpolation="bilinear")
plt.axis("off")
plt.show()