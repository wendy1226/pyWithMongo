from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['bingplanet']
collect = db['person']

#query
x = collect.find_one()
print(x)

#insert
mydict = { "name": "pi", "gender": "boy", "identity": "alienpi" }
y = collect.insert_one(mydict) 
print(y)

#delete
myquery = { "name": "bigpi" }
collect.delete_one(myquery)
# deleted show collection
for z in collect.find():
  print(z)

#reverse
myquery = { "name": "pi" }
newvalues = { "$set": { "name": "bigpi" } }
collect.update_one(myquery, newvalues)
# reverse show collection
for x in collect.find():
  print(x)

#update
collect.update_one({'name':'bigpi'},{'$set':{'age':'23'}}, upsert=True)
for x in collect.find():
  print(x)

#sort
mydoc = collect.find().sort("age",-1)
for x in mydoc:
  print(x)