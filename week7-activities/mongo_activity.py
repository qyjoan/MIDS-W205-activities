import csv
import pymongo

try:
    conn=pymongo.MongoClient()
    print "Connected!"
except pymongo.errors.ConnectionFailure, e:
    print "Connection failed : %s" % e
conn

db_name = 'cong_db'
test_db = conn[db_name]

collection = test_db.mem_db
collection

fname = 'legislators-historic.csv'
records= csv.DictReader(open(fname))
for rec in records:
    collection.insert(rec)

collection.count()

female_non_dem = collection.find({'gender':'F', 'party': {'$ne':'Democrat'}})

for a in female_non_dem:
    print a['first_name', 'birthday']

a = collection.find(
{'gender': 'F', 'party': {'$ne' : 'Democrat'}}, 
{'_id': 0, 'first_name' : 1, 'birthday' : 1}
)

collection.find({'gender': 'F', 'party': {'$ne' : 'Democrat'}}, 
{'_id': 0, 'first_name' : 1, 'birthday' : 1}
)

# or

a = collection.find( {"$or": [{"first_name": "John" }, {"first_name": "Joshua"}]})

# group by

a = collection.aggregate([{"$group": {"_id": "$first_name", "count": {"$sum": 1}}}])
pipe = [{'$group': {'_id': '$first_name', 'total': {'$sum': 1}}}, {'$sort' : { 'total' : -1,'_id':1}}]
collection.aggregate(pipeline=pipe)
