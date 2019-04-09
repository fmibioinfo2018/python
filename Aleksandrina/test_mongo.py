from pymongo import MongoClient
from neo4j import GraphDatabase, basic_auth

client = MongoClient("mongodb://62.44.127.197:27017")
db = client.saniDB

neo4j_driver = GraphDatabase.driver(
    "bolt://100.26.154.131:37250", 
    auth=basic_auth("neo4j", "jackbox-prefix-stretcher"))

def check_type(element):
    try:
        return float(element)
    except ValueError:
        return element

def parse_object(url, collection):
    with open(url, "r") as f:
        for line in f:
                dic = {}
                line = line.rstrip('\n')
                if not ':' in line: continue
                records = line.split(',')
                for record in records:
                    key, value = record.split(':',1)
                    dic[key] = check_type(value)

                collection.insert_one(dic)
                

def neo4j_add(driver, label, values):
   with driver.session() as session:
        for v_dict in values:
            query = "create (r:{}) ".format(label)
            for key, value in v_dict.items():
                query += "set r.{} = '{}' ".format(key, value)
            query += "return r"
            session.run(query)
            print(query)

def mongo_to_neo4j(collection):
    documents = collection.find({}, {'name': 1})
    documents_dicts = []
    for s in documents:
        new_document = {}
        new_document['mongo_id'] = str(s['_id'])
        new_document['name'] = s['name']
        documents_dicts.append(new_document)
    return documents_dicts


def add_relationships_from_file(driver, filename, type, from_node, to_node):
        f = open(filename, 'r')
        count = 0
        with driver.session() as session:
            for line in f:
                line = line.rstrip('\n')
                if not ',' in line: continue
                records = line.split(',')
                first = records[0]
                second = records[len(records)-1]
                query = "match (a:{}), (b:{}) where a.name = '{}' and b.name = '{}' create (a)-[r:{}]->(b) ".format(from_node, to_node, first, second, type)
                for record in records[1:len(records)-1]:
                    r = record.split(':',1)
                    if r[0] == "000": continue
                    if len(r) < 2:
                        r.append(' ')
                    query += "set r.{} = '{}' ".format(r[0], r[1])
                query += "return r"
                count += 1
                session.run(query)
                print(query)
        #print(count)
        f.close()


#parse_object("../nosql/neo4j/test_data/Sample.csv", db.samples)
#parse_object("../nosql/neo4j/test_data/HugoSymbol.csv", db.hugoSymbols)

#neo4j_add(neo4j_driver, "Samples", mongo_to_neo4j(db.samples))
#neo4j_add(neo4j_driver, "HugoSymbols", mongo_to_neo4j(db.hugoSymbols))

add_relationships_from_file(neo4j_driver, "../nosql/neo4j/test_data/mutation.csv", "mutation", "Samples", "HugoSymbols")
   

