from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roads')
def roads():
    return render_template('roads.html')

if __name__ == '__main__':
    app.run(debug=True)