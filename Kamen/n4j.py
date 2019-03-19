from neo4j.v1 import GraphDatabase, basic_auth
from pathlib import Path
import re

connection_url = 'bolt://52.72.13.205:38476'

driver = GraphDatabase.driver(
    connection_url, auth=basic_auth('neo4j', 'mother-accusation-subtask'))
session = driver.session()


def createNodeThatDoesntExist(label, properties=''):
    print(properties)

    return 'MERGE (n:{} {})'.format(label, properties)

# def updateNodeProperties(key, value, identifier='n'):
#     return 'SET {}.{} = "{}"'.format(identifier, key, value)


# def testCreatingNodes():
#     for i in range(0, 10):
#         session.run(createNode('testNode', '{{name: {}}}'.format(i)))


def readFileByLines(fileName):
    cwd = Path.cwd()
    path = '{}/test_data/{}'.format(cwd, fileName)
    with open(path) as f:
        content = f.readlines()
    return content

def accumulatePropertiesString(lines):
    result = []
    for line in lines[1:]:
        newLine = []
        line.rstrip()
        if line is not '':
            for item in line.split(','):
                if ':' not in item:
                    key = 'unspecifiedKey'
                    value = item
                else:
                    key, value = item.split(':', 1)
                newLine.append("{}:'{}'".format(key, value))
            properties = '{{{}}}'.format(','.join(newLine))
            result.append(properties)
    return result

def testForEqualLines(lines):
    print(lines.count(lines[0]) == len(lines))

def createNodes(label, properties):
    for property in properties:
       session.run(createNodeThatDoesntExist(label, property))

def main():
    # testForEqualLines(
    #     readFileByLines('HugoSymbol.csv')
    # )

    createNodes(
        'Protein',
        accumulatePropertiesString(
            readFileByLines('HugoSymbol.csv')
        )
    )

    createNodes(
        'Patient',
        accumulatePropertiesString(
            readFileByLines('Sample.csv')
        )
    )

    createNodes(
        'Mutation',
        accumulatePropertiesString(
            readFileByLines('mutation.csv')
        )
    )

if __name__ == "__main__":
    main()
