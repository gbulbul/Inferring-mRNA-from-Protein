codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
"UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
"UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
"UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


def frequency_counter(dict_codons):
    codons = {key:val for key, val in dict_codons.items() if val != "STOP"}
    count = {}
    for v in codons.values():
        if(not(v in count)):
            count[v] = 0
        count[v] += 1
    return count
print(frequency_counter(codons))
codons_freq=frequency_counter(codons)
protein_seq='MA'
def protein_to_mrna(protein_seq):
    sum=1
    for num in range(len(protein_seq)):
        for key in codons_freq.keys():
            if key==protein_seq[num]:
               sum*=codons_freq[key]
    return(sum*3) % 1000000

print(protein_to_mrna(protein_seq))
    
    

