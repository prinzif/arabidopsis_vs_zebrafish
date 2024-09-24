import pandas as pd

zebrafish_df = pd.read_csv('C:/Users/viola/Desktop/datasets/biopython/significant_zebrafish.csv')
arabidopsis_df = pd.read_csv('C:/Users/viola/Desktop/datasets/biopython/significant_arabidopsis.csv')

zebrafish_homologs = zebrafish_df[['query_id', 'subject_id', 'perc_identity', 'e_value']].drop_duplicates()
zebrafish_homologs['organism'] = 'Zebrafish'

arabidopsis_homologs = arabidopsis_df[['query_id', 'subject_id', 'perc_identity', 'e_value']].drop_duplicates()
arabidopsis_homologs['organism'] = 'Arabidopsis'

combined_homologs = pd.concat([zebrafish_homologs, arabidopsis_homologs], ignore_index=True)

filtered_homologs = combined_homologs[
    (combined_homologs['perc_identity'] > 50) &
    (combined_homologs['e_value'] < 1e-10)
]

max_identity = filtered_homologs.groupby(['query_id', 'subject_id'])['perc_identity'].max().reset_index()

final_homologs = pd.merge(max_identity, filtered_homologs, on=['query_id', 'subject_id', 'perc_identity'])

ortologs = final_homologs.groupby('query_id').filter(lambda x: len(x) == 1)

ortologs['combined'] = ortologs.apply(
    lambda x: f"{x['organism']} ({x['subject_id']}) - {x['perc_identity']}%", axis=1
)

ortologs = ortologs[['query_id', 'combined']]

ortologs.to_csv('C:/Users/viola/Desktop/datasets/biopython/highest_identity_orthologs.csv', index=False)

print(ortologs.head())

print(f"Количество ортологов: {len(ortologs)}")
