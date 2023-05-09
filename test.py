import pymongo

test = {
    "이름" : "양우성",
    "나이" : 30,
    "거주지":"서울특별시",
    "키":170,
    "프로필사진":[
        "a.jpg",
        "b.jpg"
    ]

}

conn = pymongo.MongoClient("localhost",27017)
db = conn.test
col = db.members

col.insert_one(test)