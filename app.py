from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    file = request.files['file']
    filename = file.filename
    
    file.save(filename)
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

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route('/finished', methods = ['POST', 'GET'])
def finished():
        if request.method == 'POST':
            return render_template('finished.html')
        elif request.method == 'GET':
            return render_template('finished.html')


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/search' , methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
            return render_template('search.html')
    elif request.method == 'GET':
        return render_template('search.html')

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
