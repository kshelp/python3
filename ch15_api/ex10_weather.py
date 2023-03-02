# 날씨 실황 조회
import datetime
import json
import requests

# 자신의 인증키를 복사해서 입력합니다.
API_KEY = 'Nthm35khfZR6DRDqGytWeSGTeOWEmKBf293ItGFcZHOP%2BDHWzPGpb4bAnsLTfCSSfhwbCyhaaMFm%2FR7uuhIyRw%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)
print(API_KEY_decode)


# [날짜 및 시간 설정]
now = datetime.datetime.now()  # 현재 날짜 및 시간 반환

# baseDate에 날짜를 입력하기 위해 날짜를 출력 형식을 지정해 변수에 할당
date = "{:%Y%m%d}".format(now)

# baseTime에 시간(정시)를 입력하기 위해 출력 형식을 지정해 시간만 변수에 할당
time = "{:%H00}".format(now)

# 현재 분이 30분 이전이면 이전 시간(정시)을 설정
if (now.minute >= 30):
    time = "{0}00".format(now.hour)
else:
    time = "{0}00".format(now.hour-1)

# [요청 주소 및 요청 변수 지정]
req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

baseDate = date  # 발표 일자 지정
baseTime = time  # 발표 시간 지정(정시로 지정)

nx_val = 60  # 예보지점 X 좌표(서울시 종로구 사직동)
ny_val = 127  # 예보지점 Y 좌표(서울시 종로구 사직동)

num_of_rows = 10  # 한 페이지에 포함된 결과 수
page_no = 1  # 페이지 번호

output_type = "JSON"  # 응답 데이터 형식 지정

req_parameter = {"ServiceKey": API_KEY_decode,
                 "nx": nx_val, "ny": ny_val,
                 "base_date": baseDate, "base_time": baseTime,
                 "pageNo": page_no, "numOfRows": num_of_rows,
                 "dataType": output_type}

# [데이터 요청]
r = requests.get(req_url, params=req_parameter)
#print(r.url)

# [JSON 형태로 응답받은 데이터를 딕셔너리 데이터로 변환]
dict_data = r.json()
#print(dict_data)


# [딕셔너리 데이터를 분석해서 원하는 값을 추출]

weather_items = dict_data['response']['body']['items']['item']

print("[ 발표 날짜: {} ]".format(weather_items[0]['baseDate']))
print("[ 발표 시간: {} ]".format(weather_items[0]['baseTime']))

for k in range(len(weather_items)):
    weather_item = weather_items[k]
    obsrValue = weather_item['obsrValue']
    if(weather_item['category'] == 'T1H'):
        print("* 기온: {} [℃]".format(obsrValue))
    elif(weather_item['category'] == 'REH'):
        print("* 습도: {} [%]".format(obsrValue))
    elif(weather_item['category'] == 'RN1'):
        print("* 1시간 강수량: {} [mm]".format(obsrValue))
'''
[ 발표 날짜: 20211126 ]
[ 발표 시간: 1500 ]
* 습도: 68 [%]
* 1시간 강수량: 0 [mm]
* 기온: 4.9 [℃]
'''


# 일기 예보 조회

# [날짜 및 시간 설정]
now = datetime.datetime.now()  # 현재 날짜 및 시간 반환

# baseDate에 날짜를 입력하기 위해 날짜를 출력 형식을 지정해 변수에 할당
date = "{:%Y%m%d}".format(now)

# baseTime에 시각(정시)을 입력하기 위해 출력 형식을 지정해 시간만 변수에 할당
time = "{:%H00}".format(now)

# 현재 분이 30분 이전이면 이전 시간(정시)을 설정
if (now.minute >= 30):
    time = "{0}00".format(now.hour)
else:
    time = "{0}00".format(now.hour-1)


# [요청 주소 및 요청 변수 지정]
# req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst"
req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"

baseDate = date  # 발표 일자 지정
baseTime = time  # time  # 발표 시간 지정(정시로 지정)

nx_val = 60  # 예보지점 X 좌표(서울시 종로구 사직동)
ny_val = 127  # 예보지점 Y 좌표(서울시 종로구 사직동)

num_of_rows = 30  # 한 페이지에 포함된 결과 수
page_no = 1  # 페이지 번호

output_type = "json"  # 응답 데이터 형식 지정

req_parameter = {"ServiceKey": API_KEY_decode,
                 "nx": nx_val, "ny": ny_val,
                 "base_date": baseDate, "base_time": baseTime,
                 "pageNo": page_no, "numOfRows": num_of_rows,
                 "dataType": output_type}

# [데이터 요청]
r = requests.get(req_url, params=req_parameter)
print("*******************")
print(r.url)

# [JSON 형태로 응답받은 데이터를 딕셔너리 데이터로 변환]
dict_data = r.json()

# [딕셔너리 데이터를 분석해서 원하는 값을 추출]
weather_items = dict_data['response']['body']['items']['item']

sky_cond = ["맑음", "구름 조금", "구름 많음", "흐림"]
rain_type = ["없음", "비", "비/눈", "눈", "소나기", "빗방울", "빗방울/눈날림", "눈날림"]

print("[ 발표 날짜: {} ]".format(weather_items[0]['baseDate']))
print("[ 발표 시각: {} ]".format(weather_items[0]['baseTime']))

print("[ 초단기 일기 예보 ]")

for k in range(len(weather_items)):
    weather_item = weather_items[k]

    fcstTime = weather_item['fcstTime']
    fcstValue = weather_item['fcstValue']

    if(weather_item['category'] == 'T1H'):
        print("* 시각: {0}, 기온: {1} [℃]".format(fcstTime, fcstValue))
    elif(weather_item['category'] == 'REH'):
        print("* 시각: {0}, 습도: {1} [%]".format(fcstTime, fcstValue))
    elif(weather_item['category'] == 'SKY'):
        print("* 시각: {0}, 하늘 상태: {1}".format(fcstTime,
                                             sky_cond[int(fcstValue)-1]))
    elif(weather_item['category'] == 'PTY'):
        print("* 시각: {0}, 강수 형태: {1}".format(fcstTime,
                                             rain_type[int(fcstValue)]))
    elif(weather_item['category'] == 'RN1'):
        print("* 시각: {0}, 1시간 강수량: {1} [mm]".format(fcstTime, fcstValue))
