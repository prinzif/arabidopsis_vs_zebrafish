from BCBio import GFF
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord  

def extract_gene_sequences_simple(fasta_file, gff_file):
    gene_sequences = []
    genome_seq = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
    
    with open(gff_file) as gff_handle:
        for line in gff_handle:
            if line.startswith("#"):
                continue  
            parts = line.strip().split("\t")
            if len(parts) < 9:
                continue  
            
            seq_id, source, feature_type, start, end, score, strand, phase, attributes = parts
            
            if feature_type == "gene":
                start, end = int(start), int(end)
                if start > end:
                    print(f"Skipping feature with problematic coordinates: start {start}, end {end}")
                    continue
                gene_seq = genome_seq[seq_id].seq[start:end]
                gene_record = SeqRecord(gene_seq, id=attributes, description="gene")  # Use SeqRecord
                gene_sequences.append(gene_record)
    
    return gene_sequences


arabidopsis_fasta = r"C:\Users\viola\Desktop\datasets\ncbi_dataset plant\ncbi_dataset\data\GCF_000001735.4\GCF_000001735.4_TAIR10.1_genomic.fna"
arabidopsis_gff = r"C:\Users\viola\Desktop\datasets\ncbi_dataset plant\ncbi_dataset\data\GCF_000001735.4\genomic.gff"

zebrafish_fasta = r"C:\Users\viola\Desktop\datasets\ncbi_dataset fish\ncbi_dataset\data\GCF_000002035.6\GCF_000002035.6_GRCz11_genomic.fna"
zebrafish_gff = r"C:\Users\viola\Desktop\datasets\ncbi_dataset fish\ncbi_dataset\data\GCF_000002035.6\genomic.gff"


arabidopsis_genes = extract_gene_sequences_simple(arabidopsis_fasta, arabidopsis_gff)
print(f"Extracted {len(arabidopsis_genes)} gene sequences for Arabidopsis.")

zebrafish_genes = extract_gene_sequences_simple(zebrafish_fasta, zebrafish_gff)
print(f"Extracted {len(zebrafish_genes)} gene sequences for Zebrafish.")


