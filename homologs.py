import pandas as pd

zebrafish_df = pd.read_csv('C:/Users/viola/Desktop/datasets/biopython/significant_zebrafish.csv')
arabidopsis_df = pd.read_csv('C:/Users/viola/Desktop/datasets/biopython/significant_arabidopsis.csv')

zebrafish_homologs = zebrafish_df[['query_id', 'subject_id', 'perc_identity']].drop_duplicates()
zebrafish_homologs['organism'] = 'Zebrafish'

arabidopsis_homologs = arabidopsis_df[['query_id', 'subject_id', 'perc_identity']].drop_duplicates()
arabidopsis_homologs['organism'] = 'Arabidopsis'

combined_homologs = pd.concat([zebrafish_homologs, arabidopsis_homologs], ignore_index=True)

max_identity = combined_homologs.groupby(['query_id', 'subject_id'])['perc_identity'].max().reset_index()

final_homologs = pd.merge(max_identity, combined_homologs, on=['query_id', 'subject_id', 'perc_identity'])

final_homologs['combined'] = final_homologs.apply(
    lambda x: f"{x['organism']} ({x['subject_id']}) - {x['perc_identity']}%", axis=1
)

final_homologs = final_homologs[['query_id', 'combined']]

final_homologs.to_csv('C:/Users/viola/Desktop/datasets/biopython/highest_identity_homologs.csv', index=False)

print(final_homologs.head())

print(f"Количество гомологов: {len(final_homologs)}")
