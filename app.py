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
@app.route('/10G_mode3', methods=['GET', 'POST'])
def tenG_mode3():
    if request.method == 'POST':
        option_10G_mode3 = request.form.get("option_10G_mode3")
        predict_date = request.form.get("10G_date_mode3")
        urll = "http://140.115.52.21:11135/"
        payloadd=""
        headerss = {}
        responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
        url = "http://140.115.52.21:11135/change"
        payload = json.dumps({
            "mode": 3,
            "start_date": predict_date
            })
        headers = {
                'Content-Type': 'application/json'
            }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        data = json.loads(response.text)
        if response.ok:
            return render_template('10G_mode3.html', option_10G_mode3 =option_10G_mode3, predict_date=predict_date, mode3_predict_data=data,message='計算完成')
        else:
            return render_template('10G_mode3.html',mode3_predict_data={})
    elif request.method == 'GET':
        return render_template('10G_mode3.html',mode3_predict_data={})
    return render_template('10G_mode3.html')

@app.route('/1G_mode3', methods=['GET', 'POST'])
def oneG_mode3():
    if request.method == 'POST':
        option_1G_mode3 = request.form.get("option_1G_mode3")
        predict_date = request.form.get("1G_date_mode3")
        urll = "http://140.115.52.21:11135/"
        payloadd=""
        headerss = {}
        responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
        url = "http://140.115.52.21:11135/change"
        payload = json.dumps({
            "mode": 3,
            "start_date": predict_date
            })
        headers = {
                'Content-Type': 'application/json'
            }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        data = json.loads(response.text)
        if response.ok:
            return render_template('1G_mode3.html', option_1G_mode3 =option_1G_mode3 ,predict_date=predict_date, mode3_predict_data=data,message='計算完成')
        else:
            return render_template('1G_mode3.html',mode3_predict_data={})
    elif request.method == 'GET':
        return render_template('1G_mode3.html',mode3_predict_data={})
    return render_template('1G_mode3.html')



@app.route('/1G-POE', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        option_1G = request.form.get("option_1G")
        predict_date = request.form.get("1G_date")
        print(option_1G)
        if option_1G == "mode1":
            print("hu")
            url = "http://140.115.52.21:11135/"
            payload=""
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            url = "http://140.115.52.21:11135/change"
            payload = json.dumps({
                "mode": 1,
                "start_date": predict_date
            })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response)
            print(response.text)
            data = json.loads(response.text)
            if response.ok:
                return render_template('1G-POE.html', option_1G=option_1G, predict_date=predict_date, predict_data=data,message='計算完成')
            else:
                return render_template('1G-POE.html',predict_data={})

        elif option_1G == "mode2":
            urll = "http://140.115.52.21:11135/"
            payloadd=""
            headerss = {}
            responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
            url = "http://140.115.52.21:11135/change"
            payload = json.dumps({
                "mode": 2,
                "start_date": predict_date
            })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            data = json.loads(response.text)
            if response.ok:
                print("ok")
                return render_template('1G-POE.html', option_1G=option_1G, predict_date=predict_date, predict_data=data,message='計算完成')
            else:
                return render_template('1G-POE.html',predict_data={})
        else:
            return render_template('1G-POE.html', predict_data={})
    elif request.method == 'GET':
        return render_template('1G-POE.html',predict_data={})

@app.route('/10G', methods=['GET', 'POST'])
def tenGpage2():
    if request.method == 'POST':
        option_10G = request.form.get("option_10G")
        predict_date = request.form.get("10G_date")
        print(option_10G)
        if option_10G == "mode1":
            url = "http://140.115.52.21:11135/"
            payload=""
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            url = "http://140.115.52.21:11135/change"
            payload = json.dumps({
                "mode": 1,
                "start_date": predict_date
            })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response)
            print(response.text)
            data = json.loads(response.text)
            if response.ok:
                return render_template('10G-POE.html', option_10G=option_10G, predict_date=predict_date, predict_data=data,message='計算完成')
            else:
                return render_template('10G-POE.html',predict_data={})

        elif option_10G == "mode2":
            urll = "http://140.115.52.21:11135/"
            payloadd=""
            headerss = {}
            responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
            url = "http://140.115.52.21:11135/change"
            payload = json.dumps({
                "mode": 2,
                "start_date": predict_date
            })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            print(response.text)
            data = json.loads(response.text)
            if response.ok:
                return render_template('10G-POE.html', option_10G=option_10G, predict_date=predict_date, predict_data=data,message='計算完成')
            else:
                return render_template('10G-POE.html',predict_data={})
        else:
            return render_template('10G-POE.html', predict_data={})
    elif request.method == 'GET':
        return render_template('10G-POE.html',predict_data={})




@app.route('/finished', methods = ['POST', 'GET'])
def finished():
        if request.method == 'POST':
            finished_select_option = request.form.get("finished_select_option")
            url = "http://140.115.52.21:11135/"
            payload=""
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            data = json.loads(response.text)
            print(finished_select_option)
            return render_template('finished.html', finish_data = data, finished_select_end = finished_select_option)
        elif request.method == 'GET':
            return render_template('finished.html', finish_data={})


@app.route('/add',methods = ['POST', 'GET'])
def add():
    if request.method == 'POST':
        add_id = request.form.get("add_id")
        add_num = int(request.form.get("add_num"))
        add_order = request.form.get("add_order")
        add_need = request.form.get("add_need")
        print(type(add_need),type(add_id),type(add_num),type(add_order))
        if add_id and add_num and add_order and add_need:
            urll = "http://140.115.52.21:11135/"
            payloadd=""
            headerss = {}
            responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
            url = "http://140.115.52.21:11135/insertorder"
            payload = json.dumps({
            "need_date": add_need,
            "number": add_num,
            "order_date": add_order,
            "type": add_id
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            if response.ok:
                return render_template('add.html',message='上傳完成')
            else:
                return render_template('add.html', message='上傳失敗')
        else:
            return render_template('add.html')
    elif request.method == 'GET':
         return render_template('add.html')



@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_id = str(request.form.get("search_id"))
        delete_id = request.form.get("delete_id")
        if delete_id:
            print('delete_id:', delete_id)
            urll = "http://140.115.52.21:11135/"
            payloadd=""
            headerss = {}
            responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
            url = "http://140.115.52.21:11135/deleteorder"

            payload = json.dumps({
                                "id": delete_id
                                })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            if response.ok:
                return render_template('search.html', message='Record deleted successfully.')
            else:
                return render_template('search.html', message='刪除失敗')
            
        elif search_id:
            print('search_id:', search_id)
            urll = "http://140.115.52.21:11135/"
            payloadd=""
            headerss = {}
            responsee = requests.request("POST", urll, headers=headerss, data=payloadd)
            url = "http://140.115.52.21:11135/search"

            payload = json.dumps({
                                "id": search_id
                                })
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            print(len(response.text))
            print(response.text)
            #Sprint(json.load(response))
            
            session['search_id'] = search_id
            if len(response.text) == 3:
                return render_template('search.html',message='無此訂單')
                
            else:
                data = json.loads(response.text)
                return render_template('search.html', search_data=data,message='搜尋成功')
        else:
            return render_template('search.html')
    else:
        return render_template('search.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
