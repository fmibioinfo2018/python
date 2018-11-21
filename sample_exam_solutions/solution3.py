# Да се прочете секвенцията(Fasta формат) от файл [data/fasta_seq_1.fa] и да се намери честотата на срещане на “Т” в секвенцията(15т.)

from Bio import SeqIO

fasta_sequence = SeqIO.parse(open('../sample_exam/data/fasta_seq_1.fa'), 'fasta')

sequence = ''
occurances = 0

for item in fasta_sequence:
    print(dir(item))
    sequence += str(item.seq)

for letter in sequence:
    if letter == 'T':
        occurances += 1
print(occurances)
