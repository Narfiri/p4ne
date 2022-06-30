import requests
import pprint
import ssl
import urllib3

heaers={'Accept-Version':'3'}

r = requests.get('https://lookup.binlist.net/42763801', headers=headers, verify=Fals)

#r=requests.get('https://rbc.ru')
#print(r.status_code)
#print(r.url)
#print(r.encoding)
#print(r.headers)
r.json()
ans=r.json()
ans['country']['name']
pprint.pprint(ans,indent=4)


url='https://10.31.70.209:55443'
name='restapi'
password='j0sg1280-7@'
r=requests.post(url+'/api/v1/auth/token-services')

