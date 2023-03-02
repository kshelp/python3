import pandas as pd

excel_exam_data1 = {'학생': ['A', 'B', 'C', 'D', 'E', 'F'],
                    '국어': [80, 90, 95, 70, 75, 85],
                    '영어': [90, 95, 70, 85, 90, 95],
                    '수학': [85, 95, 75, 80, 85, 100]}
df1 = pd.DataFrame(excel_exam_data1, columns=['학생', '국어', '영어', '수학'])
print(df1)
'''
  학생  국어  영어   수학
0  A  80  90   85        
1  B  90  95   95
2  C  95  70   75
3  D  70  85   80
4  E  75  90   85
5  F  85  95  100
'''

excel_writer = pd.ExcelWriter('./ch16_excel/학생시험성적2.xlsx', engine='xlsxwriter')
df1.to_excel(excel_writer, index=False)
excel_writer.save()

excel_writer2 = pd.ExcelWriter(
    './ch16_excel/학생시험성적3.xlsx', engine='xlsxwriter')
df1.to_excel(excel_writer2, index=False, sheet_name='중간고사')
excel_writer2.save()

excel_exam_data2 = {'학생': ['A', 'B', 'C', 'D', 'E', 'F'],
                    '국어': [85, 95, 75, 80, 85, 100],
                    '영어': [80, 90, 95, 70, 75, 85],
                    '수학': [90, 95, 70, 85, 90, 95]}
df2 = pd.DataFrame(excel_exam_data2, columns=['학생', '국어', '영어', '수학'])
print(df2)
'''
  학생   국어  영어  수학
0  A   85  80  90
1  B   95  90  95
2  C   75  95  70
3  D   80  70  85
4  E   85  75  90
5  F  100  85  95
'''

excel_writer3 = pd.ExcelWriter(
    './ch16_excel/학생시험성적4.xlsx', engine='xlsxwriter')
df1.to_excel(excel_writer3, index=False, sheet_name='중간고사')
df2.to_excel(excel_writer3, index=False, sheet_name='기말고사')
excel_writer3.save()
