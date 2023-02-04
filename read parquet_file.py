import pandas as pd
parquet_file = r'C:\Users\User\Desktop\test\list of company websites.snappy.parquet'
pd.read_parquet(parquet_file, engine="pyarrow")