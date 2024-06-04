from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:rlawngml27@cluster0.ecr7cir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', tlsCAFile=ca)
db = client.sample_mflix

db.test.insert_one({'name' : "juhee"})
# db.test.delete_one({'name' : "juhee"})
print(list(db.test.find({},{'_id':False})))


# 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.test.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})