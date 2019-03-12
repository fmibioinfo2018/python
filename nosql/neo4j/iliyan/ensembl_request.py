import http.client
import sys
import json
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://54.236.44.131:32834", 
    auth=basic_auth("neo4j", "blanket-pistons-wines"))
session = driver.session()

class EnsemblClient:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("rest.ensembl.org")

    def request(self, url, headers={"Content-Type": "application/json"}, method="GET"):
        self.conn.request(method, url, headers=headers)
        responce = self.conn.getresponse()
        print(responce.status, responce.reason)
        obj = responce.read().decode()
        return obj

    def close(self):
        self.comm.close()

def main():
    ens_client = EnsemblClient()
    proteins = session.run("MATCH (n:HugoSymbol) RETURN n.name, n.EntrezGeneId LIMIT 25")
    
    for name in proteins:
        print("by index {}".format(name[0]))

    obj = ens_client.request("/lookup/symbol/homo_sapiens/BRCA2?content-type=application/xml;expand=1")
    json_res = json.loads(obj)

    id = json_res['id']

    print(id)

if __name__ == '__main__':
    main()