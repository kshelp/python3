import json

python_dict = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}

print(type(python_dict))
# <class 'dict'>

json_data = json.dumps(python_dict)
print(type(json_data))
# <class 'str'>
print(json_data)
'''
{"\uc774\ub984": "\ud64d\uae38\ub3d9", "\ub098\uc774": 25, "\uac70\uc8fc\uc9c0": "\uc11c\uc6b8", "\uc2e0\uccb4\uc815\ubcf4": {"\ud0a4": 175.4, "\ubab8\ubb34\uac8c": 71.2}, "\ucde8\ubbf8": ["\ub4f1\uc0b0", "\uc790\uc804\uac70\ud0c0\uae30", "\ub3c5\uc11c"]}
'''

json_data = json.dumps(python_dict, indent=3, sort_keys=True, ensure_ascii=False)
print(json_data)
'''
{
   "거주지": "서울",
   "나이": 25,
   "신체정보": {
      "몸무게": 71.2,
      "키": 175.4
   },
   "이름": "홍길동",
   "취미": [
      "등산",
      "자전거타기",
      "독서"
   ]
}
'''

json_dict = json.loads(json_data)
print(type(json_dict))
# <class 'dict'>

print(json_dict['신체정보']['몸무게'])
# 71.2

print(json_dict['취미'])
# ['등산', '자전거타기', '독서']

print(json_dict['취미'][0])
# 등산
