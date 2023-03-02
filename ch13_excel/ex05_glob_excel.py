import glob
import re
import pandas as pd

# 원하는 문자열이 포함된 파일을 검색해 리스트를 할당한다.
excel_data_files1 = glob.glob("./ch16_excel/담당자별_판매량_*사원.xlsx")

# 리스트에 있는 엑셀 파일만큼 반복 수행한다.
for f in excel_data_files1:
    # 엑셀 파일에서 DataFrame 형식으로 데이터 가져온다.
    df = pd.read_excel(f)

    # 특정 열의 값을 변경한다.
    if(df.loc[1, '담당자'] == 'A'):
        df['담당자'] = 'Andy'
    elif(df.loc[1, '담당자'] == 'B'):
        df['담당자'] = 'Becky'
    elif(df.loc[1, '담당자'] == 'C'):
        df['담당자'] = 'Chris'

    # 엑셀 파일 이름에서 지정된 문자열 패턴을 찾아서 파일명을 변경한다.
    f_new = re.sub(".xlsx", "2.xlsx", f)
    print(f_new)

    # 수정된 데이터를 새로운 이름의 엑셀 파일로 저장한다.
    new_excel_file = pd.ExcelWriter(f_new, engine='xlsxwriter')
    df.to_excel(new_excel_file, index=False)
    new_excel_file.save()


print(glob.glob("./ch16_excel/담당자별_판매량_*사원?.xlsx"))
'''
['./ch16_excel\\담당자별_판매량_Andy사원2.xlsx', './ch16_excel\\담당자별_판매량_Becky사원2.xlsx', './ch16_excel\\담당자별_판매량_Chris사원2.xlsx']
'''
