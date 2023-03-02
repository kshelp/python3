import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'   # '맑은 고딕'으로 설정
matplotlib.rcParams['axes.unicode_minus'] = False

grade_num = [5, 14, 12, 3]
students = ['A', 'B', 'C', 'D']

df_grade = pd.DataFrame(grade_num, index=students, columns=['Student'])
print(df_grade)
'''
   Student
A        5
B       14
C       12
D        3
'''

grade_bar = df_grade.plot.bar(grid=True)
grade_bar.set_xlabel("학점")
grade_bar.set_ylabel("학생수")
grade_bar.set_title("학점별 학생 수 막대 그래프")
plt.show()
