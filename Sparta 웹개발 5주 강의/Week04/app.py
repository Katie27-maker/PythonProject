from flask import Flask, render_template, jsonify, request
import certifi

ca = certifi.where()

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:rlawngml27@cluster0.ecr7cir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', tlsCAFile=ca)

db = client.sample_mflix


@app.route('/')
def homework():
    return render_template('index.html')



@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문 완료!'})



@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)