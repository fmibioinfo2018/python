
from neo4j import GraphDatabase, basic_auth

#  "bolt://34.224.2.79:34310", 
#     auth=basic_auth("neo4j", "ingredient-vibrations-files"))
class MutationsDB:
    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)

    def add_nodes_from_file(self, filename, label):
        f = open(filename, 'r')
        with self.driver.session() as session:
            for line in f:
                line = line.rstrip('\n')
                if not ':' in line: continue
                records = line.split(',')
                query = "create (r:{}) ".format(label)
                for record in records:
                    key, value = record.split(':')
                    query += "set r.{} = '{}' ".format(key, value)
                query += "return r"
                session.run(query)
                print(query)
        f.close()

    def add_relationships_from_file(self, filename, type, from_node, to_node):
        f = open(filename, 'r')
        count = 0
        with self.driver.session() as session:
            for line in f:
                line = line.rstrip('\n')
                if not ',' in line: continue
                records = line.split(',')
                first = records[0]
                second = records[len(records)-1]
                query = "match (a:{}), (b:{}) where a.name = '{}' and b.name = '{}' create (a)-[r:{}]->(b) ".format(from_node, to_node, first, second, type)
                for record in records[1:len(records)-1]:
                    r = record.split(':')
                    if r[0] == "000": continue
                    if len(r) < 2:
                        r.append(' ')
                    query += "set r.{} = '{}' ".format(r[0], r[1])
                query += "return r"
                count += 1
                session.run(query)
                #print(query)
        #print(count)
        f.close()

    def close(self):
        self.driver.close()



if __name__ == "__main__":
    db = MutationsDB("bolt://34.224.2.79:34310", basic_auth("neo4j", "ingredient-vibrations-files"))
    db.add_nodes_from_file("../nosql/neo4j/test_data/Sample.csv", "Sample")
    db.add_nodes_from_file("../nosql/neo4j/test_data/HugoSymbol.csv", "HugoSymbol")
    db.add_relationships_from_file("../nosql/neo4j/test_data/mutation.csv", "mutation", "Sample", "HugoSymbol")