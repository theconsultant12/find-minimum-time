import Bio

from Bio.Seq import Seq as seq
from Bio.Alphabet import generic_dna,generic_rna

n_sample = ('')
dna = seq(n_sample,generic_dna)
rna = seq(n_sample, generic_rna)

def plot_nucleotide_graph(dna):
    from collections import Counter
    dna_indices = Counter(dna)
    from matplotlib import pyplot as plt
    plot = plt.bar(dna_indices.keys(),dna_indices.values())
    return plot

def translate(dna,rna_or_dna):
    if rna_or_dna.lower() == 'dna':
        new_protein = seq(dna,generic_dna).translate()
    if rna_or_dna.lower() == 'rna':
        new_protein = seq(dna,generic_rna).translate()
    return new_protein


n_sample = input('Enter a sequence string: ')
n_type = input('Type "dna" for a dna and "rna for rna sequence"')
if n_type.lower() == 'dna':
  dna = seq(n_sample,generic_dna)
elif n_type.lower() == 'rna':
  rna = seq(n_sample, generic_rna)

print('The protein sequence of the nucleotide is: ',translate(n_sample, n_type))
plot_nucleotide_graph(n_sample)
