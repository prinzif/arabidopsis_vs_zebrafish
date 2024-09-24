import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/viola/Desktop/datasets/biopython/highest_identity_orthologs.csv'
df = pd.read_csv(file_path)

def extract_gene_names(row):
    gene_info = row.split(';')
    for info in gene_info:
        if "Name=" in info:
            return info.split('=')[1]
    return None

df['gene_names'] = df['query_id'].apply(extract_gene_names)
df['combined_gene_names'] = df['combined'].apply(extract_gene_names)

fig, ax = plt.subplots(figsize=(10, 6))  
ax.axis('tight')
ax.axis('off')
table_data = df[['gene_names', 'combined_gene_names']].dropna().values.tolist()
table = ax.table(cellText=table_data, colLabels=['Arabidopsis Gene', 'Zebrafish Gene'], cellLoc='center', loc='center')

plt.show()
