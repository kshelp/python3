import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

sales = {'시간': [9, 10, 11, 12, 13, 14, 15],
         '제품1': [10, 15, 12, 11, 12, 14, 13],
         '제품2': [9, 11, 14, 12, 13, 10, 12]}

df = pd.DataFrame(sales, index=sales['시간'], columns=['제품1', '제품2'])
df.index.name = '시간'  # index 라벨 추가

print(df)
'''
    제품1  제품2
시간
9    10    9
10   15   11
11   12   14
12   11   12
13   12   13
14   14   10
15   13   12
'''


matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

product_plot = df.plot(grid=True, style=['-*', '-o'], title='시간대별 생산량')
product_plot.set_ylabel("생산량")

image_file = './ch16_excel/fig_for_excel1.png'  # 이미지 파일 경로 및 이름
plt.savefig(image_file, dpi=400)  # 그래프를 이미지 파일로 저장

plt.show()


import pandas as pd

# (1) pandas의 ExcelWriter 객체 생성
excel_file = './ch16_excel/data_image_to_excel.xlsx'
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

# (2) DataFrame 데이터를 지정된 엑셀 시트(Sheet)에 쓰기
df.to_excel(excel_writer, index=True, sheet_name='Sheet1')

# (3) ExcelWriter 객체에서 워크시트(worksheet) 객체 생성
worksheet = excel_writer.sheets['Sheet1']

# (4) 워크시트에 차트가 들어갈 위치를 지정해 이미지 넣기
worksheet.insert_image('D2', image_file, {'x_scale': 0.7, 'y_scale': 0.7})
# worksheet.insert_image(1, 3, image_file, {'x_scale': 0.7, 'y_scale': 0.7})

# (5) ExcelWriter 객체를 닫고 엑셀 파일 출력
excel_writer.save()