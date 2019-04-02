from pymongo import MongoClient

client = MongoClient("mongodb://62.44.127.197:27017")
db = client.saniDB

def parse_object(url, collection):
    with open(url, "r") as f:
        for line in f:
                dic = {}
                line = line.rstrip('\n')
                if not ':' in line: continue
                records = line.split(',')
                for record in records:
                    key, value = record.split(':',1)
                    dic[key] = value
                print(dic)
                collection.insert_one(dic)
                


#parse_object("../nosql/neo4j/test_data/Sample.csv", db.samples)
#parse_object("../nosql/neo4j/test_data/HugoSymbol.csv", db.hugoSymbols)

samples = db.samples.find({}, {'name': 1})
samples_dicts = []
for s in samples:
    s['_id'] = str(s['_id'])
    samples_dicts.append(s)

hugos = db.hugoSymbols.find({}, {'name': 1})
hugos_dicts = []
for s in hugos:
    s['_id'] = str(s['_id'])
    hugos_dicts.append(s)
    
print(hugos_dicts)
   

