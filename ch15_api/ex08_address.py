import xmltodict
import requests

# 자신의 인증키를 복사해서 입력합니다.
API_KEY = 'Nthm35khfZR6DRDqGytWeSGTeOWEmKBf293ItGFcZHOP%2BDHWzPGpb4bAnsLTfCSSfhwbCyhaaMFm%2FR7uuhIyRw%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)
print(API_KEY_decode)


req_url = "http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd"

search_Se = "road"
srch_wrd = "반포대로 201"

req_parameter = {"ServiceKey": API_KEY_decode,
                 "searchSe": search_Se, "srchwrd": srch_wrd}

r = requests.get(req_url, params=req_parameter)
xml_data = r.text
print(xml_data)


dict_data = xmltodict.parse(xml_data)
print(dict_data)


adress_list = dict_data['NewAddressListResponse']['newAddressListAreaCd']

print("[입력한 도로명 주소]", srch_wrd)
print("[응답 데이터에서 추출한 결과]")
print("- 우편번호:", adress_list['zipNo'])
print("- 도로명 주소:", adress_list['lnmAdres'])
print("- 지번 주소:", adress_list['rnAdres'])
