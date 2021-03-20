# set the name of input DNA sequence file 
filename = 'dna.txt'
# open filename
infile = open(filename,'r')
dna_sequence = infile.read().rstrip()

# sequence length
print('Sequence length: %d' % len(dna_sequence))

# Freq of A
numA = dna_sequence.count('A')
print('Freq of A: %.3f' % (numA/len(dna_sequence)))

# Freq of C
numC = dna_sequence.count('C')
print('Freq of C: %.3f' % (numC/len(dna_sequence)))

# Freq of G
numG = dna_sequence.count('G')
print('Freq of G: %.3f' % (numG/len(dna_sequence)))

# Freq of T
numT = dna_sequence.count('T')
print('Freq of T: %.3f' % (numT/len(dna_sequence)))

# G+C content
print('G+C content: %.3f' % ((numG+numC)/len(dna_sequence)))

# simple check to make sure the frequencies sum to 1
print('Sum of Freqs: %.3f' % ((numG+numC+numA+numT)/len(dna_sequence)))
