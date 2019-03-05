'''
CREATE (a:sample) SET a.HER2_STATUS = "-" SET a.HER2_SNP6 = "NEUT" RETURN a
'''



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
        print(query)
    pass

if __name__ == '__main__':
#"python/nosql/neo4j/test_data/Sample.csv"
    read_csv("python/nosql/neo4j/test_data/HugoSymbol.csv", "HugoSymbol")









