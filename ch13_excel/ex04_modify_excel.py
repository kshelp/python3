import pandas as pd

df = pd.read_excel('./ch16_excel/담당자별_판매량_Andy사원.xlsx')
print(df)
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기
0   시계   A  가  198  123  120  137
1   구두   A  가  273  241  296  217
2  핸드백   A  가  385  316  355  331
'''

df.loc[2, '4분기'] = 0
print(df)
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기
0   시계   A  가  198  123  120  137
1   구두   A  가  273  241  296  217
2  핸드백   A  가  385  316  355    0
'''

df.loc[3, '제품명'] = '벨트'
df.loc[3, '담당자'] = 'A'
df.loc[3, '지역'] = '가'
df.loc[3, '1분기'] = 100
df.loc[3, '2분기'] = 150
df.loc[3, '3분기'] = 200
df.loc[3, '4분기'] = 250
print(df)
'''
   제품명 담당자 지역    1분기    2분기    3분기    4분기
0   시계   A  가  198.0  123.0  120.0  137.0
1   구두   A  가  273.0  241.0  296.0  217.0
2  핸드백   A  가  385.0  316.0  355.0    0.0
3   벨트   A  가  100.0  150.0  200.0  250.0
'''

df['담당자'] = 'Andy'
print(df)
'''
   제품명   담당자 지역    1분기    2분기    3분기    4분기
0   시계  Andy  가  198.0  123.0  120.0  137.0
1   구두  Andy  가  273.0  241.0  296.0  217.0
2  핸드백  Andy  가  385.0  316.0  355.0    0.0
3   벨트  Andy  가  100.0  150.0  200.0  250.0
'''

import glob
excel_file_name = './ch16_excel/담당자별_판매량_Andy사원_new.xlsx'

new_excel_file = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')
df.to_excel(new_excel_file, index=False)
new_excel_file.save()

print(glob.glob(excel_file_name))
# ['./ch16_excel/담당자별_판매량_Andy사원_new.xlsx']