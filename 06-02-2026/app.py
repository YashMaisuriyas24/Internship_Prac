from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def hello_world():
    return jsonify({"message": "yash, world!"})

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', name="Yash")

if __name__ == '__main__':
    app.run(debug=True)
