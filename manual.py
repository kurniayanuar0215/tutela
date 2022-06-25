import pandas as pd

df = pd.read_csv(
    "F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/2022/TUTELA_BORDER_MERGER_MM_W07.csv")

reg1 = df["region"] == "JABAR"
mask_jabar = reg1
df_filtered = df.loc[mask_jabar]
df_filtered.to_csv(
    'F:/SQAJABAR/DATA_SQA/DATA_STATISTIK_SQA/TUTELA/2022/JABAR/TUTELA_BORDER_MERGER_MM_W07_JABAR.csv', index=False)
