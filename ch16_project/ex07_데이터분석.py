# 데이터 분석
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data_folder = './ch19_project/seoul_expense/'
years = [2017, 2018, 2019]

df_expense_all = pd.DataFrame()

for year in years:
    expense_list_year_dir = data_folder + str(year) + '/'
    expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)

    path_file_name = expense_list_year_dir + expense_list_tidy_file

    df_expense = pd.read_csv(path_file_name)
    df_expense_all = df_expense_all.append(df_expense, ignore_index=True)


print(df_expense_all.info())
'''
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 216557 entries, 0 to 216556
Data columns (total 12 columns):       
 #   Column  Non-Null Count   Dtype
---  ------  --------------   -----
 0   제목      216557 non-null  object
 1   부서레벨1   216557 non-null  object
 2   부서레벨2   216273 non-null  object
 3   집행연도    216557 non-null  int64
 4   집행월     216557 non-null  int64
 5   부서명     216478 non-null  object
 6   집행일시    216557 non-null  object
 7   집행장소    214401 non-null  object
 8   집행목적    216535 non-null  object
 9   대상인원    215535 non-null  object
 10  결제방법    216354 non-null  object
 11  집행금액    216557 non-null  int64
dtypes: int64(3), object(9)
memory usage: 19.8+ MB
None
'''

print(df_expense_all.head(2))
'''
                             제목  부서레벨1 부서레벨2  집행연도  ...               집행목적            대상 
인원 결제방법    집행금액
0  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017  ...  기본소득과 장애인복지 논
의간담회  장애인복지정책팀장 외 2명   카드   76000
1  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017  ...   장애인단체 활동지원 논 
의간담회  장애인복지정책과장 외 3명   카드  102000

[2 rows x 12 columns]
'''

print(df_expense_all.tail(2))
'''
                                                제목 부서레벨1    부서레벨2  ...       대상인원  결제방법    
집행금액
216555  2019년 12월 사업소 서울시립대학교 중앙도서관 사서과 업무추진비 - 전체   사업소  서울시립대학교  ...  
사서과장 외 8명    카드  23940
216556  2019년 12월 사업소 서울시립대학교 중앙도서관 사서과 업무추진비 - 전체   사업소  서울시립대학교  ...  
  이용자 80명    카드  53420

[2 rows x 12 columns]
'''


# 1. 연도별 추이 분석
year_expense = df_expense_all['집행연도'].value_counts()
print(year_expense)
'''
2019    74207
2018    72218
2017    70132
Name: 집행연도, dtype: int64
'''

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

plt.bar(year_expense.index, year_expense.values,
        tick_label=year_expense.index, width=0.5)
plt.title("연도별 업무추진비 집행 횟수")
plt.xlabel("연도")
plt.ylabel("집행 횟수")
plt.show()


year_total = pd.pivot_table(df_expense_all, index=[
                            '집행연도'], values=['집행금액'], aggfunc=sum)
print(year_total)
'''
             집행금액
집행연도
2017   9076941387
2018   9937556542
2019  10532330632
'''

eok_won = 100000000  # 억원
(year_total/eok_won).plot.bar(rot=0)  # 'rot = 각도'로 xtick 회전 각도를 지정
plt.ylabel('집행금액(억원)')
plt.show()


# 2. 월별 집행금액 분석
month_total = pd.pivot_table(df_expense_all, index=['집행월'], values=['집행금액'],
                             aggfunc=sum)
print(month_total)
'''
           집행금액
집행월
1    2328469179
2    2250971737
3    2314589911
4    2153704599
5    2063883588
6    2224855495
7    2372256669
8    2153716469
9    2417217365
10   2326108698
11   2719921484
12   4221133367
'''

year_month_total = pd.pivot_table(df_expense_all, index=['집행월'], columns=['집행연도'],
                                  values=['집행금액'], aggfunc=sum)
print(year_month_total)
'''
            집행금액
집행연도        2017        2018        2019
집행월
1      710368860   735587570   882512749
2      712679864   769360005   768931868
3      737250454   761059010   816280447
4      635265805   703781418   814657376
5      647582378   669044701   747256509
6      758257342   690652154   775945999
7      701604626   788926477   881725566
8      661174850   730290532   762251087
9      806170700   769404957   841641708
10     637219943   827022975   861865780
11     843619171   960310221   915992092
12    1225747394  1532116522  1463269451
'''

eok_won = 100000000  # 억원

(year_month_total/eok_won).plot.bar(rot=0)
plt.ylabel('집행금액(억원)')
plt.title("업무추진비의 월별 집행금액")
plt.legend(['2017년', '2018년', '2019년'])
plt.show()


# 3. 부서별 집행 내역 분석
dept_level1_total = pd.pivot_table(df_expense_all, index=['부서레벨1'], values=['집행금액'],
                                   aggfunc=sum)
print(dept_level1_total)
'''
                    집행금액
부서레벨1
사업소           6552128899
서울시본청        16606242519
소방재난본부(소방서)   5147645293
의회사무처         1240811850
'''


dept_level_2_total = pd.pivot_table(df_expense_all, index=['부서레벨2'], values=['집행금액'],
                                    aggfunc=sum)
