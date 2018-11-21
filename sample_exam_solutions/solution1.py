#* Да се намери честотата на срещане на “А” Аденин в секвенцията: ATAGTGGGAAGATTTATA

seq = 'ATAGTGGGAAGATTTATA'
freq = 0

for ch in seq:
    if ch == 'A':
        freq += 1

print(freq)