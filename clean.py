import matplotlib.pyplot as plt
from Bio.SeqUtils import gc_fraction
from Bio import SeqIO

def clean_sequence(seq_record):
    cleaned_seq = seq_record.seq.replace("N", "")
    gc_content = gc_fraction(cleaned_seq)
    return gc_content, len(cleaned_seq)

arabidopsis_fasta = r"C:\Users\viola\Desktop\datasets\ncbi_dataset plant\ncbi_dataset\data\GCF_000001735.4\GCF_000001735.4_TAIR10.1_genomic.fna"
arabidopsis_gc_contents = []
arabidopsis_lengths = []

with open(arabidopsis_fasta, "r") as fna_file:
    for seq_record in SeqIO.parse(fna_file, "fasta"):
        gc_content, length = clean_sequence(seq_record)
        arabidopsis_gc_contents.append(gc_content)
        arabidopsis_lengths.append(length)

zebrafish_fasta = r"C:\Users\viola\Desktop\datasets\ncbi_dataset fish\ncbi_dataset\data\GCF_000002035.6\GCF_000002035.6_GRCz11_genomic.fna"
zebrafish_gc_contents = []
zebrafish_lengths = []

with open(zebrafish_fasta, "r") as fna_file:
    for seq_record in SeqIO.parse(fna_file, "fasta"):
        gc_content, length = clean_sequence(seq_record)
        zebrafish_gc_contents.append(gc_content)
        zebrafish_lengths.append(length)

chromosomes_arabidopsis = ['Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5', 'Mito', 'Plastid']
chromosomes_zebrafish = ['Chr1', 'Chr2', 'Chr3', 'Chr4', 'Chr5']

avg_gc_arabidopsis = [sum(arabidopsis_gc_contents) / len(arabidopsis_gc_contents)]
avg_gc_zebrafish = [sum(zebrafish_gc_contents) / len(zebrafish_gc_contents)]

bar_width = 0.35
x = range(len(chromosomes_arabidopsis))  

plt.bar(x, avg_gc_arabidopsis, width=bar_width, label='Arabidopsis', color='b')
plt.bar([p + bar_width for p in x], avg_gc_zebrafish, width=bar_width, label='Zebrafish', color='g')

plt.xlabel('Chromosomes')
plt.ylabel('Average GC Content (%)')
plt.title('GC Content Comparison: Arabidopsis vs Zebrafish')
plt.xticks([p + bar_width / 2 for p in x], chromosomes_arabidopsis)
plt.legend()
plt.savefig("gc_content_comparison.png")
plt.show()
