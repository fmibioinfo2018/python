def main():
    f = open('data/dna_structure.txt', 'r')
    sequence = f.read();

    switcher = {'A': 'T', 'T': 'A', 'C': 'G', 'G':'C'}
    result_seq = []
    for item in sequence:
        result_seq.append(switcher.get(item))
    print(''.join(result_seq)[::-1])


if __name__ == "__main__":
    main()