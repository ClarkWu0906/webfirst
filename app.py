from flask import Flask, request, jsonify, render_template
import requests
import json
from json import load
import os
from werkzeug.utils import secure_filename
from flask import session
app = Flask(__name__)
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = '/home/pdclab/WebServe/webfirst/upfile'
ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(filename)
    url = "http://140.115.52.21:11135/upload"

    payload={}
    files=[
    ('file',(filename,open('/home/pdclab/WebServe/webfirst/upfile/'+filename,'rb'),'text/csv'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    
    return jsonify({'result': '上傳成功', 'filename': filename})


@app.route('/1G-POE')
def page2():
    return render_template('1G-POE.html')

@app.route('/options', methods=['POST'])
def options():
    selected_option = request.form['1G_option']
    if selected_option == 'option1':
        return render_template('1G_mode1.html')
    else:
        return "Invalid option"

@app.route('/finished', methods = ['POST', 'GET'])
def finished():
        datas =[2, 2, 3, 4]
        if request.method == 'POST':
            # url = "http://140.115.52.21:11135/test"
            # payload={}
            # headers = {}
            # response = requests.request("POST", url, headers=headers, data=payload)
            # print(response.text)
            return render_template('finished.html', data1 = datas)
        elif request.method == 'GET':
            return render_template('finished.html' , data1 = datas)


@app.route('/add',methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        return render_template('add.html')
    elif request.method == 'GET':
         return render_template('add.html')

from flask import session

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_id = str(request.form.get("search_id"))
        delete_id = request.form.get("delete_id")
        if search_id:
            print('search_id:', search_id)
            url = "http://140.115.52.21:11135/search"

            payload = json.dumps({
                                "id": search_id
                                })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            data = json.loads(response.text)
            return render_template('search.html', data=data)
        elif delete_id:
            print('delete_id:', delete_id)
            url = "http://140.115.52.21:11135/deleteorder"

            payload = json.dumps({
                                "id": delete_id
                                })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            data = json.loads(response.text)
            return render_template('search.html', message='Record deleted successfully.')
        else:
            return render_template('search.html')
    else:
        return render_template('search.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
