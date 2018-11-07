from collections import defaultdict
from collections import Counter

def main():
    """ Test main method """

    f = open('data/rosalind_dna.txt', 'r')

    print(f)
    sequence = f.read();

    count=0;
    amino_acid_map = {}
    for i in sequence:
        if not amino_acid_map.get(i):
            amino_acid_map[i]=1
        else:
            amino_acid_map[i]+=1
    
    amino_acid_map2 = defaultdict(int)
    for i in sequence:
        amino_acid_map2[i]+=1

    amino_acid_map3 = Counter(sequence)
    
    print(str(amino_acid_map["A"]) + " " + str(amino_acid_map["C"]) + " " + str(amino_acid_map["G"]) + " " + str(amino_acid_map["T"]))

    print("The count is " + str(count))
    print("Normal dict result " + str(amino_acid_map))
    print("DefaultDict result " + str(amino_acid_map2))
    print("Counter result" + str(amino_acid_map3))
if __name__ == "__main__":
    main()
