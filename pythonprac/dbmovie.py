from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.bjecv.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 가버나움의 평점 가져오기
# movie = db.movies.find_one({'title':'가버나움'})
# print(movie['star'])

# 가버나움의 평점과 같은 평점을 가진 영화제목 가져오기
# movie = db.movies.find_one({'title':'가버나움'})
# star = movie['star']
# all_movies = list(db.movies.find({'star':star},{'_id':False}))
#
# for m in all_movies:
#     print(m['title'])

# 가버나움 영화의 평점을 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})