print(dept_level_2_total.head())
'''
               집행금액
부서레벨2
119특수구조단  119225100
감사위원회     343281170
강남소방서     229660520
강동소방서     188773330
강북소방서     167700000
'''


dept_level_2_total_top10 = dept_level_2_total.sort_values(
    by=['집행금액'], ascending=False)[0:10]
print(dept_level_2_total_top10)
'''
                집행금액
부서레벨2
상수도사업본부   2156404778
기획조정실     1572753168
행정국       1320839804
서울특별시장     955448760
시민소통기획관    923338423
도시기반시설본부   620669144
정무부시장      581806882
행정1부시장     540457390
행정2부시장     522277598
기후환경본부     515222890
'''

eok_won = 100000000  # 억원

(dept_level_2_total_top10/eok_won).plot.bar(rot=80)
plt.ylabel('집행금액(억원)')
plt.title("업무추진비 집행금액이 높은 상위 10개 부서")
plt.show()


korean_font_path = 'C:/Windows/Fonts/malgun.ttf'  # 한글 폰트(맑은 고딕) 파일명

# 워드 클라우드 이미지 생성
wc = WordCloud(font_path=korean_font_path, background_color='white',
               width=800, height=600)

frequencies = dept_level_2_total['집행금액']  # pandas의 Series 형식이 됨
wordcloud_image = wc.generate_from_frequencies(frequencies)

plt.figure(figsize=(12, 9))
plt.axis('off')
plt.imshow(wordcloud_image, interpolation='bilinear')
plt.show()


# 4. 요일별 및 시간대별 집행 내역 분석
print(df_expense_all['집행일시'].values)
'''
['2017-01-26 13:10' '2017-01-25 22:41' '2017-01-24 12:35' ...
 '2019-12-19 11:34' '2019-12-16 12:39' '2019-12-03 17:35']
'''

expense_date_time = pd.to_datetime(df_expense_all['집행일시'])
print(expense_date_time.values)
'''
['2017-01-26T13:10:00.000000000' '2017-01-25T22:41:00.000000000'
 '2017-01-24T12:35:00.000000000' ... '2019-12-19T11:34:00.000000000'
 '2019-12-16T12:39:00.000000000' '2019-12-03T17:35:00.000000000']
'''

week_day_name = ["월", "화", "수", "목", "금", "토", "일"]

df_expense_all['집행일시_요일'] = [week_day_name[weekday]
                             for weekday in expense_date_time.dt.weekday]

df_expense_all['집행일시_시간'] = [hour for hour in expense_date_time.dt.hour]

print(df_expense_all.head(3))
'''
 집행금액 집행일시_요일 집행일시_시간
0  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017    1  ...  장애인복지정책팀장 
외 2명   카드   76000       목      13
1  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017    1  ...  장애인복지정책과장 
외 3명   카드  102000       수      22
2  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017    1  ...    장애인복지정책팀 
장외7명   카드   80000       화      12

[3 rows x 14 columns]
'''


expense_weekday = df_expense_all['집행일시_요일'].value_counts()
print(expense_weekday)
'''
목    45683
화    43812
수    42343
금    41381
월    39498
토     2238
일     1602
Name: 집행일시_요일, dtype: int64
'''

expense_weekday = expense_weekday.reindex(index=week_day_name)
print(expense_weekday)
'''
월    39498
화    43812
수    42343
목    45683
금    41381
토     2238
일     1602
Name: 집행일시_요일, dtype: int64
'''

expense_weekday.plot.bar(rot=0)
plt.title("요일별 업무추진비 집행 횟수")
plt.xlabel("요일")
plt.ylabel("집행 횟수")
plt.show()


expense_hour_num = df_expense_all['집행일시_시간'].value_counts()
print(expense_hour_num)
'''
12    87518
20    23013
13    20990
19    16766
21    12210
11     8356
14     8311
15     7168
10     5824
18     5783
16     5169
0      4919
9      3486
17     2889
22     2563
8       875
7       412
23      128
1        44
6        42
3        27
4        26
5        19
2        19
Name: 집행일시_시간, dtype: int64
'''


work_hour = [(k+8) % 24 for k in range(24)]
expense_hour_num = expense_hour_num.reindex(index=work_hour)
print(expense_hour_num)
'''
8       875
9      3486
10     5824
11     8356
12    87518
13    20990
14     8311
15     7168
16     5169
17     2889
18     5783
19    16766
20    23013
21    12210
22     2563
23      128
0      4919
1        44
2        19
3        27
4        26
5        19
6        42
7       412
Name: 집행일시_시간, dtype: int64
'''


expense_hour_num.plot.bar(rot=0)
plt.title("시간별 업무추진비 집행 횟수")
plt.xlabel("집행 시간")
plt.ylabel("집행 횟수")
# plt.show()


expense_hour_total = pd.pivot_table(df_expense_all, index=['집행일시_시간'],
                                    values=['집행금액'], aggfunc=sum)
print(expense_hour_total.head())
'''
집행일시_시간
0        842523116
1          7024161
2          2265190
3          7215762
4          5818431
'''


eok_won = 100000000  # 억원
expense_hour_total = expense_hour_total.reindex(index=work_hour)

(expense_hour_total/eok_won).plot.bar(rot=0)
plt.ylabel('집행금액(억원)')
plt.title("시간별대 업무추진비 집행금액")
plt.show()
