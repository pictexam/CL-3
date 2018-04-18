from pymongo import MongoClient

client=MongoClient()

db=client.dbname

doc0={"phil":"0", "food": "rice"}
doc1= {"phil":"1","food":"noodles"}
doc2= {"phil":"2","food":"sushi"}
doc3= {"phil":"3","food":"dosa"}
doc4= {"phil":"4","food":"wada"}

doc=[doc0, doc1, doc2, doc3, doc4]

db.coll.insert_many(doc)