import http.client
import sys
import json
from neo4j import basic_auth

from neo4j_test import MutationsDB

class EnsemblClient:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("rest.ensembl.org")

    def request(self, url, headers={"Content-Type" : "application/json"}, method="GET"):
        self.conn.request(method, url, headers=headers)
        response = self.conn.getresponse()
        if response.status > 200:
            return None
        obejct = response.read().decode()
        return obejct
    
    def close(self):
        self.conn.close()



def main():
    db = MutationsDB("bolt://34.207.155.255:39042", basic_auth("neo4j", "appropriation-finishes-feeling"))
    protein_name = "C1orf147"
    ens_client = EnsemblClient()
    
    query = "MATCH p=(s:Sample)-[r:mutation]->(h:HugoSymbol) RETURN ID(r) as id, h.name as name"
    res = db.execute_query(query)
    for r in res:
        protein_name = r['name']
        q = result = ens_client.request("/lookup/symbol/homo_sapiens/" + protein_name)
        if result:
            object_result = json.loads(result)
            q = "match ()-[r:mutation]->() where id(r)={} set r.ensembl_id='{}' return r".format(r['id'], object_result['id'])
            print(db.execute_query(q))

    ens_client.close()
    
    
if __name__ == '__main__':
    main()