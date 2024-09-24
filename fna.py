from Bio import SeqIO

# Загрузка Arabidopsis thaliana (TAIR10.1)
arabidopsis_fasta = "C:\\Users\\viola\\Desktop\\datasets\\ncbi_dataset plant\\ncbi_dataset\\data\\GCF_000001735.4\\GCF_000001735.4_TAIR10.1_genomic.fna"
with open(arabidopsis_fasta, "r") as fna_file:
    for seq_record in SeqIO.parse(fna_file, "fasta"):
        print(f"Arabidopsis Chromosome: {seq_record.id}")
        print(f"Length: {len(seq_record)} bp")
        print(f"First 100 bases: {seq_record.seq[:100]}")

# Загрузка генома Danio rerio (GRCz11)
zebrafish_fasta = "C:\\Users\\viola\\Desktop\\datasets\\ncbi_dataset fish\\ncbi_dataset\\data\\GCF_000002035.6\\GCF_000002035.6_GRCz11_genomic.fna"
with open(zebrafish_fasta, "r") as fna_file:
    for seq_record in SeqIO.parse(fna_file, "fasta"):
        print(f"Zebrafish Chromosome: {seq_record.id}")
        print(f"Length: {len(seq_record)} bp")
        print(f"First 100 bases: {seq_record.seq[:100]}")

