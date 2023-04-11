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

@app.route('/page2')
def page2():
    return render_template('page2.html')


if __name__ == '__main__':
    app.run(debug=True)
