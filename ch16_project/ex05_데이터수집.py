# 데이터 수집
import glob
import requests
import os
import pathlib

#인자: 확장자, 연도, 내려받을 폴더


def get_seoul_expense_list(extension, year, data_folder):

    # 깃허브의 데이터 위치 지정
    # ex) 'https://github.com/seoul-opengov/opengov/raw/master/expense_list2017/'
    expense_list_year_url = 'https://github.com/seoul-opengov/opengov/raw/master/expense_list' + \
        str(year) + '/'

    # 데이터를 내려받을 폴더 지정
    # ex) 'C:/myPyCode/data/seoul_expense/2017/'
    expense_list_year_dir = data_folder + str(year) + '/'

    # 내려받을 폴더가 없다면 폴더 생성
    if(os.path.isdir(expense_list_year_dir)):
        print("데이터 폴더({0})가 이미 있습니다. {0}년 데이터의 다운로드를 시작합니다.".format(year))
    else:
        print("데이터 폴더({0})가 없어서 생성했습니다. {0}년 데이터의 다운로드를 시작합니다.".format(year))
        # 폴더 생성
        pathlib.Path(expense_list_year_dir).mkdir(parents=True, exist_ok=True)

    # 지정한 폴더로 1월 ~ 12월 업무추진비 파일을 다운로드
    for k in range(12):
        file_name = '{0}{1:02d}_expense_list.{2}'.format(year, k+1, extension)
        url = expense_list_year_url + file_name
        print(url)
        r = requests.get(url)
        with open(expense_list_year_dir + file_name, 'wb') as f:
            f.write(r.content)


# 내려받을 업무추진비 데이터의 파일 형식을 지정
extension = "csv"

# 내려받을 업무추진비 데이터의 연도를 지정
year = 2017

# 내려받을 업무추진비 데이터의 폴더를 지정
data_folder = './ch19_project/seoul_expense/'

# 함수를 실행
get_seoul_expense_list(extension, year, data_folder)


path_name = './ch19_project/seoul_expense/2017/'  # 폴더 이름

# 지정 폴더에서 파일명에 list.csv가 포함된 파일만 지정
file_name_for_glob = path_name + "*list.csv"

csv_files = []
for csv_file in glob.glob(file_name_for_glob):
    # 반환값에서 폴더는 제거하고 파일 이름만 추출
    csv_files.append(csv_file.split("\\")[-1])

print("[폴더 이름]", path_name)  # 폴더명 출력
print("* CSV 파일:", csv_files)
'''
[폴더 이름] ./ch19_project/seoul_expense/2017/
* CSV 파일: ['201701_expense_list.csv', '201702_expense_list.csv', '201703_expense_list.csv', '201704_expense_list.csv', '201705_expense_list.csv', '201706_expense_list.csv', '201707_expense_list.csv', '201708_expense_list.csv', '201709_expense_list.csv', '201710_expense_list.csv', '201711_expense_list.csv', '201712_expense_list.csv']
'''


data_folder = './ch19_project/seoul_expense/'

years = [2017, 2018, 2019]  # 다운로드받을 연도를 지정

extension = "csv"
# extension = "xlsx"
# extension = "xml"

for year in years:
    get_seoul_expense_list(extension, year, data_folder)

print("모든 데이터를 다운로드 받았습니다.")


data_folder = './ch19_project/seoul_expense/'

years = [2017, 2018, 2019]  # 다운로드받을 연도를 지정

for year in years:
    path_name = data_folder + str(year) + "/"  # 연도별 폴더명을 지정

    # 지정 폴더에서 파일명에 list.csv가 포함된 파일만 지정
    file_name_for_glob = path_name + "*list.csv"

    csv_files = []
    for csv_file in glob.glob(file_name_for_glob):
        # 반환값에서 폴더는 제거하고 파일명만 추출
        csv_files.append(csv_file.split("\\")[-1])

    print("[폴더 이름]", path_name)  # 폴더명 출력
    print("* CSV 파일:", csv_files)
'''
[폴더 이름] ./ch19_project/seoul_expense/2017/
* CSV 파일: ['201701_expense_list.csv', '201702_expense_list.csv', '201703_expense_list.csv', '201704_expense_list.csv', '201705_expense_list.csv', '201706_expense_list.csv', '201707_expense_list.csv', '201708_expense_list.csv', '201709_expense_list.csv', '201710_expense_list.csv', '201711_expense_list.csv', '201712_expense_list.csv']
[폴더 이름] ./ch19_project/seoul_expense/2018/
* CSV 파일: ['201801_expense_list.csv', '201802_expense_list.csv', '201803_expense_list.csv', '201804_expense_list.csv', '201805_expense_list.csv', '201806_expense_list.csv', '201807_expense_list.csv', '201808_expense_list.csv', '201809_expense_list.csv', '201810_expense_list.csv', '201811_expense_list.csv', '201812_expense_list.csv']
[폴더 이름] ./ch19_project/seoul_expense/2019/
* CSV 파일: ['201901_expense_list.csv', '201902_expense_list.csv', '201903_expense_list.csv', '201904_expense_list.csv', '201905_expense_list.csv', '201906_expense_list.csv', '201907_expense_list.csv', '201908_expense_list.csv', '201909_expense_list.csv', '201910_expense_list.csv', '201911_expense_list.csv', '201912_expense_list.csv']
'''
