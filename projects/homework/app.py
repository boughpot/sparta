from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.bjecv.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.homeworks.insert_one(doc)

    return jsonify({'msg': '응원이 등록 되었습니다!'})


@app.route("/homework", methods=["GET"])
def homework_get():
    homework_list = list(db.homeworks.find({},{'_id':False}))
    return jsonify({'homeworks': homework_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
