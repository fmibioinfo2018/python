# PROBLEM TO SOLVE:
# checkout cypher syntaxis
# create sandbox db
# make a connection and create collections from the data

# import pip
# installed_packages = pip.get_installed_distributions()
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# print(installed_packages_list)

from neo4j.v1 import GraphDatabase, basic_auth
from pathlib import Path

connection_url = 'bolt://34.224.17.116:39507'

driver = GraphDatabase.driver(
    connection_url, auth=basic_auth('neo4j', 'decks-person-sources'))
session = driver.session()


def createNode(label, properties='', identifier='n'):
    return 'CREATE ({}:{} {}) '.format(identifier, label, properties)


def updateNodeProperties(key, value, identifier='n'):
    return 'SET {}.{} = "{}"'.format(identifier, key, value)


def testCreatingNodes():
    for i in range(0, 10):
        session.run(createNode('testNode', '{{name: {}}}'.format(i)))


def readFileByLines(fileName, callback):
    cwd = Path.cwd()
    path = '{}/test_data/{}'.format(cwd, fileName)

    f = open(path, 'r')

    for line in f:
        print(line)

    with open(path, encoding='utf-8-sig') as f:
        content = f.readlines()
        print(content)


def runMe(line):
    print('run run', line)


def main():
    readFileByLines('HugoSymbol1.csv', runMe)
    # testCreatingNodes()
    pass


if __name__ == "__main__":
    main()
