from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://54.236.44.131:32834", 
    auth=basic_auth("neo4j", "blanket-pistons-wines"))
session = driver.session()

def relations_read():
    f = open("python/nosql/neo4j/test_data/mutation.csv")
    lines = f.readlines()

    for line in lines[1:]:
        query = "MATCH (a:sample),(b:hugoSymbol) "
        keys = line.split(",")
        query += " WHERE a.name = '{}' AND b.name = '{}' CREATE (a)-[r:mutation]->(b) ".format(keys[0].rstrip(), keys[len(keys) - 1].rstrip())
        for key in keys[1:len(keys) - 1]:
            key_value = key.split(":")
            if len(key_value) >= 2:
                query += " SET r.{} = '{}' ".format(key_value[0].rstrip(), key_value[1].rstrip())
        query += " RETURN a "
        yield query


def read_csv(file, label):
    f = open(file,'r')
    lines = f.readlines()
    for line in lines[1:]:
        query = "CREATE (a:{}) ".format(label)
        keys = line.split(",")
        for key in keys:
            key_value = key.split(":")
            query += " SET a.{} = '{}'".format(key_value[0].rstrip(), key_value[1].rstrip())
        query += " RETURN a"
        session.run(query)
    pass

if __name__ == '__main__':
#"python/nosql/neo4j/test_data/Sample.csv"
    #read_csv("python/nosql/neo4j/test_data/HugoSymbol.csv", "HugoSymbol")
    #read_csv("python/nosql/neo4j/test_data/Sample.csv", "Sample")
    for query in relations_read():
        session.run(query)









