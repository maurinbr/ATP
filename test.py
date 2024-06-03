import pandas as pd

df = pd.read_csv("C:/Users/bruno/Downloads/listing_export_20240530054445.csv", encoding='utf-8', sep=';')

motif = df.loc[df.index==i].iloc[0,56:62].tolist()
motif = [x for x in motif if not pd.isna(x)]

print(motif)

