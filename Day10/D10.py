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
    return "Hello, World!"

@app.route('/page1')
def page1():
    return "Если вы это читаете, \
                     вы что-то знаете :)"

@app.route('/configs')
def configs():
    List = glob.glob('C:\\Users\\ev.golubyatnik\\Downloads\\config_files\\config_files\\*.txt')
    d_id = 'hostname '
    hosts=''
    for name in List:
        with open(name) as f: #открываем файл в f
            for List in f: #Цикл для построчного прохождения файла txt
                if d_id in List: #если в строке есть d_id
                    hosts+=List
        return(hosts)


host_ip='https://10.31.70.210:55443'
login = 'restapi'
password = 'j0sg1280-7@'
api_url = '/api/v1/global/memory/processes'

r = requests.post(host_ip + '/api/v1/auth/token-services', auth=('restapi', 'j0sg1280-7@'), verify=False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(host_ip + '/api/v1/interfaces/GigabitEthernet1/statistics', headers=header, verify=False)
pprint.pprint(r.json())






print(r)




if __name__ == '__main__':
    app.run(debug=True)

