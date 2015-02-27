import pymongo

try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
    print "Connection failed : %s" % e
conn

db_name = 
test_db = conn[db_name]

conn.database_name()

collect = test_db.my_collection
collect

myDoc = {'key1':1,'key2':2}
collect.insert(myDoc)
collect.insert({'key1':3,'key2':4})

conn.database_names()
test_db.collection_names()

rec = collection.fine_one({'key1':3})

print rec

print rec['key2']

docs = list(collect.find())

collect.distinct('key1')
collect.remove({'key1':1})

