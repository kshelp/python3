import glob
import pandas as pd
excel_data_files = ['./ch16_excel/담당자별_판매량_Andy사원.xlsx',
                    './ch16_excel/담당자별_판매량_Becky사원.xlsx',
                    './ch16_excel/담당자별_판매량_Chris사원.xlsx']

total_data = pd.DataFrame()

for f in excel_data_files:
    df = pd.read_excel(f)
    total_data = total_data.append(df)

print(total_data)
'''
   제품명 담당자 지역  1분기  2분기  3분기  4분기
0   시계   A  가  198  123  120  137
1   구두   A  가  273  241  296  217
2  핸드백   A  가  385  316  355  331
0   시계   B  나  154  108  155  114
1   구두   B  나  200  223  213  202
2  핸드백   B  나  350  340  377  392
0   시계   C  다  168  102  149  174
1   구두   C  다  231  279  277  292
2  핸드백   C  다  365  383  308  323
'''

total_data = pd.DataFrame()

for f in excel_data_files:
    df = pd.read_excel(f)
    total_data = total_data.append(df, ignore_index=True)

print(total_data)
'''
제품명 담당자 지역  1분기  2분기  3분기  4분기
0   시계   A  가  198  123  120  137
1   구두   A  가  273  241  296  217
2  핸드백   A  가  385  316  355  331
3   시계   B  나  154  108  155  114
4   구두   B  나  200  223  213  202
5  핸드백   B  나  350  340  377  392
6   시계   C  다  168  102  149  174
7   구두   C  다  231  279  277  292
8  핸드백   C  다  365  383  308  323
'''


print(glob.glob("./ch16_excel/담당자별_판매량_*사원.xlsx"))
'''
['./ch16_excel\\담당자별_판매량_Andy사원.xlsx', './ch16_excel\\담당자별_판매량_Becky사
원.xlsx', './ch16_excel\\담당자별_판매량_Chris사원.xlsx']
'''


excel_data_files1 = glob.glob("./ch16_excel/담당자별_판매량_*사원.xlsx")
total_data1 = pd.DataFrame()

for f in excel_data_files1:
    df = pd.read_excel(f)
    total_data1 = total_data1.append(df, ignore_index=True)

print(total_data1)
'''
제품명 담당자 지역  1분기  2분기  3분기  4분기
0   시계   A  가  198  123  120  137
1   구두   A  가  273  241  296  217
2  핸드백   A  가  385  316  355  331
3   시계   B  나  154  108  155  114
4   구두   B  나  200  223  213  202
5  핸드백   B  나  350  340  377  392
6   시계   C  다  168  102  149  174
7   구두   C  다  231  279  277  292
8  핸드백   C  다  365  383  308  323
'''

excel_file_name = './ch16_excel/담당자별_판매량_통합.xlsx'

excel_total_file_writer = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')
total_data1.to_excel(excel_total_file_writer, index=False, sheet_name='담당자별_판매량_통합')
excel_total_file_writer.save()

print(glob.glob(excel_file_name))
# ['./ch16_excel/담당자별_판매량_통합.xlsx']