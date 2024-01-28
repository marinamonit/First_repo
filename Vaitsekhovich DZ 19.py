from flask import Flask, render_template
from DB.my_model import get_orders

app = Flask(__name__)


@app.route('/' , methods=['GET'])
def template():
    spis_orders = get_orders()
    return render_template('index.html', orders=spis_orders)


@app.route('/order', methods=['GET'])
def order():
    return render_template('order.html')



if __name__ == '__main__':
    app.run()