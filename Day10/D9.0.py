import glob
import requests
import json
import pprint
import ssl
import urllib3



from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    #return sorted(all_pr['processes'],key=lambda x: x['memory-used'],reverse=true) #доделать 2 надо сделать, чтоб выводились только самые ёмкие 10 процессов
    return all_pr

from urllib3.poolmanager import PoolManager
from requests.adapters import HTTPAdapter

class Ssl1HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=ssl.PROTOCOL_TLSv1)

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'

s = requests.Session()
s.mount("https://10.31.70.210:55443", Ssl1HttpAdapter())


host_ip='https://10.31.70.210:55443'
login = 'restapi'
password = 'j0sg1280-7@'
api_url = '/api/v1/global/memory/processes'

r = s.post(host_ip + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = s.get(host_ip + '/api/v1/global/memory/processes', headers=header, verify=False)
#pprint.pprint(r.json())
#all_pr=r.json()['processes'] #доделать 1
all_pr=r.text

#sorted(all_pr['processes'],key=lambda x: x['memory-used'],reverse=true)[0:10]



#print(all_pr)

if __name__ == '__main__':
    app.run(debug=True)
