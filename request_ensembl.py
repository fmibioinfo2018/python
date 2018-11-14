import http.client
import sys
import json

class EnsemblClient:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("rest.ensembl.org")

    def request(self, url, headers={"Content-Type" : "application/json"}, method="GET"):
        self.conn.request(method, url, headers=headers)
        responce = self.conn.getresponse()
        print(responce.status, responce.reason)
        obejct = responce.read().decode()
        return obejct
    
    def close(self):
        self.conn.close()



def main():
    ens_client = EnsemblClient()
    result = ens_client.request("/family/id/PTHR10410_SF2?")
    object_result = json.loads(result)

    for item in object_result["members"][0:3]:
        seq_result = ens_client.request("sequence/id/"+item["gene_stable_id"])
        print(json.loads(seq_result))
    
    ens_client.close()
    
    
if __name__ == '__main__':
    main()
    
