# 1. 수집된 데이터 파일의 구조 분석
from datetime import datetime
import os
import pandas as pd
import glob
data_file = './ch19_project/seoul_expense/2017/201701_expense_list.csv'

with open(data_file, encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    print(line1)
    print(line2)
    print(line3)
'''
nid,title,url,dept_nm_lvl_1,dept_nm_lvl_2,dept_nm_lvl_3,dept_nm_lvl_4,dept_nm_lvl_5,exec_yr,exec_month,
expense_budget,expense_execution,category,dept_nm_full,exec_dt,exec_loc,exec_purpose,target_nm,payment_method,exec_amount

11430252,"2017년 1월 장애인복지정책과 업무추진비 집행내역",http://opengov.seoul.go.kr/public/11430252,서
울시본청,복지본부,장애인복지정책과,,,2017,1,,,,"복지본부 장애인복지정책과","2017-01-26 13:10","동해일식 
(중구 무교동)","기본소득과 장애인복지 논의간담회","장애인복지정책팀장 외 2명",카드,76000

11430252,"2017년 1월 장애인복지정책과 업무추진비 집행내역",http://opengov.seoul.go.kr/public/11430252,서
울시본청,복지본부,장애인복지정책과,,,2017,1,,,,"복지본부 장애인복지정책과","2017-01-25 22:41","김앤장 ( 
중구 무교로)","장애인단체 활동지원 논의간담회","장애인복지정책과장 외 3명",카드,102000

'''


line1_len = len(line1.split(','))
line2_len = len(line2.split(','))
line3_len = len(line3.split(','))

print("[각 줄의 데이터값의 개수]")
print("첫째 줄:{}, 둘째 줄:{}, 셋째 줄:{}".format(line1_len, line2_len, line3_len))
'''
[각 줄의 데이터값의 개수]
첫째 줄:20, 둘째 줄:20, 셋째 줄:20
'''


def get_value_count(line):

    line_rep_list = []
    for k, x in enumerate(line.split('"')):
        if(k % 2 != 0):
            x = x.replace(',', '')
        line_rep_list.append(x)

    line_rep_str = ''.join(line_rep_list)

    return len(line_rep_str.split(','))


line1_len = get_value_count(line1)
line2_len = get_value_count(line2)
line3_len = get_value_count(line3)

print("[각 줄의 데이터값의 개수]")
print("첫째 줄:{}, 둘째 줄:{}, 셋째 줄:{}".format(line1_len, line2_len, line3_len))
'''
[각 줄의 데이터값의 개수]
첫째 줄:20, 둘째 줄:20, 셋째 줄:20
'''


# 2. 첫 번째 줄의 열 이름과 개수 변경
def change_csv_file_first_line_value(old_file_name, new_file_name):
    with open(old_file_name, encoding='utf-8') as f:  # 파일을 읽기 모드로 열기
        # 전체 데이터를 읽어서 한 줄씩 lines 리스트의 각 요소에 할당
        lines = f.read().splitlines()

    # 첫째 줄의 내용을 변경할 열 이름을 지정해서 변경
    lines[0] = 'nid,제목,url,부서레벨1,부서레벨2,부서레벨3,부서레벨4,부서레벨5,\
집행연도,집행월,예산,집행,구분,부서명,집행일시,집행장소,집행목적,대상인원,결제방법,집행금액'

    with open(new_file_name, 'w', encoding='utf-8') as f:  # 파일을 쓰기 모드로 열기
        # 리스트 내의 각 요소를 개행문자(\n)로 연결해서 파일로 저장
        f.write('\n'.join(lines))


# 기존의 파일
old_file_name = './ch19_project/seoul_expense/2017/201701_expense_list.csv'

# 새로운 파일
new_file_name = './ch19_project/seoul_expense/2017/201701_expense_list_new.csv'

# 첫째 줄의 내용을 변경한 새로운 파일 생성
change_csv_file_first_line_value(old_file_name, new_file_name)


with open(new_file_name, encoding='utf-8') as f:  # 파일을 읽기 모드로 열기
    for k in range(3):
        print(f.readline())
'''
nid,제목,url,부서레벨1,부서레벨2,부서레벨3,부서레벨4,부서레벨5,집행연도,집행월,예산,집행,구분,부서명,집행일시
,집행장소,집행목적,대상인원,결제방법,집행금액

11430252,"2017년 1월 장애인복지정책과 업무추진비 집행내역",http://opengov.seoul.go.kr/public/11430252,서울시 
본청,복지본부,장애인복지정책과,,,2017,1,,,,"복지본부 장애인복지정책과","2017-01-26 13:10","동해일식 (중구 무 
교동)","기본소득과 장애인복지 논의간담회","장애인복지정책팀장 외 2명",카드,76000

11430252,"2017년 1월 장애인복지정책과 업무추진비 집행내역",http://opengov.seoul.go.kr/public/11430252,서울시 
본청,복지본부,장애인복지정책과,,,2017,1,,,,"복지본부 장애인복지정책과","2017-01-25 22:41","김앤장 (중구 무교 
로)","장애인단체 활동지원 논의간담회","장애인복지정책과장 외 3명",카드,102000

'''


# 인자: 연도, 데이터 파일이 있는 폴더
def change_year_csv_file_first_line_value(year, data_folder):

    # 데이터 파일이 있는 폴더 지정
    # ex) 'C:/myPyCode/data/seoul_expense/2017/'
    expense_list_year_dir = data_folder + str(year) + '/'

    extension = 'csv'  # 확장자 이름

    # 지정한 폴더에 있는 월별 업무추진비 파일에서 첫 번째 줄의 열 이름을 변경
    for k in range(12):
        # 기존의 파일 이름 지정
        old_file_name = expense_list_year_dir + \
            '{0}{1:02d}_expense_list.{2}'.format(year, k+1, extension)

        # 새로운 파일 이름 지정
        new_file_name = expense_list_year_dir + \
            '{0}{1:02d}_expense_list_new.{2}'.format(year, k+1, extension)

        # 첫째 줄의 내용을 변경한 새로운 파일 생성
        change_csv_file_first_line_value(old_file_name, new_file_name)


data_folder = './ch19_project/seoul_expense/'

years = [2017, 2018, 2019]  # 연도를 지정

for year in years:
    print("{}년 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일에 저장합니다.".format(year))
    change_year_csv_file_first_line_value(year, data_folder)

print("모든 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일로 저장했습니다.")
'''
2017년 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일에 저장합니다.
2018년 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일에 저장합니다.
2019년 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일에 저장합니다.
모든 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일로 저장했습니다.
'''


data_folder = './ch19_project/seoul_expense/'

years = [2017, 2018, 2019]  # 연도를 지정

for year in years:
    path_name = data_folder + str(year)  # 폴더명을 지정
    print("[폴더 이름]", path_name)  # 폴더명 출력

    new_csv_files = []

    # 지정 폴더에서 파일명에 _new.csv가 포함된 파일만 지정
    file_name_for_glob = path_name + "/*_new.csv"

    for new_csv_file in glob.glob(file_name_for_glob):
        # 반환값에서 폴더는 제거하고 파일 이름만 추출
        new_csv_files.append(new_csv_file.split("\\")[-1])

    print("* 새롭게 생성된 CSV 파일:", new_csv_files)
'''
[폴더 이름] ./ch19_project/seoul_expense/2017
* 새롭게 생성된 CSV 파일: ['201701_expense_list_new.csv', '201702_expense_list_new.csv', '201703_expense_list_new.csv', '201704_expense_list_new.csv', '201705_expense_list_new.csv', '201706_expense_list_new.csv', '201707_expense_list_new.csv', '201708_expense_list_new.csv', '201709_expense_list_new.csv', '201710_expense_list_new.csv', '201711_expense_list_new.csv', '201712_expense_list_new.csv']
[폴더 이름] ./ch19_project/seoul_expense/2018
* 새롭게 생성된 CSV 파일: ['201801_expense_list_new.csv', '201802_expense_list_new.csv', '201803_expense_list_new.csv', '201804_expense_list_new.csv', '201805_expense_list_new.csv', '201806_expense_list_new.csv', '201807_expense_list_new.csv', '201808_expense_list_new.csv', '201809_expense_list_new.csv', '201810_expense_list_new.csv', '201811_expense_list_new.csv', '201812_expense_list_new.csv']
[폴더 이름] ./ch19_project/seoul_expense/2019
* 새롭게 생성된 CSV 파일: ['201901_expense_list_new.csv', '201902_expense_list_new.csv', '201903_expense_list_new.csv', '201904_expense_list_new.csv', '201905_expense_list_new.csv', '201906_expense_list_new.csv', '201907_expense_list_new.csv', '201908_expense_list_new.csv', '201909_expense_list_new.csv', '201910_expense_list_new.csv', '201911_expense_list_new.csv', '201912_expense_list_new.csv']
'''


# 3. 데이터의 구조 및 결측시 살펴보기
expense_list2016_dir = './ch19_project/seoul_expense/2017/'
file_name = "201701_expense_list_new.csv"

df = pd.read_csv(expense_list2016_dir + file_name)
print(df.head(2))
'''
        nid                            제목  ... 결제방법    집행금액
0  11430252  2017년 1월 장애인복지정책과 업무추진비 집행내역  ...   카드   76000
1  11430252  2017년 1월 장애인복지정책과 업무추진비 집행내역  ...   카드  102000

[2 rows x 20 columns]
'''


year = 2017
expense_list_year_dir = './ch19_project/seoul_expense/' + str(year) + '/'

df_year = pd.DataFrame()
for k in range(12):

    # 파일 이름 지정
    file_name = "{0}{1:02d}_expense_list_new.csv".format(year, k+1)

    # pandas DataFrame 형식으로 csv 데이터 불러오기
    df_month = pd.read_csv(expense_list_year_dir + file_name)

    # df_year에 df_month를 세로 방향으로 추가해서 다시 df_year에 할당
    # 통합된 dataFrame의 순서대로 index를 할당하기 위해서 `ignore_index = True` 옵션 지정
    df_year = df_year.append(df_month, ignore_index=True)

print(df_year.head(2))
'''
        nid                            제목  ... 결제방법    집행금액
0  11430252  2017년 1월 장애인복지정책과 업무추진비 집행내역  ...   카드   76000
1  11430252  2017년 1월 장애인복지정책과 업무추진비 집행내역  ...   카드  102000

[2 rows x 20 columns]
'''

print(df_year.tail(2))
'''
            nid                               제목  ... 결제방법    집행금액
70130  14292506  2017년 12월 사업소_은평병원_원무과 업무추진비 내역  ...   카드  820000
70131  14292506  2017년 12월 사업소_은평병원_원무과 업무추진비 내역  ...   카드  440000

[2 rows x 20 columns]
'''

print(df_year.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 70132 entries, 0 to 70131
Data columns (total 20 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   nid     70132 non-null  int64
 1   제목      70132 non-null  object
 2   url     70132 non-null  object
 ...(생략)...
 18  결제방법    69929 non-null  object
 19  집행금액    70132 non-null  int64
dtypes: float64(2), int64(4), object(14)
memory usage: 10.7+ MB
None
'''

print(df_year.isna().sum())
'''
nid          0
제목           0
url          0
부서레벨1        0
부서레벨2       58
...(생략)...
결제방법       203
집행금액         0
dtype: int64
'''


df_year_drop = df_year.drop(columns=['nid', 'url', '부서레벨3', '부서레벨4', '부서레벨5',
                                     '예산', '집행', '구분'])
print(df_year_drop.head(2))
'''
                             제목  부서레벨1 부서레벨2  집행연도  ...               집행목적            대상
인원 결제방법    집행금액
0  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017  ...  기본소득과 장애인복지 논
의간담회  장애인복지정책팀장 외 2명   카드   76000
1  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017  ...   장애인단체 활동지원 논 
의간담회  장애인복지정책과장 외 3명   카드  102000

[2 rows x 12 columns]
'''


year = 2017
expense_list_year_dir = './ch19_project/seoul_expense/' + str(year) + '/'

expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)
df_year_drop.to_csv(expense_list_year_dir +
                    expense_list_tidy_file, index=False)


file_name = expense_list_year_dir + expense_list_tidy_file
print(file_name)
os.path.isfile(file_name)


def select_columns_save_file(year, data_folder, drop_columns_list):

    expense_list_year_dir = data_folder + str(year) + '/'
    expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)
    df_year = pd.DataFrame()

    for k in range(12):
        # 파일 이름 지정
        file_name = "{0}{1:02d}_expense_list_new.csv".format(year, k+1)

        # aDtaFrame 형식으로 csv 데이터 불러오기
        df_month = pd.read_csv(expense_list_year_dir + file_name)

        # fd_year에 df_month를 새로 추가해서 다시 df_year에 할당
        # 통합된 adtaFrame의 순서대로 index를 할당하기 위해서 `ignore_index = True` 옵션 지정
        df_year = df_year.append(df_month, ignore_index=True)

    df_year_drop = df_year.drop(columns=drop_columns_list)
    new_file_name = expense_list_year_dir + expense_list_tidy_file
    df_year_drop.to_csv(new_file_name, index=False)

    print("==> {} 파일을 생성했습니다.".format(expense_list_tidy_file))


data_folder = './ch19_project/seoul_expense/'
years = [2017, 2018, 2019]
drop_columns_list = ['nid', 'url', '부서레벨3', '부서레벨4', '부서레벨5', '예산', '집행', '구분']

for year in years:
    print("{}년 데이터를 정리해서 저장하고 있습니다.".format(year))
    select_columns_save_file(year, data_folder, drop_columns_list)
print("모든 연도의 데이터를 정리해서 파일로 저장했습니다.")
'''
./ch19_project/seoul_expense/2017/2017_expense_list_tidy.csv
2017년 데이터를 정리해서 저장하고 있습니다.
==> 2017_expense_list_tidy.csv 파일을 생성했습니다.
2018년 데이터를 정리해서 저장하고 있습니다.
==> 2018_expense_list_tidy.csv 파일을 생성했습니다.
2019년 데이터를 정리해서 저장하고 있습니다.
==> 2019_expense_list_tidy.csv 파일을 생성했습니다.
모든 연도의 데이터를 정리해서 파일로 저장했습니다.
'''

years = [2017, 2018, 2019]

for year in years:

    expense_list_year_dir = data_folder + str(year) + '/'
    expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)

    file_name = expense_list_year_dir + expense_list_tidy_file
    print(file_name, "==> ", end="")
    print(os.path.isfile(file_name))


def get_file_info(year, data_folder):
    expense_list_year_dir = data_folder + str(year) + '/'
    expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)

    path_file_name = expense_list_year_dir + expense_list_tidy_file
    print(path_file_name)
    result = os.path.isfile(path_file_name)

    # 파일 수정 시간
    modified_time = datetime.fromtimestamp(os.path.getmtime(path_file_name))

    # 파일 생성 시간
    created_time = datetime.fromtimestamp(os.path.getctime(path_file_name))

    # 파일 크기
    file_size = os.path.getsize(path_file_name)

    if(result == True):
        print("[생성한 CSV 데이터 파일의 정보]")
        print('* 폴더 위치 :', expense_list_year_dir)
        print('* 파일 이름 :', expense_list_tidy_file)
        print('* 수정 시간 :', modified_time.strftime('%Y-%m-%d %H:%M:%S'))
        print('* 생성 시간 :', created_time.strftime('%Y-%m-%d %H:%M:%S'))
        print('* 파일 크기 : {0:,} 바이트'.format(file_size))


data_folder = './ch19_project/seoul_expense/'
years = [2017, 2018, 2019]

for year in years:

    get_file_info(year, data_folder)
    print("")
'''
[생성한 CSV 데이터 파일의 정보]
* 폴더 위치 : ./ch19_project/seoul_expense/2017/
* 파일 이름 : 2017_expense_list_tidy.csv
* 수정 시간 : 2021-11-21 11:22:37
* 생성 시간 : 2021-11-20 23:27:26
* 파일 크기 : 21,505,565 바이트

./ch19_project/seoul_expense/2018/2018_expense_list_tidy.csv
[생성한 CSV 데이터 파일의 정보]
* 폴더 위치 : ./ch19_project/seoul_expense/2018/
* 파일 이름 : 2018_expense_list_tidy.csv
* 수정 시간 : 2021-11-21 11:22:38
* 생성 시간 : 2021-11-20 23:32:30
* 파일 크기 : 23,012,590 바이트

./ch19_project/seoul_expense/2019/2019_expense_list_tidy.csv
[생성한 CSV 데이터 파일의 정보]
* 폴더 위치 : ./ch19_project/seoul_expense/2019/
* 파일 이름 : 2019_expense_list_tidy.csv
* 수정 시간 : 2021-11-21 11:22:39
* 생성 시간 : 2021-11-20 23:32:31
* 파일 크기 : 24,459,405 바이트
'''
