from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    doc = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive
    }
    db.bookreview.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장이 완료 되었습니다.!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    review = list(db.bookreview.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
