'''
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

col.insert_one(test)'''

import sys
import os

dir = os.path.realpath(__file__) #경로 불러오기
print(dir)

print(sys.path)

#sys.path.append("C:\Users\wooseong\Documents\개인파일\IT_SourceCode\main_project")

#sys.path.append("C:\Users\wooseong\Documents\개인파일\IT_SourceCode\main_project")
#sys.path.append('\\wudong.synology.me@ssl@5006\DavWWWRoot\두번째 저장소\개인파일\IT_SourceCode\')