import requests

API_KEY = "et5piq3pfpqLEWPpCbvtSQ%2Bertertg%2Bx3evdvbaRBvhWEerg3efac2r3f3RfhDTERTw%2B9rkvoewRV%2Fovmrk3dq%3D%3D"

API_KEY_decode = requests.utils.unquote(API_KEY)

print("Encoded url:", API_KEY)
print("Decoded url:", API_KEY_decode)
'''
Encoded url: et5piq3pfpqLEWPpCbvtSQ%2Bertertg%2Bx3evdvbaRBvhWEerg3efac2r3f3RfhDTERTw%2B9rkvoewRV%2Fovmrk3dq%3D%3D
Decoded url: et5piq3pfpqLEWPpCbvtSQ+ertertg+x3evdvbaRBvhWEerg3efac2r3f3RfhDTERTw+9rkvoewRV/ovmrk3dq==
'''
