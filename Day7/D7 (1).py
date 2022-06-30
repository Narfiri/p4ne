import glob

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



if __name__ == '__main__':
    app.run(debug=True)

