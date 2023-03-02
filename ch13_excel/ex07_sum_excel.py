# 행 데이터의 합계 구하기
import pandas as pd

df = pd.read_excel('./ch16_excel/담당자별_판매량_통합.xlsx')

handbag = df[(df['제품명'] == '핸드백')]
print(handbag)
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기
2  핸드백   A  가  385  316  355  331
5  핸드백   B  나  350  340  377  392
8  핸드백   C  다  365  383  308  323
'''

handbag_sum = pd.DataFrame(handbag.sum(axis=1), columns=['연간판매량'])
print(handbag_sum)
'''
   연간판매량
2   1387
5   1459
8   1379
'''

handbag_total = handbag.join(handbag_sum)
print(handbag_total)
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기  연간판매량
2  핸드백   A  가  385  316  355  331   1387
5  핸드백   B  나  350  340  377  392   1459
8  핸드백   C  다  365  383  308  323   1379
'''

print(handbag_total.sort_values(by='연간판매량', ascending=True))
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기  연간판매량
8  핸드백   C  다  365  383  308  323   1379
2  핸드백   A  가  385  316  355  331   1387
5  핸드백   B  나  350  340  377  392   1459
'''

print(handbag_total.sort_values(by='연간판매량', ascending=False))
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기  연간판매량
5  핸드백   B  나  350  340  377  392   1459
2  핸드백   A  가  385  316  355  331   1387
8  핸드백   C  다  365  383  308  323   1379
'''


# 열 데이터의 합계 구하기
print(handbag_total.sum())
'''
제품명      핸드백핸드백핸드백
담당자            ABC
지역             가나다
1분기           1100
2분기           1039
3분기           1040
4분기           1046
연간판매량         4225
dtype: object
'''

handbag_sum2 = pd.DataFrame(handbag_total.sum(), columns=['합계'])
print(handbag_sum2)
'''
              합계
제품명    핸드백핸드백핸드백
담당자          ABC
지역           가나다
1분기         1100
2분기         1039
3분기         1040
4분기         1046
연간판매량       4225
'''

handbag_total2  = handbag_total.append(handbag_sum2.T)
print(handbag_total2)
'''
          제품명  담당자   지역   1분기   2분기   3분기   4분기 연간판
매량
2         핸드백    A    가   385   316   355   331  1387
5         핸드백    B    나   350   340   377   392  1459
8         핸드백    C    다   365   383   308   323  1379
합계  핸드백핸드백핸드백  ABC  가나다  1100  1039  1040  1046  4225 
'''

handbag_total2.loc['합계', '제품명'] = '핸드백'
handbag_total2.loc['합계', '담당자'] = '전체'
handbag_total2.loc['합계', '지역'] = '전체'

print(handbag_total2)
'''
    제품명 담당자  지역   1분기   2분기   3분기   4분기 연간판매량
2   핸드백   A   가   385   316   355   331  1387
5   핸드백   B   나   350   340   377   392  1459
8   핸드백   C   다   365   383   308   323  1379
합계  핸드백  전체  전체  1100  1039  1040  1046  4225
'''


import pandas as pd

# 엑셀 파일을 pandas의 DataFrame 형식으로 읽어온다.
df = pd.read_excel('./ch16_excel/담당자별_판매량_통합.xlsx')

# 제품명 열에서 핸드백이 있는 행만 선택한다.
product_name = '핸드백'
handbag = df[(df['제품명']== product_name)]

# 행별로 합계를 구하고 마지막 열 다음에 추가한다.
handbag_sum = pd.DataFrame(handbag.sum(axis=1), columns = ['연간판매량'])
handbag_total = handbag.join(handbag_sum)

# 열별로 합해 분기별 합계와 연간판매량 합계를 구하고 마지막 행 다음에 추가한다.
handbag_sum2 = pd.DataFrame(handbag_total.sum(), columns=['합계'])
handbag_total2  = handbag_total.append(handbag_sum2.T)

# 지정된 항목의 문자열을 변경한다.
handbag_total2.loc['합계', '제품명'] = product_name
handbag_total2.loc['합계', '담당자'] = '전체'
handbag_total2.loc['합계', '지역'] = '전체'

# 결과를 확인한다.
print(handbag_total2)
'''
    제품명 담당자  지역   1분기   2분기   3분기   4분기 연간판매량
2   핸드백   A   가   385   316   355   331  1387
5   핸드백   B   나   350   340   377   392  1459
8   핸드백   C   다   365   383   308   323  1379
합계  핸드백  전체  전체  1100  1039  1040  1046  4225
'''