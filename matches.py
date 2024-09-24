import pandas as pd
import matplotlib.pyplot as plt

zebrafish_file = r"C:\Users\viola\Desktop\datasets\biopython\zebrafish_vs_arabidopsis_filtered.csv"
arabidopsis_file = r"C:\Users\viola\Desktop\datasets\biopython\arabidopsis_vs_zebrafish_filtered.csv"

zebrafish_vs_arabidopsis = pd.read_csv(zebrafish_file)
arabidopsis_vs_zebrafish = pd.read_csv(arabidopsis_file)

print("Zebrafish vs Arabidopsis:")
print(zebrafish_vs_arabidopsis.head())

print("\nArabidopsis vs Zebrafish:")
print(arabidopsis_vs_zebrafish.head())

significant_zebrafish = zebrafish_vs_arabidopsis[zebrafish_vs_arabidopsis['e_value'] < 1e-5]
significant_arabidopsis = arabidopsis_vs_zebrafish[arabidopsis_vs_zebrafish['e_value'] < 1e-5]

significant_zebrafish.to_csv(r"C:\Users\viola\Desktop\datasets\biopython\significant_zebrafish.csv", index=False)
significant_arabidopsis.to_csv(r"C:\Users\viola\Desktop\datasets\biopython\significant_arabidopsis.csv", index=False)

print(f"Количество значимых совпадений для Zebrafish: {len(significant_zebrafish)}")
print(f"Количество значимых совпадений для Arabidopsis: {len(significant_arabidopsis)}")

plt.scatter(significant_zebrafish['e_value'], significant_zebrafish['perc_identity'], alpha=0.5, label='Zebrafish vs Arabidopsis')
plt.scatter(significant_arabidopsis['e_value'], significant_arabidopsis['perc_identity'], alpha=0.5, label='Arabidopsis vs Zebrafish')
plt.xscale('log')
plt.xlabel('E-значение')
plt.ylabel('Процент идентичности')
plt.legend()
plt.show()

common_genes = pd.merge(significant_zebrafish, significant_arabidopsis, how='inner', on='gene_id')
print(f"Количество общих генов: {len(common_genes)}")


