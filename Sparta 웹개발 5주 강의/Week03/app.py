import certifi
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)

ca = certifi.where()

client = MongoClient('mongodb+srv://test:rlawngml27@cluster0.ecr7cir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', tlsCAFile=ca)
db = client.sample_mflix

import requests
from bs4 import BeautifulSoup

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/movie", methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')
    print(soup)
    title = soup.select_one('meta[property="og:title"]')['content']
    print("테스트1")
    image = soup.select_one('meta[property="og:image"]')['content']
    print("테스트2")
    desc = soup.select_one('meta[property="og:description"]')['content']
    print("테스트3")
    doc = {
        'image':image,
        'title':title,
        'desc':desc,
        'star':star_receive,
        'comment':comment_receive
    }

    db.movies.insert_one(doc)

    return jsonify({'msg':'POST 연결 완료!'})

@app.route("/movie", methods=["GET"])
def movie_get():
    movies_list = list(db.movies.find({},{'_id':False}))
    return jsonify({'movies':movies_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=3000, debug=True)