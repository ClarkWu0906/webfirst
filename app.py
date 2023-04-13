from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    
    file.save(filename)
    return jsonify({'result': '上傳成功', 'filename': filename})

@app.route('/1G-POE')
def page2():
    return render_template('1G-POE.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route('/finished')
def finished():
    return render_template('finished.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
