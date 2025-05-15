import requests
import json

url = "http://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060"

zip = input("郵便番号を入力＝＞")

param = {"zipcode": zip}

res = requests.get(url, param)

data = json.loads(res.text)

print(data)

print('*'*50)

if data['results'] is not None:
    address_indo = data['results'][0]
    
    zipcode = address_indo['zipcode']
    
    address = f"{address_indo['address1']}{address_indo['address2']}{address_indo['address3']}"
    print(f"郵便番号：{zipcode } 住所：{address}")
else:
    
    print("郵便番号が見つかりませんでした。")