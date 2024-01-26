from flask import Flask

a = 0

app = Flask(__name__)


@app.route('/' , methods=['GET'])
def get():
    global a
    return f'({a})'

@app.route('/plus', methods=['POST'])
def plus():
    global a
    a += 1
    return f'({a})'

@app.route('/minus', methods=['POST'])
def minus():
    global a
    a -= 1
    return f'({a})'

if __name__ == '__main__':
    app.run()

