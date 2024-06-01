import pandas as pd

df = pd.read_csv("C:/Users/bruno/Downloads/listing_export_20240530054445.csv", encoding='utf-8', sep=';')

print(df.loc[df.index==5].iloc[0,1:12].sum())
