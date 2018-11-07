import decimal
import operator
from decimal import *
from collections import Counter
from operator import itemgetter

def getCG(DNA):
        ctr = Counter(DNA)
        return float( ctr['C'] + ctr['G'] ) / len(DNA)

def main2():
    blocks = open('data/fasta.txt', 'r').read().split(">")[1:]

    DNAS = {}

    for block in blocks:
        [name, DNA] = block.split("\n", 1)
        DNA = DNA.replace("\n", '')
        DNAS[name] = getCG(DNA)

    DNAS_S = sorted(DNAS.items(), key=itemgetter(1))

    print(DNAS_S[-1][0])
    print ('%2.6f%%' % (DNAS_S[-1][1]*100))

def main1():
    f = open('data/fasta.txt', 'r')
    getcontext().prec = 8

    dict = {}
    current_name = ''
    current_seq = ''
    line1 = '1'
    while True:
        if not line1: break
        line1 = f.readline().strip()

        if not line1 or line1.startswith('>'):
            gc_count = 0
            for item in current_seq:
                if item == 'G' or item == 'C':
                    gc_count = gc_count + 1
            if gc_count > 0:
                freq = (Decimal(gc_count)/len(current_seq)) * 100
                dict.update({current_name: freq})

            current_seq = ''
            current_name = line1[1:]
        else:
            current_seq = current_seq + line1
    
    
    sorted_x = sorted(dict.items(), key=operator.itemgetter(0))
    print(sorted_x)

if __name__ == '__main__':
    main2()
