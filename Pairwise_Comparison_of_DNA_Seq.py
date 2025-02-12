
seq = ['ATG', 'TGC', 'CGA']

for seq1 in seq:
    for seq2 in seq:
        if seq1 != seq2:
            print(f'Comparing {seq1} with {seq2}')
            distancia = 0
            for i in range(len(seq1)):
                if seq1[i] != seq2[i]:
                    distancia += 1
            print(f"Hamming distance of {seq1} y {seq2} es {distancia}")


