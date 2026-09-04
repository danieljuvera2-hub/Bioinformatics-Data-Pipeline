import pandas as pd
df = pd.read_csv("rna_data.csv")
df_clean = df.dropna()
df_clean['Gene_ID'] = df_clean['Gene_ID'].str.upper()
df_clean = df_clean[df_clean['Expression_Level'] >= 0]
df_clean = df_clean[df_clean['P_Value'] <= 0.05]
gene_summary = df_clean.groupby('Gene_ID')['Expression_Level'].mean() 
print(gene_summary)
gene_summary.to_csv("gene_summary.csv")
