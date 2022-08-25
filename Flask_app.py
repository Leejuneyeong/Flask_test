
from flask import Flask,render_template;

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/test1')
def test():
    return render_template('test1.html')

if __name__ == '__main__':
    app.run()
